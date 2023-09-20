## Neina Akada Maula (2206827592)
## Pemrograman Berbasis Platform E

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
Virtual environment berguna untuk mengisolasi environment update Python kita dari *environment system* yang ada. Hal ini memungkinkan instalasi paket dan modul yang diperlukan tanpa mengganggu sistem. Selain itu, virtual environment juga mempermudah kita untuk membagikan aplikasi maupun menduplikatnya. Meskipun mungkin memungkinkan untuk mengembangkan aplikasi web Django tanpa virtual environment, hal ini tidak dianjurkan karena Django memerlukan banyak paket dan modul yang dapat menyebabkan konflik atau masalah kompatibilitas jika diinstal langsung pada sistem. Selain itu, tanpa *virtual environment*, memindahkan atau menduplikat aplikasi menjadi lebih sulit karena harus menginstall ulang semua *dependencies* secara manual. Oleh karena itu, menggunakan *virtual environment* adalah pendekatan yang lebih baik untuk mengembangkan aplikasi.

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

## TUGAS 3
- [x] **Membuat input form untuk menambahkan objek model pada app sebelumnya.**
    - Membuat file `forms.py` di directory `main`
    - Membuat fungsi `create_product` yang menerima parameter request pada `views.py` untuk mengelola input form
    ```
        def create_product(request):
        form = ProductForm(request.POST or None)
        
        if form.is_valid() and request.method == "POST":
            form.save()
                return HttpResponseRedirect(reverse('main:show_main'))
        
        context = {'form': form}
        return render(request, "create_product.html", context)
    ```
    - Jika input valid, data akan disave dengan `form.save` dan user akan dialihkan ke main page

- [x] **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**
    - Membuat file `base.html` sebagai kerangka webpage lalu mengintegrasikannya dengan menambahkan kode `'DIRS': [BASE_DIR / 'templates']` agar terdeteksi sebagai template
    - Mengubah `main.html` pada subdirectory `templates` menjadi
  ```
    {% extends 'base.html' %}

        {% block content %}
        <h1>WarGo</h1>
        
        <h5>Name:</h5>
        <p>{{ nama }}</p>
        
        <h5>Kelas:</h5>
        <p>{{ kelas }}</p>
        {% endblock content %}
  ```
    - Membuat fungsi `show_xml` pada `views.py` untuk mengambil product dan mengembalikannya dalam bentuk XML
    - Membuat fungsi `show_json` pada `views.py` untuk mengambil product dan mengembalikannya dalam bentuk JSON
    - Membuat fungsi `show_xml_by_id` pada `views.py` untuk mengambil product dan mengembalikan data product berdasarkan ID dalam bentuk XML
    - Membuat fungsi `show_xml` pada `views.py` untuk mengambil product dan mengembalikan data product berdasarkan ID dalam bentuk JSON
      
- [x] **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
    - Mengimport fungsi `create_product` dan menambahkan Path URL `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` pada `urlpatterns` di `urls.py` agar fungsi bisa digunakan 
    ```
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json')
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ```
    
## Apa perbedaan antara form POST dan form GET dalam Django?
- POST
berguna untuk mengirimkan data secara langsung tanpa menampilkan datanya pada URL. POST cocok untuk digunakan dalam pengiriman data yang bersifat sensitif atau rahasia seperti password. POST tidak memiliki limit dalam pengiriman data sehingga cocok dalam pengiriman data yang kompleks ataupun besar.

- GET
digunakan untuk mengambil data dari server yang dikirim sebagai parameter kemudian data ditampilkan pada URL. Dari segi keamanan, POST lebih unggul dibandingkan GET. Selain itu, GET memiliki limit kapasitas data yang relatif kecil.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML
berguna untuk menyimpan dan mengelola data dengan strukur yang kuat dan bersifat hierarkis. XML memiliki syntax yang ketat ditandai dengan aturan pembukaan dan penutupan tag. Dari segi keamanan, XML memiliki mekanisme bawaan seperti DTD dan XML untuk melindungi data.

- JSON
digunakan untuk pertukaran data antar aplikasi dengan format yang sederhana dan mudah dimengerti manusia. JSON umumnya digunakan untuk pertukaran data antara user dan server dalam web development dan JavaScript based applications. Format syntax JSON lebih sederhana dibandingkan XML.

- HTML
berguna untuk merancang suatu webpage termasuk mengatur konten yang ada di dalamnya dan menampilkannya pada browser. HTML digunakan untuk mengatur konten seperti text, gambar, link, dan sebagainya. Karena tidak dirancang untuk pengiriman data terstuktur, keamanan dari HTML tergantung pada implementasi aplikasi. 

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON memiliki format yang ringan, lebih kecil dibandingkan XML
- JSON memiliki struktur kode yang sederhana sehingga mudah dibaca oleh manusia
- JSON memiliki kompatibilitas yang tinggi dengan banyak programming language meliputi JavaScript, Python, C++, Ruby, dan sebagainya
- JSON memiliki keamanan yang lebih baik dibandingkan XML karena tidak mendukung eksekusi kode
- JSON mudah untuk dikembangkan dan diintegrasikan pada bahasa pemrograman

- [x] **Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md**
- HTML
  ![image](https://github.com/neinakada/wargo/assets/119840206/75c54c5b-4632-499f-bdef-0cd22753d472)

- XML
![image](https://github.com/neinakada/wargo/assets/119840206/1a44501b-6c4d-4c05-9ab1-f591654a0197)

- JSON
![image](https://github.com/neinakada/wargo/assets/119840206/82ca7371-cd56-4c9f-a77a-0116a25edbb2)

- XML by ID
![image](https://github.com/neinakada/wargo/assets/119840206/1e9282ed-e9d4-4779-97cb-9b499e24d818)

- JSON by ID
![image](https://github.com/neinakada/wargo/assets/119840206/c914c819-8fcd-48be-b628-f366dcfcb459)

- [x] Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data.
      - Menambahkan `'jumlah_product': products.count()` pada `views.py` yang berguna untuk menghitung berapa banyak product yang ditambahkan pada aplikasi
      - Mengedit file `main.html` dengan menambahkan tulisan `"Kamu menyimpan {{ jumlah_product }} item pada aplikasi ini"`
      - Jumlah product akan otomatis terupdate setiap ada product baru yang ditambahkan
