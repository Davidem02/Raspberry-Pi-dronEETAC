from picamera2 import Picamera2
import cv2
import time
from dronLink.Dron import Dron
import sys
import os
import glob
from stitching import Stitcher
stitcher = Stitcher()
stitcher = Stitcher(detector="sift", confidence_threshold=0.2)

# ========== INICIALITZACIÓ ==========
start = False
ultima_telemetria = None
foto_interval = 0.5
foto_count = 1
index_imatge = 1

# Obrir arxiu per escriure telemetria
f = open('Telemetria.txt', 'w')

# ========== FUNCIONS ==========
def processar_telemetria(telemetryInfo):
    try:
        f.write(str(telemetryInfo) + '\n')
        print('[INFO] Telemetria capturada:', telemetryInfo)
    except ValueError as e:
        print('[ERROR] No s\'ha pogut escriure la telemetria:', e)

def callback_telemetria(info):
    global ultima_telemetria
    ultima_telemetria = info

# ========== CONNEXIÓ DRON ==========
dron = Dron()
dron.connect('/dev/ttyAMA0', 115200)
print('[INFO] Connectat al dron')

try:
    dron.send_telemetry_info(callback_telemetria)
except Exception as e:
    print(f"[ERROR] No s'ha pogut rebre telemetria: {e}")
    dron.disconnect()
    sys.exit(1)

# Esperar fins que flightMode sigui "GUIDED"
print('[INFO] Esperant mode "GUIDED"...')
while True:
    if ultima_telemetria and ultima_telemetria.get("flightMode") == "AUTO":
        print('[INFO] Mode "GUIDED" detectat. Començant la captura.')
        break
    time.sleep(0.5)

# ========== INICIALITZAR CÀMERA ==========
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480), "format": "RGB888"}))
picam2.start()
print("[INFO] Previsualització iniciada. Prem 'q' per sortir.")

# ========== CAPTURA ==========
start_time = time.time()
last_capture_time = 0

while True:
    frame = picam2.capture_array()
    cv2.imshow('Camara USB', frame)

    current_time = time.time()
    elapsed_time = current_time - start_time

    # A partir del 3r segon, captura cada 5 segons
    if elapsed_time >= 3 and current_time - last_capture_time >= foto_interval:
        filename = f"imatge{foto_count}.jpg"
        picam2.capture_file(filename)
        print(f"[{int(elapsed_time)}s] Foto desada: {filename}")
        foto_count += 1
        last_capture_time = current_time
        dron.send_telemetry_info(processar_telemetria)

    # Sortir amb 'q'
    if cv2.waitKey(1) & 0xFF == ord('q') or ultima_telemetria.get("flightMode") == "LAND":
        break
        
        
panorama = stitcher.stitch(["imatge?.jpg"])
panorama.save('panorama.jpg')
# ========== FINALITZACIÓ ==========
picam2.stop()
cv2.destroyAllWindows()
f.close()
print("[INFO] Finalitzat.")