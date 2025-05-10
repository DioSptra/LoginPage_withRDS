#!/bin/bash

# Install dependencies untuk Flask app
echo "Installing dependencies..."
cd /home/ubuntu/login_rds
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Menghentikan proses Flask yang sudah berjalan sebelumnya
echo "Stopping any previous Flask processes..."
pkill -f app.py || true  # Memastikan tidak ada Flask app yang sedang berjalan

# Pastikan direktori tempat aplikasi Flask ada
mkdir -p /home/ubuntu/login_rds

# Jalankan Flask app di background
echo "Starting Flask app..."
nohup python3 /home/ubuntu/login_rds/app.py > out.log 2>&1 &  # Jalankan Flask di background dan redirect output ke out.log

echo "Deployment selesai!"
