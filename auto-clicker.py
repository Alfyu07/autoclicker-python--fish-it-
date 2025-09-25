import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# === KONFIGURASI ===
TOGGLE_KEY = KeyCode(char="=")     # Aktifkan/Nonaktifkan
INTERVAL_MS = 40                 # Jeda antar klik (dari akhir klik sebelumnya ke awal berikutnya)
DURATION_MS = 410                  # Lama menahan klik (dalam milidetik)
CLICK_REPEAT = True                # True = ulang terus, False = sekali saja

# === VARIABEL GLOBAL ===
clicking = False
mouse = Controller()

def perform_held_click():
    """Lakukan klik dengan menahan selama DURATION_MS"""
    mouse.press(Button.left)
    time.sleep(DURATION_MS / 1000.0)  # Tahan
    mouse.release(Button.left)

def clicker():
    global clicking
    while True:
        if clicking:
            if CLICK_REPEAT:
                # Mode ulang terus
                while clicking:
                    perform_held_click()
                    time.sleep(INTERVAL_MS / 1000.0)
            else:
                # Mode sekali jalan
                perform_held_click()
                clicking = False
                print("✅ Klik sekali selesai.")

        time.sleep(0.01)

def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
        if clicking:
            mode = "🔁 BERULANG" if CLICK_REPEAT else "🔂 SEKALI JALAN"
            print(f"🟢 AUTO-CLICKER (HOLD) DIMULAI! ({mode})")
            print(f"   Tahan klik: {DURATION_MS} ms | Interval: {INTERVAL_MS} ms")
            print(f"   Tekan '{TOGGLE_KEY}' untuk menghentikan.")
        else:
            print("🛑 AUTO-CLICKER DIHENTIKAN.")

# === JALANKAN ===
print(f"📌 Tekan '{TOGGLE_KEY}' untuk mengaktifkan/menonaktifkan")
print(f"⚙️  Hold Time: {DURATION_MS}ms | Interval: {INTERVAL_MS}ms | Repeat: {CLICK_REPEAT}")

click_thread = threading.Thread(target=clicker, daemon=True)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()