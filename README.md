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

