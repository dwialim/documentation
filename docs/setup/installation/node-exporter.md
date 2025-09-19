# Panduan Install Node Exporter

## Apa itu Node Exporter?
{{ small("
Node Exporter adalah **agen monitoring** yang digunakan untuk mengumpulkan metrics hardware dan sistem operasi. Prometheus sendiri hanya bertindak sebagai **server monitoring** dan tidak bisa langsung mengumpulkan data dari sistem. Node Exporter lah yang akan mengumpulkan data, lalu Prometheus akan menarik (scrape) data tersebut. data metriks yang dikumpulkan seperti: CPU usage, Memori (RAM), Disk usage, Load average, Network traffic, Proses yang berjalan
") }}


## Fungsi Node Exporter
{{ small("
Node Exporter meng-**expose** berbagai metrics terkait host (server) dalam format HTTP endpoint (`:9100/metrics`), supaya Prometheus bisa **scrape** data tersebut secara periodik.
") }}


## Cara Kerja Node Exporter
1. {{ small("Install Node Exporter di server target (Linux biasanya).") }}
2. {{ small("Node Exporter jalan sebagai service dan expose metrics di port `9100`.") }}
3. {{ small("Prometheus melakukan scrape ke `http://<server_ip>:9100/metrics`.") }}
4. {{ small("Data disimpan Prometheus dan bisa divisualisasikan di Grafana.") }}


## Install Node Exporter
{{ small("Sama seperti prometheus, Kita akan menginstall Node Exporter dari [Pre-Compile Binary](https://prometheus.io/download/#node_exporter) yang sudah disediakan.") }}
```bash
cd /tmp

wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz

tar -xvzf node_exporter-*.*-amd64.tar.gz
cd node_exporter-*.*-amd64
```
{{ small("
Kemudian pindahkan binari node exporter ke `/usr/local/bin`. Dan agar lebih aman, buat juga user dan group yang akan digunakan untuk menjalankan **Node Exporter**. Terakhir ubah kepemilikan direktorinya.
") }}
```bash
sudo useradd -rs /bin/false node_exporter

sudo mv node_exporter /usr/local/bin/
sudo chown node_exporter:node_exporter /usr/local/bin/node_exporter
```

{{ small("Buat konfigurasi node exporter di Systemd. Ini bertujuan agar node exporter berjalan sebagai service.") }}
```bash
sudo nano /etc/systemd/system/node_exporter.service
```

{{ small("Salin dan tempel baris kode di bawah ini:") }}
```bash
[Unit]
Description=Prometheus exporter for machine metrics

[Service]
Restart=always
User=prometheus
ExecStart=/usr/local/bin/node_exporter
ExecReload=/bin/kill -HUP $MAINPID
TimeoutStopSec=20s
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
```

{{ small("Lalu Mulai dan Aktifkan Servicenya.") }}
```bash
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter
sudo systemctl status node_exporter
```

{{ small("Pastikan statusnya **active (running)** seperti ini:") }}
{{ image_with_caption("images.status_node_exporter", "Status Node Exporter – monitoring overview", "100%") }}

## Menghubungkan Node Exporter ke Prometheus
{{ small("
Sekarang kita akan mencoba menghubungkan node exporter agar dapat di scrape oleh prometheus. Nantinya Kita bisa melihat metriks-metrik yang dikumpulkan oleh node exporter. Untuk antisipasi kegagalam, pertama Kita cadagkan dulu konfigurasi default dari prometheus. Kemudian buat file konfigurasi yang baru.
") }}
```bash
sudo mv /etc/prometheus/prometheus.yml /etc/prometheus/prometheus.yml.bak
sudo nano /etc/prometheus/prometheus.yml
```

{{ small("Salin dan tempelkan baris konfigurasi di bawah ini:") }}
```bash
global:
  scrape_interval: 15s        # default untuk semua job (interval pengambilan data)
  evaluation_interval: 15s    # evaluasi aturan setiap 15 detik

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node-exporter-localhost"
    scrape_interval: 5s       # override khusus Node Exporter (optional)
    static_configs:
      - targets: ["localhost:9100"]
```
{{ small("Kemudian restart service prometheus.") }}
```bash
sudo systemctl restart prometheus
```

{{ small("
Kemudian Kita cek konfigurasinya sudah berhasil apa belum.<br>
Masuk ke Prometheus **Web Console -> Status -> Targets**. Pastikan Endpoint sudah bertambah **node-exporter-localhost** dan berstate ***up*** seperti ini:
") }}
{{ image_with_caption("images.endpoint_node_exporter", "Endpoint Node Exporter", "100%") }}
