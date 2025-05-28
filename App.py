import time
import tkinter as tk
from tkinter import ttk, messagebox
from Dron import Dron
from MapFrame import MapFrameClass
from geopy.distance import geodesic
import math

# ===== Constants càmera SC1223 =====
FOV_H_DEG = 66

def calc_line_spacing(altitude, overlap):
    """Amplada coberta per la càmera a l'altitud (m) i FOV horitzontal."""
    fov_rad = math.radians(FOV_H_DEG)
    width = 2 * altitude * math.tan(fov_rad / 2)
    spacing = width * (1 - overlap)
    return spacing

# =============== PESTANYA STITCHING ================
def stitching_window(dron):
    stitch_window = tk.Toplevel()
    stitch_window.title("Stitching - Planificació de Vol")
    stitch_window.geometry("1200x850")

    # ============ Controls superiors (Stitching) ================
    frame_ctrl = ttk.LabelFrame(stitch_window, text="Stitching")
    frame_ctrl.pack(side="top", fill="x", padx=10, pady=3, anchor="n")

    vel_var = tk.DoubleVar(value=1.0)
    alt_var = tk.DoubleVar(value=5.0)
    thr_var = tk.DoubleVar(value=60.0)
    punts = []
    area_polygon = [None]
    traj_lines = []
    waypoints = []

    ttk.Label(frame_ctrl, text="Velocitat (m/s):").pack(side="left", padx=2)
    ttk.Entry(frame_ctrl, textvariable=vel_var, width=6).pack(side="left", padx=3)
    ttk.Label(frame_ctrl, text="Altitud (m):").pack(side="left", padx=2)
    ttk.Entry(frame_ctrl, textvariable=alt_var, width=6).pack(side="left", padx=3)
    ttk.Label(frame_ctrl, text="Threshold (%):").pack(side="left", padx=2)
    ttk.Entry(frame_ctrl, textvariable=thr_var, width=6).pack(side="left", padx=3)

    # Mode per posar punts
    area_mode = tk.BooleanVar(value=False)

    def crear_area():
        area_mode.set(True)
        punts.clear()
        if area_polygon[0]:
            area_polygon[0].delete()
            area_polygon[0] = None
        for l in traj_lines:
            l.delete()
        traj_lines.clear()

    def implementar_area():
        if len(punts) != 4:
            messagebox.showwarning("Error", "Primer has de definir una àrea de 4 punts.")
            return

        altitud = alt_var.get()
        threshold = thr_var.get() / 100
        sep = calc_line_spacing(altitud, threshold)
        if sep < 0.2:
            sep = 0.2

        p1, p2, p3, p4 = punts
        width = geodesic(p1, p2).meters
        n_lines = max(1, int(width / sep))

        # Esborra línies anteriors
        if not hasattr(stitch_window, "traj_lines"):
            stitch_window.traj_lines = []
        for line in stitch_window.traj_lines:
            try:
                line.delete()
            except:
                pass
        stitch_window.traj_lines = []

        # Genera el patró zig-zag i guarda waypoints per la missió
        previous = None
        traj_points = []

        for i in range(n_lines + 1):
            frac = i / n_lines
            x_start = p1[0] + (p2[0] - p1[0]) * frac
            y_start = p1[1] + (p2[1] - p1[1]) * frac
            x_end = p4[0] + (p3[0] - p4[0]) * frac
            y_end = p4[1] + (p3[1] - p4[1]) * frac

            # Alterna l'ordre per fer zig-zag
            if i % 2 == 0:
                segment = [(x_start, y_start), (x_end, y_end)]
            else:
                segment = [(x_end, y_end), (x_start, y_start)]

            # Dibuixa la línia de vol
            line = map_widget.set_path(segment, color="red", width=2)
            stitch_window.traj_lines.append(line)

            # Dibuixa la línia d'unió amb la següent
            if previous is not None:
                join = map_widget.set_path([previous, segment[0]], color="red", width=2)
                stitch_window.traj_lines.append(join)

            # GUARDA el punt inicial i final del segment:
            if previous is None:
                traj_points.append(segment[0])
            traj_points.append(segment[1])
            previous = segment[1]

        # GUARDA ELS WAYPOINTS per la missió
        waypoints.clear()
        waypoints.extend(traj_points)

        stitch_window.title(
            f"Stitching - {n_lines + 1} línies, {sep:.2f} m separació"
        )

    def aplicar_missio():
        if len(waypoints) < 2:
            messagebox.showerror("Missió", "Has de crear i implementar l'àrea abans.")
            return
        altitud = alt_var.get()
        velocitat = vel_var.get()
        # Construeix la missió per la teva API del dron:
        flight_plan = {
            "takeOffAlt": altitud,
            "waypoints": [
                {"lat": lat, "lon": lon, "alt": altitud}
                for lat, lon in waypoints
            ]
        }
        try:
            dron.executeMission(flight_plan, velocitat)
            messagebox.showinfo("Missió", "Missió enviada i executant-se!")
        except Exception as e:
            messagebox.showerror("Error missió", f"No s'ha pogut executar la missió:\n{str(e)}")

    ttk.Button(frame_ctrl, text="Crear àrea", command=crear_area).pack(side="left", padx=8)
    ttk.Button(frame_ctrl, text="Implementar àrea", command=implementar_area).pack(side="left", padx=8)
    ttk.Button(frame_ctrl, text="Aplicar Missió", command=aplicar_missio).pack(side="left", padx=8)
    ttk.Label(stitch_window, text="1- Clica 'Crear àrea', selecciona 4 punts, 'Implementar àrea', després 'Aplicar Missió'", foreground="brown").pack(pady=2)

    # ============ Mapa ================
    from MapFrame import MapFrameClass
    map_frame_class = MapFrameClass(dron)
    map_frame = map_frame_class.buildFrame(stitch_window)
    map_frame.pack(fill="both", expand=True)
    map_widget = map_frame_class.map_widget

    # --- Maneig de clics per afegir punts a l'àrea
    def map_click_event(coords):
        if not area_mode.get():
            return
        if len(punts) < 4:
            punts.append(coords)
            map_widget.set_marker(coords[0], coords[1], text=f"{len(punts)}")
            if len(punts) == 4:
                # Tanca l'àrea
                corners = [punts[0], punts[1], punts[2], punts[3], punts[0]]
                area_polygon[0] = map_widget.set_path(corners, color="blue", width=3)
                area_mode.set(False)
    map_widget.add_left_click_map_command(map_click_event)



