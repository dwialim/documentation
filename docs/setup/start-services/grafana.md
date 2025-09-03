# Start the Grafana server
{{
small("Topik ini berisi petunjuk untuk memulai server Grafana. Untuk perubahan konfigurasi tertentu, Anda mungkin perlu memulai ulang server Grafana agar perubahan tersebut berlaku.

Petunjuk berikut memulai proses `grafana-server` sebagai pengguna `grafana`, yang dibuat selama instalasi paket.

Jika Anda menginstal dengan APT repository atau `.deb` package, Anda dapat menjalankan server menggunakan systemd atau init.d. Jika Anda menginstal berkas biner `.tar.gz`, jalankan berkas biner tersebut.")
}}

<!-- {{ h1("Topik ini berisi petunjuk untuk memulai")}}<br>
{{ h2("Topik ini berisi petunjuk untuk memulai")}}<br>
{{ h3("Topik ini berisi petunjuk untuk memulai")}}<br>
{{ h4("Topik ini berisi petunjuk untuk memulai")}}<br>
{{ h5("Topik ini berisi petunjuk untuk memulai")}}<br>
{{ h6("Topik ini berisi petunjuk untuk memulai")}}<br>
{{ small("Topik ini berisi petunjuk untuk memulai")}} -->

## Linux
{{ small("Sub-bagian berikut menjelaskan tiga metode untuk memulai dan memulai ulang server Grafana: dengan systemd, initd, atau dengan langsung menjalankan binernya. Anda hanya perlu mengikuti satu set instruksi, tergantung pada konfigurasi mesin Anda.") }}

### Start the Grafana server with systemd
{{ small("Selesaikan langkah-langkah berikut untuk memulai server Grafana menggunakan systemd dan verifikasi bahwa server tersebut berjalan.") }}

1. {{ small("Untuk memulai service, jalankan perintah berikut:") }}
```bash
sudo systemctl daemon-reload
sudo systemctl start grafana-server
```
2. {{ small("Untuk memverifikasi bahwa service berjalan, jalankan perintah berikut:") }}
```bash
sudo systemctl status grafana-server
```

### Configure the Grafana server to start at boot using systemd
{{ small("Untuk konfigurasi server Grafana agar mulai saat boot, jalankan perintah berikut:") }}
```bash
sudo systemctl enable grafana-server.service
```

#### Serve Grafana on a port < 1024

{{ small("Jika Anda menggunakan `systemd` dan ingin memulai Grafana pada port yang lebih rendah dari 1024 Anda harus menambahkan penggantian unit `systemd`.") }}

1. {{ small("Jalankan perintah berikut untuk membuat berkas pengganti di editor yang Anda konfigurasikan.") }}
```bash
# Alternatively, create a file in /etc/systemd/system/grafana-server.service.d/override.conf
sudo systemctl edit grafana-server.service
```
```bash
# Alternatively, create a file in /etc/systemd/system/grafana-server.service.d/override.conf
sudo systemctl edit grafana-server.service
```
2. {{ small("Tambahkan pengaturan tambahan berikut untuk memberikan kemampuan {{ code('CAP_NET_BIND_SERVICE') }}") }}.</br>
{{ small("To learn more about capabilities, refer to [capabilities(7) — Linux manual page](https://man7.org/linux/man-pages/man7/capabilities.7.html).") }}


### Restart the Grafana server using systemd
{{ small("Untuk memulai ulang server Grafana, jalankan perintah berikut:") }}

```bash
sudo systemctl restart grafana-server
```

!!! info "**CATATAN**"
    Pengguna SUSE atau openSUSE mungkin perlu memulai server dengan metode systemd, lalu menggunakan metode init.d untuk mengonfigurasi Grafana agar memulai saat boot.

#### Start the Grafana server using init.d
{{ small("Selesaikan langkah-langkah berikut untuk memulai server Grafana menggunakan init.d dan verifikasi bahwa server tersebut berjalan:") }}

1. {{ small("Untuk memulai server Grafana, jalankan perintah berikut:") }}
```bash
sudo service grafana-server start
```
2. {{ small("Untuk memverifikasi bahwa layanan berjalan, jalankan perintah berikut:") }}
```bash
sudo service grafana-server status
```

#### Configure the Grafana server to start at boot using init.d
{{ small("Untuk mengonfigurasi server Grafana agar mulai saat boot, jalankan perintah berikut:") }}
```bash
sudo update-rc.d grafana-server defaults
```

#### Restart the Grafana server using init.d
{{ small("Untuk restart server Grafana, jalankan perintah berikut:") }}
```bash
sudo service grafana-server restart
```

#### Start the server using the binary
{{ small("Biner `Grafana` .tar.gz membutuhkan direktori kerja yang merupakan direktori instalasi root tempat biner dan folder `public` berada.

Untuk memulai server Grafana, jalankan perintah berikut:
") }}
```bash
./bin/grafana server
```


## Next steps
{{ small("Setelah server Grafana aktif dan running, pertimbangkan untuk mengambil langkah berikutnya:") }}

- Lihat [Get Started]({{ link("grafana_get_started") }}) untuk mempelajari cara membuat dasbor pertama Anda.
<!-- - Lihat {ref}`grafana-start <Get Started>` untuk mempelajari cara membuat dasbor pertama Anda. -->
- Lihat [Configuration]({{ link("grafana_config") }}) untuk mempelajari cara menyesuaikan lingkungan Anda.

