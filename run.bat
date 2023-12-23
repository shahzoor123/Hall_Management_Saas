@echo off

:: Change directory to your project folder on the desktop
cd /d "%USERPROFILE%\Desktop\Panda"

:: Activate the virtual environment (change 'env_name' to your environment name)
call venv\Scripts\activate.bat

:: Start the Django development server
python manage.py runserver

:: Exit the script
exit
