# 2024-Dj-After65Store
Membuat aplikasi ecommece After65Store menggunakan Django versi 5


## 1. SETUP


#### 1. Membuat lingkungan virtual dengan nama venv312502

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        λ REM: Membuat lingkungan virtual dengan nama venv312502

        λ python --version
        Python 3.12.1

        λ pip --version
        pip 24.0 

        λ python -m venv venv312502 --promp After65Store

        modified:   .gitignore
        modified:   README.md


#### 2. Mengaktifkan venv312502

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        λ REM: Mengaktifkan venv312502

        λ venv312502\Scripts\activate.bat

        (After65Store) λ 

        Note: 
        prompt After65Store ada di dalam tanda kurung (After65Store) menandai venv312502 sedang aktif


#### 3. Menginstal Django versi 5.0.2

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Menginstal Django versi 5.0.2

        (After65Store) λ pip install django==5.0.2
        Collecting django==5.0.2
        ...
        Successfully installed asgiref-3.7.2 django-5.0.2 sqlparse-0.4.4 tzdata-2024.1

        [notice] A new release of pip is available: 23.2.1 -> 24.0
        [notice] To update, run: python.exe -m pip install --upgrade pip


#### 4. Memeriksa hasil instalasi

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Memeriksa hasil instalasi

        (After65Store) λ pip list
        Package  Version
        -------- -------
        asgiref  3.7.2
        Django   5.0.2
        pip      23.2.1
        sqlparse 0.4.4
        tzdata   2024.1

        [notice] A new release of pip is available: 23.2.1 -> 24.0
        [notice] To update, run: python.exe -m pip install --upgrade pip


#### 5. Meng-upgrade pip

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-24.0


## 2. DJANGO PROJECT


#### 1. Memeriksa perintah untuk membuat proyek

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Memeriksa perintah untuk membuat proyek

        (After65Store) λ django-admin

        Type 'django-admin help <subcommand>' for help on a specific subcommand.

        Available subcommands:

        [django]
            check
            ...
            dbshell
            ...
            makemigrations
            migrate
            runserver
            sendtestemail
            shell
            ...
            startapp
            startproject <---
            test
            testserver


#### 2. Membuat proyek django dengan nama 'config'

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Membuat proyek django dengan nama 'config'

        (After65Store) λ django-admin startproject config

        (After65Store) λ tree config /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ-AFTER65STORE\CONFIG
        │   manage.py
        │
        └───config
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py

        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py


## 3. DJANGO SERVER


#### 1. Menjalankan django server untuk kali pertama

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Menjalankan django server untuk kali pertama (lihat perintah di atas)

        (After65Store) λ cd config\

        (After65Store) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        March 07, 2024 - 13:36:04
        Django version 5.0.2, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        modified:   README.md


#### 2. Melihat tampilan default django pada browser

        ...
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.



## 4. STRUKTUR PROYEK


#### 1. Mengganti nama folder 'config' terluar menjadi 'root'

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Mengganti nama folder 'config' terluar menjadi 'root'

        (After65Store) λ mv config root

        modified:   README.md
        renamed:    config/config/__init__.py -> root/config/__init__.py
        renamed:    config/config/asgi.py -> root/config/asgi.py
        renamed:    config/config/settings.py -> root/config/settings.py
        renamed:    config/config/urls.py -> root/config/urls.py
        renamed:    config/config/wsgi.py -> root/config/wsgi.py
        renamed:    config/manage.py -> root/manage.py


