# Panduan Install Prometheus

## Apa itu Prometheus?
{{ small("**Prometheus** adalah open-source monitoring & alerting toolkit yang awalnya dibuat oleh SoundCloud, sekarang dikelola oleh **CNCF (Cloud Native Computing Foundation)**.

Prometheus banyak dipakai di dunia **cloud-native, DevOps, Kubernetes** untuk mengumpulkan metrik, menyimpannya, lalu membuat query/alert.") }}


## Fungsi Prometheus
{{ small("**Mengumpulkan metrik** dari aplikasi, server, container, database, dsb.") }}
{{ small("**Menyimpan data** dalam bentuk time-series (berdasarkan timestamp).") }}
{{ small("**Query data** dengan bahasa khusus bernama PromQL.") }}
{{ small("**Membuat alert** (via Alertmanager) kalau ada kondisi tertentu (misalnya CPU > 80%).") }}
{{ small("Bisa diintegrasikan dengan **Grafana** untuk visualisasi.") }}


## Cara Kerja Prometheus
1. {{ small("**Scraping** → Prometheus secara aktif menarik (pull) data dari endpoint HTTP yang expose /metrics.") }}
2. {{ small('**Time-series DB** → Data disimpan berdasarkan label (contoh: cpu_usage{instance="server1"}).') }}
3. {{ small("**Query** → Kita bisa jalankan query PromQL untuk analisis atau visualisasi.") }}
4. {{ small("**Alerting** → Jika kondisi match (misalnya disk_usage > 90%), alert dikirim ke Alertmanager → lalu diteruskan ke email, Slack, PagerDuty, dll.") }}


## Mempersiapkan server
{{ small("
Sebelum menginstal aplikasi atau perangkat lunak pada server, ada beberapa langkah penting yang harus dilakukan. Pertama, **update** untuk memastikan daftar paket terbaru tersedia di sistem. Selanjutnya, **upgrade** package yang sudah terinstal ke versi termutakhir guna memperbaiki celah keamanan dan bug. Selain itu, atur zona waktu server/VPS sesuai dengan lokasi pengguna agar catatan log server mudah dipantau dan tugas penjadwalan otomatis (**cron**) dapat berjalan sesuai waktu yang diharapkan.
") }}
```bash
sudo apt update
sudo apt upgrade -y
```
{{ small("Atur juga timezone server dan sesuaikan dengan daerah tempat tinggal Anda. disini saya mengatur timezone server ke Asia/Jakarta.") }}
```bash
sudo timedatectl set-timezone Asia/Jakarta
```


## Install Prometheus
{{ small("
Ada beberapa cara untuk menginstall prometheus, diantaranya dengan **Pre-Compiled Binary, APT Paket, Build From Fource, dan Docker Image**. Tapi pada tutorial kali ini Kita akan menginstall prometheus dengan metode **Pre-Compile Binary**. yaitu dengan mengunduh **biner yang sudah dicompile** langsung dari situs resmi Prometheus. Karena cara ini cocok untuk pengguna yang ingin langsung menggunakan Prometheus tanpa perlu melakukan *compile* sendiri.

[Pre-Compiled Binary](https://prometheus.io/download/)
") }}
```bash
sudo apt install -y wget tar
cd /tmp

wget https://github.com/prometheus/prometheus/releases/download/v3.5.0/prometheus-3.5.0.linux-amd64.tar.gz

tar -xvzf prometheus-3.5.0.linux-amd64.tar.gz
cd prometheus-3.5.0.linux-amd64
```
{{ small("*Perintah di atas akan masuk ke direktori /tmp dan mengunduh prometheus versi v3.5.0*") }}

{{ small("Buat user dan group untuk menjalankan prometheus, buat juga direktori untuk menyimpan binari dan file konfigurasi prometheus.") }}
```bash
sudo useradd --no-create-home --shell /bin/false prometheus

sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
```

{{ small("Pindahkan file binari dan file konfigurasi prometheus ke direktori /var/lib dan /etc.") }}
```bash
sudo mv prometheus.yml /etc/prometheus/
sudo mv prometheus /usr/local/bin/
sudo mv promtool /usr/local/bin/
```

{{ small("Ubah kepemilikan direktori `/etc/prometheus`, `/usr/bin/prometheus`, dan `/var/lib/prometheus` agar bisa diakses oleh user prometheus.") }}
```bash
sudo chown -R prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /var/lib/prometheus
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool
```

- **/etc/prometheus**: Tempat menyimpan file konfigurasi prometheus.
- **/usr/local/bin/prometheus**: Lokasi file executable prometheus
- **/var/lib/prometheus**: Tempat penyimpanan data prometheus yang berubah-ubah.

{{ small("Terakhir buat konfigurasi systemd agar prometheus berjalan sebagai service di VPS atau Server..") }}
```bash
sudo nano /etc/systemd/system/prometheus.service
```

{{ small("Salin dan tempel baris kode di bawah ini:") }}
```bash
[Unit]
Description=Prometheus
Documentation=https://prometheus.io/docs/introduction/overview
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus \

[Install]
WantedBy=multi-user.target
```

{{ small("Lalu Mulai dan Aktifkan Servicenya.") }}
```bash
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus
sudo systemctl status prometheus
```

{{ small("Pastikan statusnya **active (running)** seperti ini:") }}
{{ image_with_caption("images.status_prometheus", "Status Prometheus – monitoring overview", "100%") }}

{{ small("Buka Web Console Prometheus dengan menggunakan IP Address dengan port :9090 (*default port*).<br>
Masuk ke **Status -> Targets**, dan pastikan prometheus endpoint state up seperti gambar di bawah ini:<br>
`http://<server_ip>:9090/targets`
") }}
{{ image_with_caption("images.web_console_prometheus", "Tampilan Web Console Prometheus", "100%") }}



<!-- {{ small("") }}
```bash
```

1. {{ small("**Persiapan server** — (Update, Upgrade, Atur Zona Waktu).") }}
1. {{ small("**Prometheus** (server) — menyimpan metrics, job scraping.") }}
2. {{ small("**node_exporter** (di setiap host yang ingin dimonitor) — expose metrics host di :9100.") }}
3. {{ small("**Grafana** — visualisasi + import dashboard Prometheus (sebagai datasource).") }}

{{ small("") }} -->