# ============= FUNCIONS DE CONTROL DRON =============
def connect():
    global dron, connectBtn
    connection_string = 'tcp:127.0.0.1:5763'
    baud = 115200
    dron.connect(connection_string, baud)
    connectBtn['bg'] = 'green'
    connectBtn['fg'] = 'white'
    connectBtn['text'] = 'Conectado'

def arm(button):
    global dron, armBtn
    dron.arm()
    armBtn['bg'] = 'green'
    armBtn['fg'] = 'white'
    armBtn['text'] = 'Armado'

def takeoff():
    global dron, takeOffBtn, alt_entry
    try:
        alt = float(alt_entry.get())
        dron.takeOff(alt, blocking=False, callback=informar, params='VOLANDO')
        takeOffBtn['bg'] = 'yellow'
        takeOffBtn['text'] = 'Despegando....'
    except:
        messagebox.showerror("error", "Introducela altura para el despegue")

def informar(mensaje):
    global takeOffBtn, RTLBtn, connectBtn, armBtn, landBtn, dron
    messagebox.showinfo("showinfo", "Mensaje del dron:--->  " + mensaje)
    if mensaje == 'VOLANDO':
        takeOffBtn['bg'] = 'green'
        takeOffBtn['fg'] = 'white'
        takeOffBtn['text'] = 'En el aire'
    if mensaje == "EN CASA":
        RTLBtn['bg'] = 'green'
        RTLBtn['fg'] = 'white'
        RTLBtn['text'] = 'En casa'
        dron.disconnect()
        connectBtn['bg'] = 'dark orange'
        connectBtn['fg'] = 'black'
        connectBtn['text'] = 'Conectar'
        armBtn['bg'] = 'dark orange'
        armBtn['fg'] = 'black'
        armBtn['text'] = 'Armar'
        takeOffBtn['bg'] = 'dark orange'
        takeOffBtn['fg'] = 'black'
        takeOffBtn['text'] = 'Despegar'
        RTLBtn['bg'] = 'dark orange'
        RTLBtn['fg'] = 'black'
        RTLBtn['text'] = 'RTL'
    if mensaje == "EN TIERRA":
        landBtn['bg'] = 'green'
        landBtn['fg'] = 'white'
        landBtn['text'] = 'En tierra'
        dron.disconnect()
        connectBtn['bg'] = 'dark orange'
        connectBtn['fg'] = 'black'
        connectBtn['text'] = 'Conectar'
        armBtn['bg'] = 'dark orange'
        armBtn['fg'] = 'black'
        armBtn['text'] = 'Armar'
        takeOffBtn['bg'] = 'dark orange'
        takeOffBtn['fg'] = 'black'
        takeOffBtn['text'] = 'Despegar'
        landBtn['bg'] = 'dark orange'
        landBtn['fg'] = 'black'
        landBtn['text'] = 'Aterrizar'

def RTL():
    global dron, RTLBtn
    if dron.going:
        dron.stopGo()
    dron.RTL(blocking=False, callback=informar, params='EN CASA')
    RTLBtn['bg'] = 'yellow'
    RTLBtn['text'] = 'Retornando....'

