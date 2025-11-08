# Proposal Proyek: Autonomous Delivery Bot

**Mata Kuliah:** Robotic Computer Vision
**Mahasiswa:** Hafizh Hilman Asyhari
**Tanggal:** 18 September 2025
**Country:** Indonesia

## 1. Latar Belakang

Perkembangan e-commerce dan logistik *last-mile* membutuhkan solusi pengiriman yang efisien, cepat, dan otomatis. Robot kurir otonom (Autonomous Delivery Bots) menawarkan solusi untuk menavigasi lingkungan dalam ruangan (seperti gedung perkantoran, apartemen, atau kampus) untuk mengantarkan paket tanpa intervensi manusia.

Proyek ini bertujuan untuk merancang dan mensimulasikan *core vision system* untuk robot semacam itu.

## 2. Tujuan Proyek

Membangun sistem visi untuk robot simulasi (di Gazebo) yang memungkinkannya untuk:
1.  **Bernavigasi** secara mandiri di lingkungan koridor yang telah dipetakan.
2.  **Menghindari** rintangan statis (pot tanaman, kursi) dan dinamis (orang berjalan).
3.  **Mendeteksi** dan **Membaca** target spesifik (misalnya, nomor pintu atau QR code).
4.  **Berinteraksi** dengan target (misalnya, berhenti secara presisi di depan pintu yang benar).

## 3. Ruang Lingkup (Scope)

* **Fokus:** Sistem visi (CV) dan integrasinya dengan navigasi (Robotics).
* **Platform:** Simulasi penuh menggunakan **ROS**, **Gazebo**, dan **OpenCV**.
* **Out-of-Scope:** Desain perangkat keras, optimasi baterai, sistem mekanik kompleks (misal: lengan robot).

## 4. Tumpukan Teknologi (Technology Stack)

* **Simulasi:** ROS (Noetic/Galactic) + Gazebo
* **Persepsi (Visi):** OpenCV 4.x, Python 3
* **Model Visi:** CNN (via Keras/PyTorch), YOLO (untuk deteksi objek), U-Net (untuk segmentasi).
* **Navigasi:** ROS Navigation Stack (Gmapping/AMCL, move_base).

## 5. Milestone Utama

* **Minggu 1-4 (Fondasi):** Setup lingkungan, streaming video ROS, kalibrasi kamera, deteksi garis/tepi.
* **Minggu 5-8 (Persepsi 1):** Pelacakan objek, implementasi CNN sederhana. (UTS: Pelacak objek).
* **Minggu 9-12 (Persepsi 2):** Implementasi YOLO untuk deteksi rintangan/pintu, estimasi kedalaman (Depth).
* **Minggu 13-16 (Aksi):** Integrasi SLAM, integrasi ROS Navigation Stack, Visual Servoing untuk *docking* ke pintu. (UAS: Demo penuh).