#### 2. Memindahkan file README.md dan .gitignore ke dalam folder root

        Steps:

        1. Pindahkan file README.md dan .gitignore ke dalam folder root (drag and drop)
        2. Pindahkan folder .git ke dalam root direktori 

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store(main -> origin)
        (After65Store) λ REM: Masuk ke root direktori

        (After65Store) λ ls
        root/  venv312502/

        (After65Store) λ cd root\

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ ls
        config/  db.sqlite3  manage.py*  README.md

        (After65Store) λ tree /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:.
        │   .gitignore
        │   db.sqlite3
        │   manage.py
        │   README.md
        │
        └───config
            │   asgi.py
            │   settings.py
            │   urls.py
            │   wsgi.py
            │   __init__.py
            │
            └───__pycache__
                    settings.cpython-312.pyc
                    urls.cpython-312.pyc
                    wsgi.cpython-312.pyc
                    __init__.cpython-312.pyc

        modified:   README.md
        renamed:    root/config/__init__.py -> config/__init__.py
        renamed:    root/config/asgi.py -> config/asgi.py
        renamed:    root/config/settings.py -> config/settings.py
        renamed:    root/config/urls.py -> config/urls.py
        renamed:    root/config/wsgi.py -> config/wsgi.py
        renamed:    root/manage.py -> manage.py



## 5. DJANGO APP


#### 1. Membuat folder app di dalam folder root

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ REM: Membuat folder app di dalam folder root

        (After65Store) λ mkdir app

        (After65Store) λ ls
        app/  config/  db.sqlite3  manage.py*  README.md

        modified:   README.md


#### 2. Membuat app (aplikasi) django di dalam folder app dengan nama 'shop'

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ REM: Membuat app (aplikasi) django di dalam folder app dengan nama 'shop'

        (After65Store) λ ls
        app/  config/  db.sqlite3  manage.py*  README.md

        (After65Store) λ mkdir app\shop

        (After65Store) λ python manage.py startapp shop app\shop

        (After65Store) λ ls
        app/  config/  db.sqlite3  manage.py*  README.md

        (After65Store) λ tree app /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ-AFTER65STORE\ROOT\APP
        └───shop
            │   admin.py
            │   apps.py
            │   models.py
            │   tests.py
            │   views.py
            │   __init__.py
            │
            └───migrations
                    __init__.py

        modified:   README.md
        new file:   app/shop/__init__.py
        new file:   app/shop/admin.py
        new file:   app/shop/apps.py
        new file:   app/shop/migrations/__init__.py
        new file:   app/shop/models.py
        new file:   app/shop/tests.py
        new file:   app/shop/views.py



## 6. DJANGO TEMPLATES, VIEWS DAN URLs


#### 1. Hallo World dari ulrs dan views

        modified:   README.md
        new file:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   config/urls.py


#### 2. Mengaktifkan template django

        modified:   README.md
        modified:   config/settings.py


#### 3. Membuat laman Home menampilkan Hallo World dari templates, views, urls

        modified:   README.md
        modified:   app/shop/views.py
        new file:   templates/shop/index.html


#### 4. Menampilkan data dari home_view pada home page

        modified:   README.md
        modified:   app/shop/views.py
        modified:   templates/shop/index.html


#### 5. Mengisi html template pada home page

        modified:   README.md
        modified:   templates/shop/index.html


#### 6. STATAC FILE part 1- Membuat STATICFILES_DIRS

        modified:   README.md
        modified:   config/settings.py


#### 7. STATAC FILE part 2- Membuat folder 'static' dan mengisi assets

        modified:   README.md
        new file:   static/assets/css/plugins/animate.css
        new file:   static/assets/css/plugins/images/ui-icons_444444_256x240.png
        ...
        new file:   static/assets/scss/style.scss
        modified:   templates/shop/index.html


#### 8. STATAC FILE part 3- Loading static files

        modified:   README.md
        new file:   static/assets/css/custom.css
        modified:   static/assets/css/style.css
        new file:   static/assets/css/uicons-regular-straight.css
        modified:   templates/shop/index.html


#### 9. Membuat base template dan extends base template pada home page

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/shop/index.html


#### 10. Template inheritance part 1 - Move main pada base template pada home page

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/shop/index.html


