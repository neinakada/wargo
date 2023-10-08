## Neina Akada Maula (2206827592)
## Pemrograman Berbasis Platform E

## Link Aplikasi
WarGo: https://neina-akada-tugas.pbp.cs.ui.ac.id/

## TUGAS 2
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

- [x] **Menjawab pertanyaan**
    - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    <img src='/assets/bagan.png'>

    - Jelaskan mengapa kita menggunakan ***virtual environment?*** Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    Virtual environment berguna untuk mengisolasi environment update Python kita dari *environment system* yang ada. Hal ini memungkinkan instalasi paket dan modul yang diperlukan tanpa mengganggu sistem. Selain itu, virtual environment juga mempermudah kita untuk membagikan aplikasi maupun menduplikatnya. Meskipun mungkin memungkinkan untuk mengembangkan aplikasi web Django tanpa virtual environment, hal ini tidak dianjurkan karena Django memerlukan banyak paket dan modul yang dapat menyebabkan konflik atau masalah kompatibilitas jika diinstal langsung pada sistem. Selain itu, tanpa *virtual environment*, memindahkan atau menduplikat aplikasi menjadi lebih sulit karena harus menginstall ulang semua *dependencies* secara manual. Oleh karena itu, menggunakan *virtual environment* adalah pendekatan yang lebih baik untuk mengembangkan aplikasi.

    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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
            - **ViewModel:** Memperantarai Model dan View dengan memformat data yang diambil dari Model untuk mempermudah penggunaan oleh View.

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
    
- [x] **Menjawab pertanyaan**
    - Apa perbedaan antara form POST dan form GET dalam Django?
        - **POST** berguna untuk mengirimkan data secara langsung tanpa menampilkan datanya pada URL. POST cocok untuk digunakan dalam pengiriman data yang bersifat sensitif atau rahasia seperti password. POST tidak memiliki limit dalam pengiriman data sehingga cocok dalam pengiriman data yang kompleks ataupun besar.
        - **GET** digunakan untuk mengambil data dari server yang dikirim sebagai parameter kemudian data ditampilkan pada URL. Dari segi keamanan, POST lebih unggul dibandingkan GET. Selain itu, GET memiliki limit kapasitas data yang relatif kecil.

    - Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
        - **XML** berguna untuk menyimpan dan mengelola data dengan strukur yang kuat dan bersifat hierarkis. XML memiliki syntax yang ketat ditandai dengan aturan pembukaan dan penutupan tag. Dari segi keamanan, XML memiliki mekanisme bawaan seperti DTD dan XML untuk melindungi data.
        - **JSON** digunakan untuk pertukaran data antar aplikasi dengan format yang sederhana dan mudah dimengerti manusia. JSON umumnya digunakan untuk pertukaran data antara user dan server dalam web development dan JavaScript based applications. Format syntax JSON lebih sederhana dibandingkan XML.
        - **HTML** berguna untuk merancang suatu webpage termasuk mengatur konten yang ada di dalamnya dan menampilkannya pada browser. HTML digunakan untuk mengatur konten seperti text, gambar, link, dan sebagainya. Karena tidak dirancang untuk pengiriman data terstuktur, keamanan dari HTML tergantung pada implementasi aplikasi. 

    - Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
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

- [x] **Menambahkan pesan "Kamu menyimpan X item pada aplikasi ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data.**
    - Menambahkan `'jumlah_product': products.count()` pada `views.py` yang berguna untuk menghitung berapa banyak product yang ditambahkan pada aplikasi
    - Mengedit file `main.html` dengan menambahkan tulisan `"Kamu menyimpan {{ jumlah_product }} item pada aplikasi ini"`
    - Jumlah product akan otomatis terupdate setiap ada product baru yang ditambahkan

## TUGAS 4
 - [x] **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
