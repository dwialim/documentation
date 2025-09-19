# Buat dashboard pertama Anda
{{ small("Topik ini membantu Anda memulai Grafana dan membangun dashboard pertama Anda menggunakan sumber data bawaan Grafana. Untuk mempelajari lebih lanjut tentang Grafana, silakan lihat [Pengantar Grafana](https://grafana.com/docs/grafana/latest/introduction/).") }}

!!! info "**CATATAN**"
    Grafana juga menawarkan [akun gratis dengan Grafana Cloud](https://grafana.com/signup/cloud/connect-account?pg=gsdocs) untuk membantu Anda memulai dengan lebih mudah dan cepat. Anda dapat menginstal Grafana untuk hosting mandiri atau mendapatkan akun Grafana Cloud gratis


### Install Grafana

{{ small("Grafana dapat diinstal di berbagai sistem operasi. Untuk daftar persyaratan perangkat keras dan perangkat lunak minimum, serta petunjuk penginstalan Grafana, silakan lihat bagian [Install Grafana]({{ link('grafana_install') }}).") }}

#### Sign in to Grafana
{{ small("Untuk masuk ke Grafana untuk pertama kalinya:") }}

1. {{ small("Buka web browser Anda dan kunjungi http://localhost:3000/.") }}<br>
{{ small("Port HTTP default yang digunakan Grafana adalah `3000`, kecuali Anda telah mengonfigurasi port yang berbeda.") }}

2. {{ small("Pada halaman masuk, masukkan `admin` untuk username dan password.") }}
3. {{ small("Klik **Sign in**.") }}<br>
{{ small("Jika berhasil, Anda akan melihat permintaan untuk mengubah password.") }}

!!! info "**CATATAN**"
    Kami sangat menyarankan Anda mengubah password administrator default.

#### Create a dashboard
{{ small("Jika Anda sudah menyiapkan sumber data yang Anda ketahui cara melakukan kuerinya, lihat [Create dashboard](#).

Untuk membuat dashboard pertama Anda menggunakan sumber data bawaan `-- Grafana --`:") }}

1. {{ small("Klik **Dashboard** di menu utama") }}
2. {{ small("Pada halaman **Dashboard**, klik **New** dan pilih **New Dashboard** dari drop-down menu.") }}
3. {{ small("Pada Dashboard, klik **+ Add visualization**.") }}</br>
![Image title](https://grafana.com/media/docs/grafana/dashboards/empty-dashboard-10.2.png){ loading="lazy" }
4. {{ small("Pada kotak dialog yang terbuka, klik `-- Grafana --`:") }}
![Image title](https://grafana.com/media/docs/grafana/dashboards/screenshot-data-source-selector-10.0.png?w=900){ loading=lazy }
{{ small("Ini mengonfigurasikan [query](https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/#add-a-query) Anda dan menghasilkan Random Walk dashboard.") }}
5. {{ small("Klik **Refresh** untuk query data source.") }}
6. {{ small("Setelah selesai mengedit panel, klik **Save dashboard**.") }}</br>
{{ small("Atau, klik **Back to dashboard** jika Anda ingin melihat perubahan diterapkan ke dashboard terlebih dahulu. Kemudian, klik **Save dashboard** jika sudah siap.") }}
7. {{ small("Tambahkan judul deskriptif untuk dashboard, atau minta Grafana membuatnya menggunakan fitur [generatif AI](#), lalu klik **Save**.") }}
8. {{ small("Klik **Back to dashboard** dan kemudian **Exit edit**.") }}

{{ small("Selamat, Anda telah membuat dashboard pertama Anda dan menampilkan hasilnya.") }}
