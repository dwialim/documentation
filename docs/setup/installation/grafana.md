# Install Grafana
{{ small("Grafana adalah platform open-source untuk monitoring dan observability yang memungkinkan Anda memvisualisasikan metrics, logs, dan traces dari berbagai sumber data.") }}

## Supported operating systems
{{ small("Grafana mendukung sistem operasi berikut:") }}

- [Debian or Ubuntu](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)
- [RHEL or Fedora](https://grafana.com/docs/grafana/latest/setup-grafana/installation/redhat-rhel-fedora/)
- [SUSE or openSUSE](https://grafana.com/docs/grafana/latest/setup-grafana/installation/suse-opensuse/)
- [macOS](https://grafana.com/docs/grafana/latest/setup-grafana/installation/mac/)
- [Windows](https://grafana.com/docs/grafana/latest/setup-grafana/installation/windows/)

???+ note "**CATATAN**"
    Pemasangan Grafana pada sistem operasi lain dimungkinkan, tetapi tidak disarankan atau didukung.


## Hardware recommendations
{{ small("Grafana membutuhkan sumber daya sistem minimum:") }}

- Minimum recommended memory: 512 MB
- Minimum recommended CPU: 1 core


## Supported databases
{{
    small("Grafana membutuhkan basis data untuk menyimpan data konfigurasinya, seperti pengguna, sumber data, dan dasbor. Persyaratan spesifiknya bergantung pada ukuran instalasi Grafana dan fitur yang Anda gunakan.

Grafana mendukung database berikut:
    ")
}}

- [SQLite 3](https://www.sqlite.org/index.html)
- [MySQL 8.0+](https://www.mysql.com/support/supportedplatforms/database.html)
- [PostgreSQL 12+](https://www.postgresql.org/support/versioning/)

{{ small("Secara default Grafana menggunakan database SQLite tertanam, yang disimpan di lokasi instalasi Grafana.") }}
!!! info "**CATATAN**"
    SQLite berfungsi dengan baik jika lingkungan Anda kecil, tetapi tidak disarankan ketika lingkungan Anda mulai berkembang. Untuk informasi lebih lanjut tentang batasan SQLite, Lihat [Penggunaan SQLite yang Tepat](https://www.sqlite.org/whentouse.html). Jika Anda menginginkan [high availability](https://grafana.com/docs/grafana/latest/setup-grafana/set-up-for-high-availability/), Anda harus menggunakan basis data MySQL atau PostgreSQL. Untuk informasi tentang cara menentukan parameter konfigurasi basis data di dalam berkas ```grafana.ini```, lihat [[database]](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#database).

{{ small("Grafana mendukung versi-versi basis data ini yang secara resmi didukung oleh proyek pada saat versi Grafana dirilis. Ketika versi Grafana tidak lagi didukung, Grafana Labs mungkin juga akan menghentikan dukungan untuk versi basis data tersebut. Lihat tautan di atas untuk mengetahui kebijakan dukungan masing-masing proyek.") }}
!!! info "**CATATAN**"
    PostgreSQL versi 10.9, 11.4, dan 12-beta2 terdampak bug (dilacak oleh proyek PostgreSQL sebagai [bug #15865](https://www.postgresql.org/message-id/flat/15865-17940eacc8f8b081%40postgresql.org)) yang mencegah versi-versi tersebut digunakan dengan Grafana. Bug ini telah diperbaiki di versi PostgreSQL yang lebih baru.

!!! info "**CATATAN**"
    Biner dan gambar Grafana mungkin tidak berfungsi dengan basis data yang tidak didukung, meskipun mereka mengklaim sebagai sistem drop-in atau mereplikasi API sebaik mungkin. Biner dan gambar yang dibangun dengan [BoringCrypto](https://pkg.go.dev/crypto/internal/boring) mungkin memiliki masalah yang berbeda dengan distribusi Grafana lainnya.


## Supported web browsers
{{ small("Grafana mendukung versi terbaru dari peramban berikut. Versi lama peramban ini mungkin tidak didukung, jadi Anda harus selalu memperbarui ke versi peramban terbaru saat menggunakan Grafana.") }}

!!! info "**CATATAN**"
    Aktifkan JavaScript di browser Anda. Menjalankan Grafana tanpa enable JavaScript di browser tidak didukung.

- Chrome/Chromium
- Firefox
- Safari
- Microsoft Edge


<!-- | Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource | -->


## Install from APT repository

{{ small("If you install from the APT repository, Grafana automatically updates when you run apt-get update.") }}

| Grafana Version				| Package				| Repository														|
|-------------------------------|:----------------------|:------------------------------------------------------------------|
| `Grafana Enterprise`			| grafana-enterprise	| [https://apt.grafana.com](https://apt.grafana.com) stable main	|
| `Grafana Enterprise (Beta)`	| grafana-enterprise	| [https://apt.grafana.com](https://apt.grafana.com) beta main		|
| `Grafana OSS`					| grafana				| [https://apt.grafana.com](https://apt.grafana.com) stable main	|
| `Grafana OSS (Beta)`			| grafana				| [https://apt.grafana.com](https://apt.grafana.com) beta main		|

!!! info "**CATATAN**"
    Grafana Enterprise adalah edisi yang direkomendasikan dan standar. Edisi ini tersedia gratis dan mencakup semua fitur edisi OSS. Anda juga dapat meningkatkan ke [paket fitur Enterprise lengkap](https://grafana.com/products/enterprise/?utm_source=grafana-install-page), yang mendukung [plugin Enterprise](https://grafana.com/grafana/plugins/?enterprise=1&utcm_source=grafana-install-page).

{{ small("Selesaikan langkah-langkah berikut untuk menginstal Grafana dari APT repository:") }}

1. {{ small("Install the prerequisite packages") }}
```bash
sudo apt-get install -y apt-transport-https software-properties-common wget
```
2. {{ small("Import the GPG key") }}
```bash
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
```
3. {{ small("Add repository for stable release") }}
```bash
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
4. {{ small("Add repository for beta releases") }}
```bash
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
5. {{ small("Update packages") }}
```bash
sudo apt-get update
```
6. {{ small("Install the latest Grafana OSS release") }}
```bash
sudo apt-get install grafana
```
7. {{ small("Install the latest Grafana Enterprise release") }}
```bash
sudo apt-get install grafana-enterprise
```


## Install Grafana using a deb package
{{small("Jika Anda menginstal Grafana secara manual menggunakan deb package, Anda harus memperbarui Grafana secara manual untuk setiap versi baru.

Selesaikan langkah-langkah berikut untuk menginstal Grafana menggunakan deb package:
")}}

1. Navigasi ke [Grafana download page](https://grafana.com/grafana/download).
2. Pilih versi Grafana yang ingin Anda instal.
    - Versi Grafana terbaru dipilih secara default.
    - Kolom **Versi** hanya menampilkan rilis yang ditandai. Jika Anda ingin menginstal versi Nightly Build, klik Versi **Nightly Build**, lalu pilih versi.
3. Pilih Edisi.
    - **Enterprise**: Ini adalah versi yang direkomendasikan. Secara fungsional, versi ini identik dengan versi sumber terbuka, tetapi mencakup fitur-fitur yang dapat Anda buka dengan lisensi, jika Anda menginginkannya.
    - **Open Source**: Versi ini secara fungsional identik dengan versi Enterprise, tetapi Anda perlu mengunduh versi Enterprise jika menginginkan fitur Enterprise.
4. Tergantung pada sistem yang Anda jalankan, klik tab **Linux** atau **ARM** pada [download page](https://grafana.com/grafana/download).
5. Copy & paster kode dari [download page](https://grafana.com/grafana/download) ke command line Anda dan jalankan.


## Next steps
- [Configure the Grafana servers]({{ link("grafana_config") }})
- [Start the Grafana server]({{ link("grafana_service") }})









<!-- # {Component} {Action}

{Content here...}

## Related {Action}
- [Other Component](prometheus.md)
- [All {Action}s](index.md)

## {Component} Workflow
| Step | Action | Link |
|------|--------|------|
| 1️⃣ | Install | [Install {Component}](../installation/{component}.md) |
| 2️⃣ | Configure | [Configure {Component}](../configuration/{component}.md) |  
| 3️⃣ | Start | [Start {Component}](../start/{component}.md) |

## Navigation
- [← {Action} Hub](index.md)
- [← Setup Overview](../index.md)
- [🏠 Home](../../index.md) -->
