@echo off

rem Activate Virtual Env
call interview_app_env\Scripts\activate.bat

rem Run App
set FLASK_APP=jcrm_lite
set FLASK_ENV=development
flask run
