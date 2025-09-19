# Monitoring AWS Instance dengan CloudWatch


## Kenapa Harus Monitoring?
{{ small("
Bayangkan kamu punya server di AWS (EC2). Server itu jalanin aplikasi penting — entah web, API, database, atau service internal. Kalau server tiba-tiba CPU full, RAM habis, atau disk penuh, maka:
") }}

- Aplikasi jadi lambat atau bahkan mati.
- User mengalami downtime.
- Bisa keluar biaya ekstra kalau ada auto-scaling tidak terkendali.

{{ small("Monitoring dengan AWS CloudWatch membantu kita:") }}

- Melihat performa instance (CPU, RAM, Disk, Network).
- Membuat alarm kalau resource tinggi/rendah.
- Mengambil keputusan cepat (scale up, scale out, atau optimasi).


## Cara Kerja CloudWatch
1. {{ small("Basic Monitoring (default)") }}
    - Semua EC2 otomatis mengirim metric ke CloudWatch, seperti:
        - CPU Utilization
        - Network In/Out
        - Disk Read/Write
    - Interval: 5 menit (atau 1 menit kalau diaktifkan detailed monitoring).
2. {{ small("Custom Monitoring (CloudWatch Agent)") }}
    - Untuk metric yang tidak dikirim default (misalnya RAM, swap, disk usage).
    - Harus install CloudWatch Agent di dalam EC2.
    - Agent mengumpulkan data OS lalu push ke CloudWatch.
3. {{ small("CloudWatch Alarm") }}
    - Bisa bikin trigger kalau CPU > 80%, RAM > 90%, Disk > 90%.
    - Alarm bisa kirim notifikasi via SNS (email, Slack, ntfy lewat Lambda, dsb).


## Monitoring CPU (default metric)
### Buat Dashboard
1. {{ small("Buka AWS Console → CloudWatch.") }}
2. {{ small("Masuk ke dashboard → Create dashboard.") }}
3. {{ small("Klik nama dashboard yang baru dibuat → Add Widget (tombol **+** sebelah kanan). ") }}
4. {{ small("Pilih Metrics → EC2 → Per-Instance Metrics.") }}
5. {{ small("Pilih instance ID → klik CPUUtilization → Create Widget.") }}
6. {{ small("Akan muncul grafik penggunaan CPU dalam %.") }}

{{ small("CPU sudah otomatis termonitor tanpa install apapun") }}


## Monitoring RAM & Disk (CloudWatch Agent)
{{ small("Sekarang, kita akan install CloudWatch Agent yang akan dijalankan pada EC2 instance dan akan mengirimkan matriks data ke Cloudwatch.") }}

### Assign role ke EC2 instance
{{ image_with_caption("images.cloud_watch_agent_server_policy", "Assign role ke EC2 instance", "100%") }}

{{ small("
Kita perlu membuat role untuk EC2 instance, attatch permission CloudWatchAgentServerPolicy ke dalam role, lalu attach role tersebut ke EC2 instance. permission ini akan memungkinkan EC2 instance untuk mengirimkan log ke CloudWatch.
") }}

### Download & Install CloudWatch Agent
{{ small("
Sekarang, Connect ke EC2 instance menggunakan SSH atau apapun itu, dan jalankan perintah berikut untuk menginstal agent.
") }}
```bash
# Update package
sudo apt update -y

wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb

sudo dpkg -i amazon-cloudwatch-agent.deb
```

### Buat Configuration
{{ small("
Buat file `amazon-cloudwatch-agent.json` tempat kita akan menulis script yang akan dijalankan menggunakan agent.
") }}
```bash title="amazon-cloudwatch-agent.json"
sudo nano /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

{{ small("
Kemudian paste script yang di bawah ini. Di sini, kita akan mendapatkan data disk dan RAM setiap menit selama 60s, tetapi kita akan mengirimkan data ke Cloudwatch setiap 5 menit atau 300s.
") }}
```json
{
    "agent": {
        "metrics_collection_interval": 300,
        "run_as_user": "root"
    },
    "metrics": {
        "append_dimensions": {
            "InstanceId": "${aws:InstanceId}"
        },
        "metrics_collected": {
            "mem": {
                "measurement": [
                    "mem_used_percent"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ]
            },
            "disk": {
                "measurement": [
                    "used_percent"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ]
            }
        }
    }
}
```

### Start CloudWatch agent
{{ small("
Setelah Anda menyimpan skrip di atas di berkas amazon-cloudwatch-agent.json, Anda perlu menjalankan agent tersebut agar dapat mengirimkan data ke Cloudwatch.
") }}

```bash
sudo systemctl enable amazon-cloudwatch-agent
sudo systemctl start amazon-cloudwatch-agent
```

### Cek Status agent
```bash
sudo systemctl status amazon-cloudwatch-agent
```
{{ small("Pastikan statusnya **active (running)** seperti ini:") }}
{{ image_with_caption("images.status_amazone_cloud_watch_agent", "Status Amazon Cloud Watch Agent – monitoring overview", "100%") }}

### Buat Dashboard
<ol>
    <li>{{ small("Buka CloudWatch → Dashboards.") }}</li>
    <li>{{ small("Klik Create dashboard → beri nama EC2-Monitoring.") }}</li>
    <li>{{ small("Klik nama dashboard yang baru dibuat → Add Widget (tombol **+** sebelah kanan).") }}</li>
    <li>
        {{ small("Pilih Metrics → CWAgent → InstanceId.") }}
        <br>
        {{ image_grid([
            ("images.metric_cwagent", "CWAgent"),
            ("images.metric_instanceid", "InstanceId"),
        ], "250", "100") }}
    </li>
    <li>
        {{ small("Pilih instance ID → klik mem_used_percent → Create Widget.") }}
        {{ image_with_caption("images.create_widget_mem_used_percent", "Create Widget Memory", "90%") }}
    </li>
</ol>
