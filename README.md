# Neina Akada Maula (2206827592)
# Pemrograman Berbasis Platform E
# Tugas 2

## Link Adaptable
WarGo: https://wargo.adaptable.app/

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- [x] **Membuat sebuah proyek Django baru.**
    - Membuat *virtual environment* dengan mengetikkan ```python -m venv env``` pada shell atau command prompt.
    - Mengaktifkan *virtual environment* dengan mengetikkan ```env\Scripts\activate```
    - Menambahkan file requirements.txt pada direktori yang sama 
    - Menambahkan dependencies yang dibutuhkan
    - Menjalankan perintah `pip install -r requirements.txt` untuk menginstall dependencies
    - Menjalankan perintah `django-admin startproject wargo` untuk memulai project
    - Menambahkan `"*"` pada bagian ALLOWED_HOSTS pada file `settings.py`
    ```
    ...
    ALLOWED_HOSTS = []
    ...
    ```
    - Menambahkan file `.gitignore` untuk menentukan file dan directory yang harus di*ignore* oleh Git

- [x] **Membuat aplikasi dengan nama `main` pada proyek tersebut**
    - Mengetikkan perintah `manage.py startapp main`
    - Membuat folder `templates` pada directory `main`
    - Menambahkan file `main.html` pada directory yang sama yang berfungsi sebagai *interface* aplikasi

- [x] **Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`**
    - Menambahkan `path('main/', include('main.urls'))` pada `urls.py`

- [x] **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut**
    - `name` dengan tipe Charfield
    - `amount` dengan tipe IntegerField
    - `description` dengan tipe TextField
    Menambahkan ketiga atribut pada `models.py`

- [x] **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
    - Menambahkan fungsi `show_main` yang berisi nama aplikasi, nama mahasiswa, dan kelas yang kemudian direturn ke `html`

- [x] **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**
    - Melakukan deployment dengan memilih Python App Temolate dan PostgreSQL
    - Memilih versi Python yang sesuai dengan yang ada pada perangkat
    - Memasukkan perintah `python manage.py migrate && gunicorn shopping_list.wsgi` pada bagian Start Command
    - Mendeploy aplikasi

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
<img src='/assets/bagan.png'>

### Jelaskan mengapa kita menggunakan ***virtual environment?*** Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
Virtual environment berguna untuk mengisolasi environment update Python kita dari *environment system* yang ada. Hal ini memungkinkan instalasi paket dan modul yang diperlukan tanpa mengganggu sistem. Selain itu, virtual environment juga mempermudah kita untuk membagikan aplikasi maupun menduplikatnya. Meskipun mungkin memungkinkan untuk mengembangkan aplikasi web Django tanpa virtual environment, hal ini tidak dianjurkan karena Django memerlukan banyak paket dan modul yang dapat menyebabkan konflik atau masalah kompatibilitas jika diinstal langsung pada sistem. Selain itu, tanpa *virtual environment*, memindahkan atau menggandakan aplikasi menjadi lebih sulit karena harus menginstal ulang semua *dependencies* secara manual. Oleh karena itu, menggunakan *virtual environment* adalah pendekatan yang lebih baik untuk mengembangkan aplikasi.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- **Model-View-Controller (MVC):**
    - **Model:** Menyimpan data dan logika dalam aplikasi.
    - **View:** Menghandle tampilan grafis dengan menampilkan data dari model.
    - **Controller:** Mengatur alur aplikasi dengan menyalurkan input pada View untuk diolah dengan Model.

- **Model-View-Template (MVT):**
    - **Model:** Menyimpan data dan logika dalam aplikasi.
    - **View:** Interface aplikasi.
    - **Template:** Menggambarkan cara menampilkan data pada View dari Model. 

- **Model-View-ViewModel (MVVM):**
    - **Model:** Menyimpan data dan logika dalam aplikasi.
    - **View:** Interface aplikasi.
    - **ViewModel:** Memperantarai Model dan View dengan memformat data yang diambil dari Model untuk mempermudah penggunaan oleh View..

**Perbedaan:**
Perbedaan antara MVC, MVT, dan MVVM secara umum adalah cara mereka menghubungkan data dengan tampilan. MVC menggunakan Controller untuk menghubungkan data dengan tampilan secara manual. Sedangkan MVT menggunakan View untuk menghubungkan data dengan tampilan secara otomatis. Sementara MVVM menggunakan ViewModel untuk menghubungkan data dengan tampilan secara deklaratif