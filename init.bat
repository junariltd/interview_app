@echo off

rem Configure Virtual Env
python -m venv interview_app_env
call interview_app_env\Scripts\activate.bat
pip install -r requirements.txt

rem Init DB
set FLASK_APP=jcrm_lite
set FLASK_ENV=development
flask init-db