#### 12. Template inheritance part 2 - Membuat shared template and use include

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/shared/00_head.html
        new file:   templates/shared/01_top_bar.html
        new file:   templates/shared/02_header.html
        new file:   templates/shared/03_off_canvas_wishlist.html
        new file:   templates/shared/04_off_canvas_cart.html
        new file:   templates/shared/05_off_canvas_mobile_menu.html
        new file:   templates/shared/12_footer.html
        new file:   templates/shared/13_modal_pop_up_search.html
        new file:   templates/shared/14_modal_login_register.html
        new file:   templates/shared/15_modal_image_zoom.html
        new file:   templates/shared/16_scripts.html


#### 13. Template inheritance part 3 - Membuat component template

        modified:   README.md
        modified:   templates/base.html
        renamed:    templates/shared/12_footer.html -> templates/shared/06_footer.html
        renamed:    templates/shared/13_modal_pop_up_search.html -> templates/shared/07_modal_pop_up_search.html
        renamed:    templates/shared/14_modal_login_register.html -> templates/shared/08_modal_login_register.html
        renamed:    templates/shared/15_modal_image_zoom.html -> templates/shared/09_modal_image_zoom.html
        renamed:    templates/shared/16_scripts.html -> templates/shared/10_scripts.html
        new file:   templates/shop/components/01_hero_slider.html
        new file:   templates/shop/components/02_banner_1.html
        new file:   templates/shop/components/03_services.html
        new file:   templates/shop/components/04_product.html
        new file:   templates/shop/components/05_deal_of_the_day.html
        new file:   templates/shop/components/06_testimonial.html
        new file:   templates/shop/components/07_brand.html
        modified:   templates/shop/index.html

        Note:

        Dilakukan perubahan penomoran file pada shared folder


#### 14. Membuat laman product-list

        modified:   README.md
        modified:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   templates/shared/02_header.html
        renamed:    templates/shop/components/01_hero_slider.html -> templates/shop/components/1_home/01_hero_slider.html
        renamed:    templates/shop/components/02_banner_1.html -> templates/shop/components/1_home/02_banner_1.html
        renamed:    templates/shop/components/03_services.html -> templates/shop/components/1_home/03_services.html
        renamed:    templates/shop/components/04_product.html -> templates/shop/components/1_home/04_product.html

        renamed:    templates/shop/components/05_deal_of_the_day.html -> templates/shop/components/1_home/05_deal_of_the_day.html
        renamed:    templates/shop/components/06_testimonial.html -> templates/shop/components/1_home/06_testimonial.html
        renamed:    templates/shop/components/07_brand.html -> templates/shop/components/1_home/07_brand.html
        new file:   templates/shop/components/2_products/01_breadcrumb.html
        new file:   templates/shop/components/2_products/02_shop_top_bar.html
        new file:   templates/shop/components/2_products/03_content.html
        new file:   templates/shop/components/2_products/04_load_more.html
        new file:   templates/shop/components/2_products/05_sidebar.html
        modified:   templates/shop/index.html
        new file:   templates/shop/product_list.html

        NOTE: 

        Rename: from components to components/1_home and move the file to it



## 7. DJANGO APP BLOG


#### 1. Membuat aplikasi blog

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ REM: Membuat aplikasi blog

        (After65Store) λ mkdir app\blog

        (After65Store) λ python manage.py startapp blog app\blog

        (After65Store) λ tree app/blog /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ-AFTER65STORE\ROOT\APP\BLOG
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py

        modified:   README.md
        new file:   app/blog/__init__.py
        new file:   app/blog/admin.py
        new file:   app/blog/apps.py
        new file:   app/blog/migrations/__init__.py
        new file:   app/blog/models.py
        new file:   app/blog/tests.py
        new file:   app/blog/views.py


#### 2. Membuat laman blog

        modified:   README.md
        new file:   app/blog/urls.py
        modified:   app/blog/views.py
        modified:   config/urls.py
        new file:   templates/blog/post_list.html
        modified:   templates/shared/02_header.html


