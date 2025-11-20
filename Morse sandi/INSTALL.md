# Panduan Install Python 3.10 dan Setup Virtual Environment

## Masalah
- `morse-audio-decoder` membutuhkan Python 3.10 atau 3.11
- Sistem Anda memiliki Python 3.12 (Windows) dan Python 3.13 (WSL)
- Perlu install Python 3.10

## Solusi 1: Install Python 3.10 di Windows (Recommended)

### Langkah 1: Download Python 3.10
```
Download dari: https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe
```

### Langkah 2: Install Python 3.10
1. Jalankan installer
2. **PENTING:** Centang "Add Python 3.10 to PATH"
3. Pilih "Customize installation"
4. Pastikan "pip" dan "py launcher" tercentang
5. Install

### Langkah 3: Buat Virtual Environment dengan Python 3.10
```powershell
# Pindah ke folder Morse sandi
cd "c:\Users\infin\Documents\LABS\POLTEK\Morse sandi"

# Buat venv dengan Python 3.10
py -3.10 -m venv venv

# Aktifkan venv
.\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install morse-audio-decoder
pip install morse-audio-decoder

# Verifikasi
python --version
# Should show: Python 3.10.11
```

## Solusi 2: Install Python 3.10 di WSL

```bash
# Di WSL
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev

# Buat venv
cd /mnt/c/Users/infin/Documents/LABS/POLTEK/"Morse sandi"
python3.10 -m venv venv

# Aktifkan
source venv/bin/activate

# Install
pip install --upgrade pip
pip install morse-audio-decoder
```

## Solusi 3: Gunakan Python 3.12 dengan Library Alternatif

Jika tidak bisa install Python 3.10, gunakan library alternatif yang support Python 3.12:

```powershell
# Dengan Python 3.12
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1

# Install alternative libraries
pip install scipy numpy

# Gunakan script custom (bukan morse-audio-decoder)
```

## Verifikasi Instalasi

```powershell
# Check versi Python yang terinstall
py --list

# Should show:
# -V:3.12 *        Python 3.12 (64-bit)
# -V:3.10          Python 3.10 (64-bit)  <- Setelah install

# Check versi di venv
python --version
pip --version
```

## Troubleshooting

### Error: "py -3.10" not found
- Python 3.10 belum terinstall
- Download dan install dari link di atas

### Error: "morse-audio-decoder" requires Python >=3.10,<3.11
- Virtual environment menggunakan Python yang salah
- Hapus venv dan buat ulang dengan Python 3.10

### PowerShell execution policy error
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Quick Commands

```powershell
# Hapus venv lama (jika ada)
Remove-Item -Recurse -Force venv

# Buat venv baru dengan Python 3.10
py -3.10 -m venv venv

# Aktifkan
.\venv\Scripts\Activate.ps1

# Install packages
pip install morse-audio-decoder

# Run script
python solve.py
```
