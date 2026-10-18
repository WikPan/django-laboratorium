@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
    if errorlevel 1 goto blad
)
".venv\Scripts\python.exe" -c "import django; assert django.get_version() == '5.2.17'" >nul 2>&1
if errorlevel 1 (
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    if errorlevel 1 goto blad
)
".venv\Scripts\python.exe" manage.py migrate --noinput
if errorlevel 1 goto blad
".venv\Scripts\python.exe" przygotuj_demo.py
if errorlevel 1 goto blad
echo.
echo Otworz w przegladarce: http://127.0.0.1:8000/
echo Konto po pierwszym uruchomieniu: student / Student123!
echo Zatrzymanie serwera: Ctrl+C. Pozostaw to okno otwarte podczas pokazu.
".venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
if errorlevel 1 goto blad
exit /b 0
:blad
echo.
echo Uruchomienie nie powiodlo sie. Sprawdz blad powyzej.
echo Wymagany Python 3.10+; przy pierwszym uruchomieniu takze Internet.
pause
exit /b 1