def aterrizar():
    global dron, landBtn
    if dron.going:
        dron.stopGo()
    dron.Land(blocking=False, callback=informar, params='EN TIERRA')
    landBtn['bg'] = 'yellow'
    landBtn['text'] = 'Aterrizando....'

def change_speed(speed):
    global dron
    dron.changeNavSpeed(float(speed))

def go(direction):
    global dron
    if not dron.going:
        dron.startGo()
    dron.go(direction)

def showmap(dron):
    map_window = tk.Toplevel()
    map_window.title("Map Display")
    map_window.geometry("900x600")
    map_frame_class = MapFrameClass(dron)
    map_frame = map_frame_class.buildFrame(map_window)
    map_frame.pack(fill="both", expand=True)

# ============ DASHBOARD PRINCIPAL =============
def crear_ventana():
    global dron, altShowLbl, headingShowLbl, speedSldr, gradesSldr, speedShowLbl
    global takeOffBtn, connectBtn, armBtn, RTLBtn, landBtn, alt_entry

    dron = Dron()

    ventana = tk.Tk()
    ventana.title("Ventana con botones y entradas")
    ventana.geometry("1300x650")
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    controlFrame = tk.LabelFrame(ventana, text="Control")
    controlFrame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

    connectBtn = tk.Button(controlFrame, text="Conectar", bg="dark orange", command=connect)
    connectBtn.grid(row=0, column=0, padx=3, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    armBtn = tk.Button(controlFrame, text="Armar", bg="dark orange", command=lambda: arm(armBtn))
    armBtn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    takeOffFrame = tk.Frame(controlFrame)
    takeOffFrame.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
    alt_entry = tk.Entry(takeOffFrame)
    alt_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
    takeOffBtn = tk.Button(takeOffFrame, text="Despegar", bg="dark orange", command=takeoff)
    takeOffBtn.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    RTLBtn = tk.Button(controlFrame, text="RTL", bg="dark orange", command=RTL)
    RTLBtn.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    speedSldr = tk.Scale(controlFrame, label="Velocidad (m/s):", resolution=1, from_=0, to=20, tickinterval=5,
                         orient=tk.HORIZONTAL, command=change_speed)
    speedSldr.set(1)
    speedSldr.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

    navFrame = tk.LabelFrame(controlFrame, text="Navegación")
    navFrame.grid(row=5, column=0, padx=50, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
    for i, (txt, cmd) in enumerate([
        ("NW", lambda: go("NorthWest")), ("No", lambda: go("North")), ("NE", lambda: go("NorthEast")),
        ("We", lambda: go("West")), ("St", lambda: go("Stop")), ("Ea", lambda: go("East")),
        ("SW", lambda: go("SouthWest")), ("So", lambda: go("South")), ("SE", lambda: go("SouthEast")),
    ]):
        tk.Button(navFrame, text=txt, bg="dark orange", command=cmd)\
            .grid(row=i//3, column=i%3, padx=2, pady=2, sticky=tk.N + tk.S + tk.E + tk.W)

    MapButton = tk.Button(controlFrame, text="Mostrar mapa", bg="dark orange",
                          command=lambda: showmap(dron))
    MapButton.grid(row=6, column=0, padx=5, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

    userFrame = tk.LabelFrame(ventana, text="Funcionalidades extra")
    userFrame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)
    userFrame.rowconfigure(0, weight=1)
    userFrame.rowconfigure(1, weight=1)
    userFrame.rowconfigure(2, weight=1)
    userFrame.rowconfigure(3, weight=1)
    userFrame.rowconfigure(4, weight=1)
    userFrame.rowconfigure(5, weight=1)
    userFrame.rowconfigure(6, weight=1)
    userFrame.rowconfigure(7, weight=1)
    userFrame.rowconfigure(8, weight=1)
    userFrame.rowconfigure(9, weight=1)
    userFrame.rowconfigure(10, weight=1)
    userFrame.columnconfigure(0, weight=1)
    userFrame.columnconfigure(1, weight=1)
    userFrame.columnconfigure(2, weight=1)
    userFrame.columnconfigure(3, weight=1)

    landBtn = tk.Button(userFrame, text="Aterrizar", bg="dark orange", command=aterrizar)
    landBtn.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=tk.N + tk.E + tk.W)
    earth_button = tk.Button(userFrame, text="Earth", bg="Dark orange", command=lambda: print("Earth!"))
    earth_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky=tk.N + tk.E + tk.W)
    stitchingBtn = tk.Button(userFrame, text="Stitching", bg="light grey", command=lambda: stitching_window(dron))
    stitchingBtn.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky=tk.N + tk.E + tk.W)

    return ventana


if __name__ == "__main__":
    ventana = crear_ventana()
    ventana.mainloop()