<!-- install virtual environment -->
pip install virutalenv

<!-- activte virtual environment -->
env\Scripts\activate(cmd)
.\env\Scripts\activate(powershell)
source .env\bin\activate

<!-- install django -->
pip install django

<!-- create project -->
<!-- django-admin startproject <project_name> . -->
django-admin startproject project .

<!-- create app -->
<!-- python manage.py <app__name> -->
python manage.py startapp todo

<!-- run django -->
python manage.py runserver