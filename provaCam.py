from picamera2 import Picamera2
import cv2
import time

# Inicialitza i configura la càmera Pi
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

print("Previsualització en marxa. Prem 'q' per sortir.")

# Variables de control de temps
start_time = time.time()
last_capture_time = 0
foto_interval = 5
foto_count = 1

while True:
    # Captura un frame de la càmera Pi
    frame = picam2.capture_array()

    # Converteix a escala de grisos
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostra el frame en una finestra anomenada 'Camara USB'
    cv2.imshow('Camara USB', gray)

    current_time = time.time()
    elapsed_time = current_time - start_time

    # A partir del tercer segon, fes una foto cada 5 segons
    if elapsed_time >= 3 and current_time - last_capture_time >= foto_interval:
        filename = f"imatge{foto_count}.jpg"
        picam2.capture_file(filename)
        print(f"[{int(elapsed_time)}s] Foto desada: {filename}")
        foto_count += 1
        last_capture_time = current_time

    # Si es prem la tecla 'q', surt del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Atura la càmera i tanca la finestra
picam2.stop()
cv2.destroyAllWindows()