#### 3. Membuat template inheritance pada laman blog

        modified:   app/blog/apps.py
        modified:   app/blog/views.py
        new file:   templates/blog/components/01_breadcrumb.html
        new file:   templates/blog/components/02_post_list.html
        new file:   templates/blog/components/03_pagination.html
        new file:   templates/blog/components/04_sidebar_search.html
        new file:   templates/blog/components/05_sidebar_post_category.html
        new file:   templates/blog/components/06_sidebar_recent_post.html
        new file:   templates/blog/components/07_sidebar_banner.html
        new file:   templates/blog/components/08_sidebar_tags.html
        modified:   templates/blog/post_list.html


#### 4. Membuat template post_details

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py
        modified:   templates/blog/components/02_post_list.html
        new file:   templates/blog/post_details.html



## 8. DJANGO APP PAGE


#### 1. Membuat app page

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ mkdir app\page

        (After65Store) λ python manage.py startapp page app\page

        (After65Store) λ tree app/page /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ-AFTER65STORE\ROOT\APP\page
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py

        modified:   README.md
        new file:   app/page/__init__.py
        new file:   app/page/admin.py
        new file:   app/page/apps.py
        new file:   app/page/migrations/__init__.py
        new file:   app/page/models.py
        new file:   app/page/tests.py
        new file:   app/page/views.py


#### 2. Membuat laman about

        new file:   app/page/urls.py
        modified:   app/page/views.py
        modified:   config/urls.py
        new file:   templates/page/about.html
        modified:   templates/shared/02_header.html


#### 3. Membuat template inheritance pada laman about

        modified:   README.md
        modified:   templates/page/about.html
        new file:   templates/shared/_brand.html
        new file:   templates/shared/_services.html
        new file:   templates/shared/_testimonial.html
        modified:   templates/shop/index.html


#### 4. Membuat laman contact

        modified:   README.md
        modified:   app/page/urls.py
        modified:   app/page/views.py
        modified:   templates/page/about.html
        new file:   templates/page/contact.html
        modified:   templates/shared/02_header.html


#### 5. Merubah nama app page menjadi page

        modified:   README.md
        renamed:    app/page/__init__.py -> app/page/__init__.py
        renamed:    app/page/admin.py -> app/page/admin.py
        renamed:    app/page/apps.py -> app/page/apps.py
        renamed:    app/page/migrations/__init__.py -> app/page/migrations/__init__.py
        renamed:    app/page/models.py -> app/page/models.py
        renamed:    app/page/tests.py -> app/page/tests.py
        renamed:    app/page/urls.py -> app/page/urls.py
        renamed:    app/page/views.py -> app/page/views.py
        modified:   config/urls.py
        renamed:    templates/page/about.html -> templates/page/about.html
        renamed:    templates/page/contact.html -> templates/page/contact.html
        modified:   templates/shared/02_header.html


#### 6. Membuat laman wishlish

        modified:   README.md
        modified:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   templates/shared/03_off_canvas_wishlist.html
        new file:   templates/shop/wishlist.html


#### 7. Membuat laman cart

        modified:   README.md
        modified:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   templates/shared/04_off_canvas_cart.html
        new file:   templates/shop/cart.html


#### 8. Membuat laman checkout

        modified:   README.md
        modified:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   templates/shared/04_off_canvas_cart.html
        new file:   templates/shop/checkout.html


#### 9. House keeping - Merubah kata 'setting' menjadi 'page'

        modified:   README.md

        NOTE:

        1. Perubahan nama dilakukan karena nama app 'setting'
           telah dirubah namanya menjadi 'page'



## 8. DJANGO APP ACCOUNT


#### 1. Membuat account app

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ REM: Membuat account app

        (After65Store) λ mkdir app\account

        (After65Store) λ python manage.py startapp account app\account

        (After65Store) λ tree app/account /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ-AFTER65STORE\ROOT\APP\ACCOUNT
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py

        modified:   README.md
        new file:   app/account/__init__.py
        new file:   app/account/admin.py
        new file:   app/account/apps.py
        new file:   app/account/migrations/__init__.py
        new file:   app/account/models.py
        new file:   app/account/tests.py
        new file:   app/account/views.py


