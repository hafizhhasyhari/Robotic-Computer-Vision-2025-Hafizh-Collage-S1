# Robotic-Computer-Vision-2025-Hafizh-Collage-S1
🤖 Robotic Computer Vision
<div align="center">
Halo saya Hafizh Hilman Asyhari dari indonesia!.
Dokumentasi perjalanan belajar 16 minggu untuk mata kuliah Robotic Computer Vision.

📜 Silabus Lengkap (16 Minggu) • 🚀 Quick Start • 🗂️ Struktur Repositori • 🎯 Proyek Utama

</div>

🎯 Fokus & Studi Kasus
Repositori ini mendokumentasikan pembelajaran saya dalam mata kuliah Robotic Computer Vision. Fokus utamanya adalah merancang dan mensimulasikan Robot Kurir Otonom (Autonomous Delivery Bot).
Tujuan Proyek Utama: Membangun sistem visi untuk robot yang memungkinkannya:
Bernavigasi di lingkungan yang telah dipetakan (misal: koridor).
Menghindari rintangan statis dan dinamis (misal: orang, pot tanaman).
Mendeteksi dan membaca target (misal: nomor pintu, QR code).
Berinteraksi dengan objek (misal: berhenti di depan pintu yang benar).

.

📚 Pembagian Materi
Perjalanan belajar ini dibagi menjadi empat bagian utama:

Bagian 1: Fondasi RCV (Minggu 1-4)

Pengenalan Robot Operating System (ROS) & OpenCV.

Pemrosesan gambar dasar, filter, dan deteksi tepi.

Transformasi geometris dan kalibrasi kamera.

Bagian 2: "Melihat" Dunia (Minggu 5-8)

Deteksi fitur (SIFT, ORB) dan pencocokan.

Optical Flow dan pelacakan objek.

Dasar-dasar Deep Learning (CNN) untuk klasifikasi.

Ujian Tengah Semester (Implementasi Pelacak Objek Sederhana)

Bagian 3: Memahami Ruang & Objek (Minggu 9-12)

Object Detection (YOLO, SSD) secara real-time.

Segmentasi Semantik (membedakan jalan, dinding, rintangan).

Visi Stereo dan Perkiraan Kedalaman (Depth Estimation).

Bagian 4: Navigasi & Aksi (Minggu 13-16)

Dasar-dasar SLAM (Simultaneous Localization and Mapping).

Integrasi Visi dengan ROS Navigation Stack.

Interaksi Objek (Visual Servoing).

Proyek Akhir (Demo Robot Kurir Otonom)
Gazebo (untuk simulasi)

## 🗂️ Struktur Repositori
Struktur folder ini dirancang untuk mencerminkan 13 komponen pembelajaran yang Anda minta, diatur per minggu atau per topik.

robotic-computer-vision/
---

''' bash
│
├── README.md                 # Halaman utama ini
├── SYLLABUS.md               # Silabus 16 minggu lengkap (ada di bawah)
├── LICENSE
├── .gitignore
├── requirements.txt          # Kebutuhan library Python
├── environment.yml           # Untuk setup environment Conda
│
├── 01-materi/                # Slide, PDF, dan catatan teori per minggu
│   ├── week-01/
│   └── ...
│
├── 02-praktik-lab/           # Kode implementasi hands-on (Jupyter/Python scripts)
│   ├── lab-01_setup_env/
│   ├── lab-02_image_filtering/
│   └── ...
│
├── 03-latihan-mandiri/       # Soal latihan tambahan dan solusi saya
│   ├── exercise-01/
│   └── ...
│
├── 04-pameran-showcase/      # Hasil visual (GIF, MP4, screenshot) dari lab
│   ├── week-02_canny_edge.gif
│   └── ...
│
├── 05-proyek-akhir/          # Proyek utama "Autonomous Delivery Bot"
│   ├── proposal.md
│   ├── src/                  # Kode sumber ROS/Python
│   ├── models/               # Model .h5 atau .pt (misal: YOLO)
│   ├── launch/               # File launch ROS
│   ├── worlds/               # File world Gazebo (simulasi)
│   └── docs/                 # Laporan akhir
│
├── 06-penelitian/            # Tinjauan paper, ringkasan, dan anotasi
│   ├── summary_orb-slam.pdf
│   └── review_yolov8.md
│
├── 07-studi-bisnis/          # Analisis aplikasi RCV di dunia nyata
│   ├── case_amazon_kiva.md
│   └── case_boston_dynamics.md
│
├── 08-karya-ip/              # Aset unik, diagram arsitektur, logo proyek
│   ├── diagrams/
│   └── logo/
│
├── 09-catatan-refleksi/      # Jurnal pembelajaran pribadi, 'aha moments'
│   └── learning_journal.md
│
├── 10-naskah-cerita/         # Ide-ide kreatif dan skrip film
│   └── ide_naskah.md
│
├── 11-pengabdian-masyarakat/ # Ide untuk aplikasi sosial
│   └── ide_robot_bantu_tunanetra.md
│
├── 12-reusable-tools/        # Skrip utilitas (misal: data augmentation)
│   ├── webcam_test.py
│   ├── ros_node_template.py
│   └── augmentation_script.py
│
└── media/                    # Gambar untuk README dan dokumentasi
    └── images/
        └── banner.png
'''

🚀 Quick Start
Prasyarat
Python 3.9+

OpenCV 4.x

ROS (Noetic atau Galactic/Humble direkomendasikan)

Gazebo (untuk simulasi)

Instalasi
Clone repositori ini:

Instalasi
1. Clone repositori ini:

'''
git clone https://github.com/[USERNAME_ANDA]/robotic-computer-vision.git
cd robotic-computer-vision
'''

2. Setup Python Environment (disarankan menggunakan venv):
'''
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
'''
3 Setup ROS Environment (jika menggunakan):
'''
# (Pastikan ROS sudah terinstal)
# Buat Catkin Workspace (jika perlu)
catkin_make
source devel/setup.bash
'''



