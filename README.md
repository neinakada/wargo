## Neina Akada Maula (2206827592)
## Pemrograman Berbasis Platform E

## Link Adaptable
WarGo: https://wargo.adaptable.app/

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
    ...
                <td><a href="{% url 'main:hapus_product' product.id %}">
            <button>
                Hapus Product
            </button>
        </a></td>
    ...
    ```