#### 2. Membuat laman login/register

        modified:   README.md
        new file:   app/account/urls.py
        modified:   app/account/views.py
        modified:   config/urls.py
        new file:   templates/account/register.html
        modified:   templates/shared/02_header.html



## 9. DJANGO APP SETTING


#### 1. Membuat setting app

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ REM: Membuat setting app

        (After65Store) λ mkdir app\setting

        (After65Store) λ python manage.py startapp setting app\setting

        (After65Store) λ tree app/setting /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ-AFTER65STORE\ROOT\APP\SETTING
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py


        modified:   README.md
        new file:   app/setting/__init__.py
        new file:   app/setting/admin.py
        new file:   app/setting/apps.py
        new file:   app/setting/migrations/__init__.py
        new file:   app/setting/models.py
        new file:   app/setting/tests.py
        new file:   app/setting/views.py


#### 2. Menampilkan data statis

        modified:   README.md
        new file:   app/setting/urls.py
        modified:   app/setting/views.py
        modified:   config/urls.py
        new file:   templates/setting/setting_data_statis.html
        modified:   templates/shared/00_head.html
        modified:   templates/shared/01_top_bar.html
        modified:   templates/shared/05_off_canvas_mobile_menu.html


        NOTE: 

        1. Data tidak berhasil ditampilkan.
        2. Mungkin kalau data sudah ada di dalam db, data bisa ditampilkan.

        (:


#### 3. Remove statis data from head and top_bar

        modified:   README.md
        modified:   templates/shared/00_head.html
        modified:   templates/shared/01_top_bar.html



## 10. DATABASE


#### 1. Remove statis data from head and top_bar

        mysql> CREATE DATABASE 2024_dj_after65_store;
        Query OK, 1 row affected (0.15 sec)

        mysql> SHOW DATABASES;
        +-------------------------------------------+
        | Database                                  |
        +-------------------------------------------+
        | 2024_dj_after65_store                     |
        | ...
        | sakila                                    |
        | sys                                       |
        | test_db                                   |
        +-------------------------------------------+
        42 rows in set (0.14 sec)


#### 2. Konek db dengan proyek

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-Dj-After65Store\root(main -> origin)
        (After65Store) λ pip install mysqlclient
        ...
        Successfully installed mysqlclient-2.2.4

        # MySQL db
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '2024_dj_after65_store',
            'USER': 'root',
            'PASSWORD': '',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }

        (After65Store) λ python manage.py check
        System check identified no issues (0 silenced).


#### 3. Mengamankan sensitif file

        Steps 1: instal django-environ
        (bisaapa) λ python -m pip install django-environ

        Steps 2: create .env .env-example
        (bisaapa) λ touch .env .env-example

        Steps 3: set up .env file
        DEBUG=True
        SECRET_KEY=django-insecure-httc#cur2tsn2qq*zhu$%d+*gtm21u4l=$p(_$!5+8ukcgo&k2
        DATABASE_NAME=2024_dj5_kamubisaapa
        DATABASE_USER=root
        DATABASE_PASSWORD=
        DATABASE_HOST=localhost
        DATABASE_PORT=3306

        # Step 4: setup config/settings.py
        # 1. import environ dan os
        import environ
        import os

        # 1. Create environ
        env = environ.Env(
            # set casting, default value
            DEBUG=(bool, False)
        )

        # 2. Set the project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 3. Take environment variables from .env file
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

        # 4. False if not in os.environ because of casting above
        DEBUG = env('DEBUG')

        # 5. Raises Django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
        SECRET_KEY = env('SECRET_KEY')

        # 6. Set db
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.environ.get('DATABASE_NAME'),
                'USER': os.environ.get('DATABASE_USER'),
                'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
                'HOST': os.environ.get('DATABASE_HOST'),
                'PORT': os.environ.get('DATABASE_PORT'),
            }
        }

        Step 5: run python manage.py check
        (bisaapa) λ python manage.py check

        The result:
        System check identified no issues (0 silenced).

        new file:   .env-example
        modified:   README.md
        modified:   config/settings.py