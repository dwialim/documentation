# Configure Grafana
???+ note "**CATATAN**"
    Setelah menambahkan opsi khusus, [hapus komentar](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/#remove-comments-in-the-ini-files) pada bagian yang relevan dari berkas konfigurasi.
    
    Mulai ulang Grafana agar perubahan diterapkan.

Grafana adalah platform open-source untuk monitoring dan observability yang memungkinkan Anda memvisualisasikan metrics, logs, dan traces dari berbagai sumber data.


### Configuration file location
> Pengaturan default untuk instans Grafana disimpan dalam berkas `<WORKING DIRECTORY>/conf/defaults.ini`. Jangan ubah berkas ini.
>
> Tergantung pada OS Anda, berkas konfigurasi kustom Anda dapat berupa berkas `<WORKING DIRECTORY>/conf/custom.ini` atau berkas `/usr/local/etc/grafana/grafana.ini`. Anda dapat menggunakan jalur konfigurasi kustom dengan opsi `--config`.

#### Linux
> Jika Anda menginstal Grafana menggunakan paket deb atau RPM, maka berkas konfigurasi Anda terletak di `/etc/grafana/grafana.ini` dan `custom.ini` terpisah tidak digunakan. Jalur ini ditentukan dalam skrip Grafana init.d menggunakan opsi `--config`.

#### Docker
> Lihat [Konfigurasi image Docker Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/) untuk informasi tentang variabel lingkungan, penyimpanan persisten, dan pembuatan image Docker kustom.

#### Grafana Cloud
> Tidak ada berkas konfigurasi lokal untuk Grafana Cloud stacks, tetapi banyak dari pengaturan ini masih dapat dikonfigurasi. Untuk mengedit pengaturan yang dapat dikonfigurasi, buka tiket dukungan.

### Remove comments in the .ini files
Grafana menggunakan titik koma (;) untuk memberi komentar pada baris dalam INI file. Untuk menghapus komentar pada suatu baris, hapus titik koma (;) dari awal baris tersebut.

Grafana mengabaikan semua baris konfigurasi yang dimulai dengan titik koma.

Misalnya:
```bash title="ini"
;http_port = 3000
```

### Configuration options
#### `[server]`
##### `http_addr`
> Host tempat server mendengarkan. Jika mesin Anda memiliki lebih dari satu network interface, Anda dapat menggunakan pengaturan ini untuk mengekspos layanan Grafana hanya pada satu network interface dan tidak menyediakannya pada interface lain, seperti loopback interface. Nilai kosong setara dengan menetapkan nilai ke 0.0.0.0, yang berarti layanan Grafana terikat ke semua interface.
>
>Di environments yang menggunakan network address translation (NAT), pastikan Anda menggunakan alamat network interface dan bukan final public address; jika tidak, Anda mungkin melihat kesalahan seperti bind: cannot assign requested address in the logs.


## Next steps
- [Start the Grafana server]({{ link("grafana_service") }})
