@echo off
REM Script de instalação rápida - Fernanda Doces

echo.
echo ===============================================
echo  INSTALACAO - FERNANDA DOCES
echo ===============================================
echo.

REM Cria ambiente virtual
echo [1/4] Criando ambiente virtual...
python -m venv venv
call venv\Scripts\activate

REM Instala dependências
echo [2/4] Instalando dependências...
pip install -r requirements.txt

REM Migrações
echo [3/4] Executando migrações...
python manage.py migrate

REM Coleta arquivos estáticos
echo [4/4] Coletando arquivos estáticos...
python manage.py collectstatic --noinput

echo.
echo ===============================================
echo  PRONTO PARA INICIAR!
echo ===============================================
echo.
echo Próximos passos:
echo 1. Crie um superusuário:
echo    python manage.py createsuperuser
echo.
echo 2. Inicie o servidor:
echo    python manage.py runserver
echo.
echo 3. Acesse:
echo    http://localhost:8000
echo    http://localhost:8000/admin
echo.
pause
