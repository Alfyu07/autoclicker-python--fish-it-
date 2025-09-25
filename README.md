# Auto Clicker Python

Auto Clicker sederhana menggunakan Python dan `pynput` untuk melakukan klik mouse otomatis dengan interval dan durasi yang dapat diatur.

## Persyaratan

- Python 3.x
- Modul `pynput`

## Instalasi

1. **Download dan install [Python 3.x](https://www.python.org/downloads/) jika belum terpasang di komputer Anda.**

2. **Clone atau download repositori ini.**

3. **Masuk ke folder proyek:**

   ```bash
   cd autoclicker-python--fish-it-
   ```

4. **(Opsional) Buat dan aktifkan virtual environment:**

   ```bash
   python -m venv venv
   # Aktifkan di Windows:
   venv\Scripts\activate
   # Aktifkan di macOS/Linux:
   source venv/bin/activate
   ```

5. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

## Menjalankan Auto Clicker

1. **Jalankan script:**

   ```bash
   python auto-clicker.py
   ```

2. **Instruksi Penggunaan:**
   - Tekan tombol `=` pada keyboard untuk mengaktifkan/mematikan auto clicker.
   - Klik akan dilakukan otomatis sesuai pengaturan interval dan durasi di script.
   - Untuk menghentikan, tekan kembali tombol `=`.

## Konfigurasi

Ubah parameter berikut di file `auto-clicker.py` sesuai kebutuhan:

- `TOGGLE_KEY`: Tombol keyboard untuk toggle.
- `INTERVAL_MS`: Jeda antar klik (ms).
- `DURATION_MS`: Lama menahan klik (ms).
- `CLICK_REPEAT`: `True` untuk klik berulang, `False` untuk sekali klik.

---

**Catatan:**  
Jalankan script di lingkungan yang aman dan gunakan secara bertanggung jawab.