Mengimport `redirect`, `UserCreationForm`, dan `messages` pada `views.py`
    ```
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```
    **a.  Register**
    - Membuat fungsi `register` pada `views.py` menggunakan `UserCreationForm` yang menerima parameter `request`
        ```
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
        ```
    - Membuat file `register.html` pada folder `templates`
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            
            <h1>Register</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}
        ```
    - Mengimport fungsi dengan menambahkan `from main.views import register` pada `urls.py` yang ada di subdirektori `main`
    - Menambahkan `path('register/', register, name='register'),` ke `urlpatterns` agar fungsi dapat diakses

    **b. Login**
    - Mengimport `authenticate` dan `login` dengan menambahkan `from django.contrib.auth import authenticate, login` pada `views.py`
    - Membuat fungsi `login` pada `views.py` untuk mengautentikasi akun pengguna
    ```
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```
    - Membuat file `login.html` pada folder `templates` 
    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %}
    ```
    - Mengimport fungsi dengan menambahkan `from main.views import login_user` pada `urls.py` yang ada di subdirektori `main`
    - Menambahkan `path('login/', login_user, name='login'),` ke `urlpatterns` agar fungsi dapat diakses

    **c. Logout**
    - Mengimport `logout` dengan menambahkan `from django.contrib.auth import logout` pada `views.py`
    - Membuat fungsi `logout` pada `views.py`
    ```
    def logout_user(request):
    logout(request)
    return redirect('main:login')
    ```
    - Menambahkan kode berikut pada `main.html` untuk membuat button logout
    ```
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
    - Mengimport fungsi dengan menambahkan `from main.views import logout_user` pada `urls.py` yang ada di subdirektori `main`
    - Menambahkan `path('logout/', login_user, name='logout'),` ke `urlpatterns` agar fungsi dapat diakses


 - [x] **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**
    - akada
    ![image](https://github.com/neinakada/wargo/assets/119840206/9c4ee661-b46a-4419-9401-aebfabb574da)

    - neina
    ![image](https://github.com/neinakada/wargo/assets/119840206/e08dbd19-10e3-405d-82db-64ba7b95fd8c)



 - [x] **Menghubungkan model Item dengan User.**
    - Menambahkan kode `from django.contrib.auth.models import User` pada `models.py` yang ada di subdirektori `main`
    - Menambahkan kode dibawah untuk menghubungkan produk dengan user melalui sebuah _relationship_
    ```
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
    ```
    - Mengubah fungsi `create_product` menjadi seperti dibawah untuk mencegah Django menyimpan langsung objek ke database dari form
    ```
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```
    - Mengubah fungsi `show_main` untuk menampilkan objek `Product` yang telah dihubungkan dengan logged in user dan menampilkan nama sesuai dengan username yang diinput saat login
    ```
    def show_main(request):
        products = Product.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
        ...
        }
    ...
    ```
    - Migrasi model dengan menulis `python manage.py makemigrations` pada terminal
    - Mengetik `1` untuk menetapkan _default value_ untuk _field user_ pada semua baris di database
    - Mengetik `1` untuk memberikan ID 1 pada user pertama yang telah terdaftare
    - Mengaplikasikan migrasi dengan mengetikkan `python manage.py migrate` pada terminal


 - [x] **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**
    - Mengimport `HttpResponseRedirect`, `reverse`, dan `datetime`
    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
    - Menambahkan fungsi `last_login` pada fungsi `login_user` agar dapat melihat last login user dengan mengganti kode menjadi seperti dibawah
    ```
    ...
    if user is not None:
        login(request, user) # untuk login
        response = HttpResponseRedirect(reverse("main:show_main")) # untuk membuat response
        response.set_cookie('last_login', str(datetime.datetime.now())) # untuk membuat cookie dan memasukannya ke response
        return response
    ...
    ```
    - Menambahkan `'last_login': request.COOKIES['last_login'],` pada fungsi `show.main` untuk menambahkan informasi cookie last_login yang akan ditampilkan pada web
    - Mengubah fungsi `logout_user` untuk menghapus cookie last_login ketika user logout
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
    - Menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada `main.html` untuk menampilkan data last login


 - [x] **Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).**

    - **Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
    UserCreationForm adalah sebuah form yang disediakan oleh Django untuk membuat pengguna baru yang dapat menggunakan aplikasi web. Form ini memiliki tiga bidang meliputi username, password1, dan password2. 
    **Kelebihan** dari UserCreationForm adalah kemudahan penggunaannya, keamanannya yang terjamin dari serangan seperti _cross-site scripting_ atau *SQL injection*. Selain itu, UserCreationForm mendukung prinsip KISS dan DRY sehingga kode yang digunakan harus simple, singkat, dan tidak lebih dari 40-50 line.
    **Kekurangan** dari UserCreationForm adalah tidak adanya bidang email sehingga kita tidak dapat mengirim *verification email* kepada pengguna untuk verifikasi akun saat pendaftaran.

    - **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
    **Autentikasi** berguna unutuk memastikan bahwa hanya pengguna sah yang dapat mengakses aplikasi untuk melindungi data dan informasi dari askes yang tidak sah.
    **Otorisasi** berguna untuk mengontrol akses pengguna ke bagian-bagian khusus dari aplikasi web untuk memastikan bahwa pengguna hanya dapat melakukan aksi tertentu sesuai dengan peran yang diberikan.
    Autentikasi dan otorisasi adalah dua konsep yang berbeda namun melengkapi satu sama lain.

    - **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
    Dalam konteks aplikasi web, cookies adalah file teks kecil yang disimpan di sisi client seperti pada browser saat mengunjungi suatu web. Cookies berguna untuk menyimpan informasi tentang pengguna dan interaksi mereka dengan web tersebut. Django menggunakan cookies untuk mengelola data sesi pengguna.
    Framework sesi Django memungkinkan kita menyimpan dan mengambil data apapun berdasarkan pengunjung situs. Data sesi disimpan di server dan terisolasi dari proses pengiriman dan penerimaan cookies. Cookies hanya berisi ID sesi, tidak termasuk data sesi itu sendiri (kecuali jika kita menggunakan backend berbasis cookie).

    - **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
    Penggunaan cookies dalam pengembangan web secara umum tidak dianggap sebagai ancaman terhadap privasi dan keamanan situs web. Cookies tidak menyimpan informasi pribadi, kecuali dalam beberapa situasi tertentu, seperti nomor kartu kredit dan alamat IP. Namun, cookies tidak memiliki potensi untuk mengirimkan malware atau virus.

    Tetapi, memang ada beberapa risiko ancaman yang perlu diwaspadai meliputi:
        - **Masalah privasi** karena cookies dapat disalahgunakan untuk melacak perilaku user dan mengumpulkan informasi pribadi
        - **_Cross-Site Request Forgery_** dimana penyerang memaksa _authenticated user_ untuk melakukan sebuah aksi di suatu situs web.
        - **_Cross-Site Scripting_** dimana penyerang menyisipkan script berbahaya ke dalam web yang dilihat oleh user lain.


- [x] **[BONUS] Tambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.**
    - Menambahkan function `kurang_amount` dan `tambah_amount` pada `views.py`
        ```
        ...
        def tambah_amount(request, id):
            product = Product.objects.get(id=id)
            product.amount += 1
            product.save()
            response = HttpResponseRedirect(reverse("main:show_main"))
            return response

        def kurang_amount(request,id):
            product = Product.objects.get(id=id)
            
            if (product.amount != 0):
                product.amount -= 1
                product.save()
            response = HttpResponseRedirect(reverse("main:show_main"))
            return response
        ...
        ```
    - Mengimport function pada `urls.py` yang ada di subdirektori `main`
        ```
        from main.views import kurang_amount, tambah_amount
        ```
    - Menambahkan path url ketiga function pada `urlpatterns` di `urls.py`  
        ```
        path('tambah_amount/<int:id>', tambah_amount, name='tambah_amount'),
        path('kurang_amount/<int:id>', kurang_amount, name='kurang_amount'),
        ```
    - Menambahkan button pada `main.html`
        ```
        ...
            <td><a href="{% url 'main:tambah_amount' product.id %}">
                <button>
                    + Product
                </button>
            </a></td>

            <td><a href="{% url 'main:kurang_amount' product.id %}">
                <button>
                    - Product
                </button>
            </a></td>
        ...
        ```
    
- [x] **[BONUS] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.**
    - Menambahkan function `hapus_product` pada `views.py`
        ```
        def hapus_product(request, id):
        Product.objects.filter(pk=id).delete()
        response = HttpResponseRedirect(reverse("main:show_main"))
        return response
        ```
    - Mengimport function `hapus_product`
        ```
        from main.views import hapus_product
        ```
    - Menambahkan path URL pada `urlpatterns` di `urls.py`
        ```
        path('hapus_product/<int:id>', hapus_product, name='hapus_product'),
        ```
    - Menambahkan button Hapus Product pada `main.html`
        ```
            <td><a href="{% url 'main:hapus_product' product.id %}">
                <button>
                    Hapus Product
                </button>
            </a></td>
        ```

## TUGAS 5

 - [x] **Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.**
    - Mengatur alignment text agar berposisi di tengah dengan menambahkan `text-align: center`
    - Mengatur font agar menjadi poppins dengan menambahkan `font-family: poppins`
    - Menambahkan `margin: 0 auto` untuk mengatur elemen ke tengah horizontal
    - Mengubah font yang dibutuhkan untuk menjadi bold dengan menambahkan `font-weight: bold`
    - Mengatur warna background dari element dengan menambahkan kode `background-color <hexcode warna>`

 - [x] **Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.**
    - Mengatur alignment text dengan menambahkan `text-align: <posisi>`
    - Mengatur font agar menjadi poppins dengan menambahkan `font-family: poppins`
    - Menambahkan navigation bar
    - Mengubah font yang dibutuhkan untuk menjadi bold dengan menambahkan `font-weight: bold`
    - Mengatur warna background dari element dengan menambahkan kode `background-color <hexcode warna>`
 
 - [x] **Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).**

    - **Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**
    CSS selectors terbagi menjadi lima kategori meliputi
        - Simple selectors: Men*select* element berdasarkan nama, id, atau class
        - Combinator selectors: Men*select* elements berdasarkan *specific relationship* diantaranya
        - Pseudo-class selectors: Men*select* elements berdasarkan *state* tertentu
        - Pseudo-elements selectors: Men*select* and menata elements
        - Attribute selectors: Men*select* elements berdasarkan attribute atau value dari attributenya


    - **Jelaskan HTML5 Tag yang kamu ketahui.**
        - !DOCTYPE: Menentukan jenis dokumen HTML
        - html: Menandai awal dan akhir dari dokumen HTML
        - head: Menyediakan informasi tentang dokumen HTML
        - title: Menentukan judul untuk dokumen HTML
        - body: Menandai awal dan akhir dari isi dokumen HTML
        - h1 - h6: Menandai judul dari dokumen HTML dengan ukuran yang berbeda-beda
        - p: Menandai paragraf dalam dokumen HTML
        - a: Membuat hyperlink ke page lain atau email address
        - img: Menampilkan gambar dalam dokumen HTML
        - button: Menandai tombol yang dapat diklik
        - div: Menandai sebuah section

    - **Jelaskan perbedaan antara margin dan padding.**
        **Margin**
        - Margin merupakan ruang di luar batas elemen
        - Margin berguna untuk mengatur jarak antar elemen
        - Margin memisahkan blok dari blok yang berdekatan
        - Margin tidak meliputi background dan background color

        **Padding**
        - Padding adalah ruang di dalam batas 
        - Padding berguna untuk menambah ruang internal sebuah elemen
        - Padding memisahkan konten dari batas
        - Padding meliputi gambar  dan warna background yang diterapkan di sekitar content

    - **Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
    **Tailwind** merupakan kerangka kerja CSS yang lebih berfokus pada penggunaan utility yang menyediakan pre-designed widgets yang dapat membantu developers untuk membuat situs dari awal. Tailwind ditulis menggunakan bahasa pemrograman PostCSS dan CSS.
    **Bootstrap** merupakan sebuah kerangka kerja yang berguna unutuk mengembangkan suatu web berdasarkan framework CSS. Bootstrap menyediakan template interface seperti navigation, typography, buttons, dan forms. Bootstrap dirancang menggunakan bahasa pemrograman JavaScript dan HTML.

- [x] **[BONUS] Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.**

    Menambahkan kode dibawah pada bagian `<style>` di file `main.html`
    ```
    table tr:last-child {
        background-color: rgba(63, 204, 212, 0.312); //line untuk mengubah background color yang berbeda
        color: #000000;
        border: 2px solid rgb(255, 255, 255);
    }
    ```

## TUGAS 6

- [x] **Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX**
    - [x] **AJAX GET**
        - [x] **Ubahlah kode tabel data item agar dapat mendukung AJAX GET.**
            - Menghapus kode tabel yang telah ada sebelumnya
            - Menambahkan kode pada `main.html` 
                ```
                <table class="center-table" id="product_table"></table>` pada `main.html`
                ```

        - [x] **Lakukan pengambilan task menggunakan AJAX GET.**
            - Membuat fungsi `get_product_json` pada `views.py`
                ```
                def get_product_json(request):
                    product_item = Product.objects.all()
                    return HttpResponse(serializers.serialize('json', product_item))
                ```
                - Melakukan routing terhadap fungsi `get_product_json` dengan menambahkan kode `from main.views import get_product_json` dan menambahkan path url `path('get-product/', get_product_json, name='get_product_json'),` pada `urls.py`di subdirektori `main`
                - Menambahkan kode dibawah pada bagian `<script>` di `main.html`
                ```
                async function getProducts() {
                    return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
                }
                ```


    - [x] **AJAX POST**
        - [x] **Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.**
            - Membuat modal dengan menambahkan kode dibawah pada `main.html`
                ```
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form id="form" onsubmit="return false;">
                                    {% csrf_token %}
                                    <div class="mb-3">
                                        <label for="name" class="col-form-label">Name:</label>
                                        <input type="text" class="form-control" id="name" name="name"></input>
                                    </div>
                                    <div class="mb-3">
                                        <label for="amount" class="col-form-label">Amount:</label>
                                        <input type="number" class="form-control" id="amount" name="amount"></textarea>
                                    </div>
                                    <div class="mb-3">
                                        <label for="description" class="col-form-label">Description:</label>
                                        <textarea class="form-control" id="description" name="description"></textarea>
                                    </div>
                                </form>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                            </div>
                        </div>
                    </div>
                </div>
                ```
            - Membuat button untuk mengakses modal dengan menambahkan kode 
                ```
                <button type="button" class="button" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product</button>
                ```
        - [x] **Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.**
            - Mengimport `from django.views.decorators.csrf`
            - Membuat fungsi `add_product_ajax` pada `views.py`
                ```
                @csrf_exempt
                    def add_product_ajax(request):
                        if request.method == 'POST':
                            name = request.POST.get("name")
                            amount = request.POST.get("amount")
                            description = request.POST.get("description")
                            user = request.user

                            new_product = Product(name=name, amount=amount, description=description, user=user)
                            new_product.save()

                            return HttpResponse(b"CREATED", status=201)

                        return HttpResponseNotFound()
                ```
            
        - [x] **Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.**
            - Mengimport fungsi `add_product_ajax` pada `urls.py`
                ```
                from main.views import add_product_ajax
                ```
            - Melakukan routing dengan menambahkan path url
                ```
                path('create-ajax/', add_product_ajax, name='add_product_ajax'),
                ```
        - [x] **Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/**

            Menambahkan fungsi `addProduct` pada `<script>` di `main.html`

                function addProduct() {
                    fetch("{% url 'main:add_product_ajax' %}", {
                        method: "POST",
                        body: new FormData(document.querySelector('#form'))
                    }).then(refreshProducts)

                    document.getElementById("form").reset()
                    return false
                }
        - [x] **Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.**

            Menambahkan fungsi `refreshProducts` pada `<script>` di `main.html`
            ```
            async function refreshProducts() {
                    document.getElementById("product_table").innerHTML = ""
                    const products = await getProducts()
                    let htmlString = `<tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Amount</th>
                        <th>Actions</th>
                    </tr>`
                    
                    products.forEach((item) => {
                        console.log(item)
                        htmlString += `\n<tr>
                        <td>${item.fields.name}</td>
                        <td>${item.fields.description}</td>
                        <td>${item.fields.amount}</td>
                        <td>

                        <a href="edit-product/${item.pk}">
                            <button>
                                Edit
                            </button>
                        </a>

                        <button type="button" class="button" id="button_delete" onClick="deleteProduct(${item.pk})">
                            Delete
                        </button>

                        </td>
                    </tr>`
                    })

                    document.getElementById("product_table").innerHTML = htmlString
                }
                ```

    - [x] **Melakukan perintah collectstatic**
        - Menambahkan kode dibawah pada `settings.py`
            ```
            STATIC_URL = 'static/'
            STATIC_ROOT = os.path.join(BASE_DIR, 'static')
            ```
        - Menjalankan `python 3 manage.py collectstatic`

-[x] **Menjawab pertanyaan**
- **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**

    **Asynchronous Programming**

    - Tugas-tugas dieksekusi secara independen
    - Waktu eksekusi lebih cepat karena tidak perlu menunggu tugas lain selesai sebelum melanjutkan ke tugas berikutnya
    - Memerlukan pemahaman mendalam mengenai konsep callback dan promise
    - Cocok untuk aplikasi web yang memerlukan response time yang cepat dan efisien seperti aplikasi real-time atau streaming
   
    **Synchronous Programming**

    - Tugas-tugas dieksekusi satu persatu secara berurutan
    - Waktu eksekusi lebih lama karena dalam pengerjaan suatu tugas harus menunggu tugas lain selesai dikerjakan
    - Lebih mudah dipahami dan diimplementasikan
    - Cocok digunakan untuk aplikasi yang memerlukan urutan eksekusi yang terstruktur dan jelas seperti mobile app atau desktop app

- **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

    Dalam penerapan JavaScript dan AJAX, paradigma _event-driven programming_ berguna untuk membangun aplikasi web yang responsif dan interaktif yang menggunakan event sebagai pemicu dalam eksekusi kode. Paradigma ini berbeda dengan program yang sifatnya prosedural karena program akan berjalan sesuai dengan events yang di-_trigger_. Pada tugas ini, contoh penerapannya ada pada button yang menjalankan fungsi `addProduct()` dan `deleteProduct(pk)` yang akan dijalankan jika button `Add Product` dan `Delete` di-_click_.
    

- **Jelaskan penerapan asynchronous programming pada AJAX.**

    Asynchronous programming pada AJAX mengacu pada kemampuan AJAX untuk mengirim dan menerima data dari server tanpa perlu melakukan reload halaman keseluruhan. Hal ini cukup penting dalam pengembangan web karena memungkinkan web app untuk berinteraksi dengan server secara dinamis tanpa harus mereaload page yang meningkatkan _response time_ dan _user experience_.

- **Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**

    **Fetch API**
    - Lebih ringan dan cepat, tidak memerlukan library tambahan
    - Lebih mudah dalam penggunaan karena menggunakan Promise
    - Mendukung format JSON dan XML
    - Tidak mensupport fitur _cross-domain request_ pada browser yang lebih lama
    - Tidak mensupport fitur timeout pada browser lama

    **jQuery**
    - Lebih berat karena memerlukan library tambahan
    - Lebih sulit penggunaannya
    - Mendukung format JSON, XML, dan HTML
    - Mensupport fitur _cross-domain request_ pada browser lama
    - Mensupport fitur timeout pada browser lama

    Menurut saya, Fetch API lebih baik karena lebih mudah digunakan karena menggunakan Promise. Selain itu, Fetch API lebih ringan sehingga lebih cepat dibandingkan dengan jQuery.  

- [x] **Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE**
    - Membuat fungsi `delete_product_ajax` pada `views.py`
        ```
        @csrf_exempt
        def delete_product_ajax(request, id):
            product = Product.objects.get(pk=id)
            product.delete()
            response = HttpResponseRedirect(reverse("main:show_main"))
            return response
        ```
    - Mengimport fungsi pada `urls.py` dengan menambahkan `from main.views import delete_product_ajax`
    - Menambahkan path URL dengan menambahkan kode
        ```
        path('delete_product_ajax/<int:id>', delete_product_ajax, name='delete_product_ajax')
        ```
    - Menambahkan button `delete` di `main.html`
        ```
        <button type="button" class="button" id="button_delete" onClick="deleteProduct(${item.pk})">
            Delete
        </button>
        ```
    - Menambahkan kode dibawah pada `<script>` 
        ```
        function deleteProduct(pk) {
            fetch(`/delete_product_ajax/${pk}`, {
                method: 'DELETE',
            }).then(refreshProducts);
        }
         ```