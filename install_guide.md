# Descargar el repositorio

´´´bash
git clone https://github.com/otelo2/BCDSaliva.git
´´´

# Configurar ambiente virtual de python (virtual environment)

´´´python
python3 -m venv venv
´´´

Una vez creado el virtual environment, se debe activar desde la terminal para poder usarlo.
Como alternativa, se puede usar VSCode, que automaticamente detectará el virtual environment y puedes usarlo al abrir una nueva terminal en VScode.

## Verificar que se está usando el venv

|            | Sin Virtual Environment                             | Con Virtual Environment                                    |
|------------|-----------------------------------------------------|------------------------------------------------------------|
| Interprete | Python 3.10.0 64-bit                                | Python 3.10.0 64-bit ('venv': venv)                        |
| Terminal   | D:\Documentos\Otoño 2021\Servicio Social\BCDSaliva> | (venv) D:\Documentos\Otoño 2021\Servicio Social\BCDSaliva> |

# Instalar requirements.txt

´´´python
pip3 install -r requirements.txt
´´´

# Instalar base de datos

Descargar el instalador de MySQL community desde la página oficial. Link de Windows: https://dev.mysql.com/downloads/installer/

## Configurar MySQLServer

Config type: Development Computer
Connectivity: TCP/IP, Port 3306, X Protocol Port: 33060
Authentication method: Legacy (no es lo ideal, no pude hacerlo funcional con el recomendado)
Accounts and Roles: MySQL Root Password: password (no hay que usar password como contraseña, sólo es ejemplo)

## Crear base de datos

Usando MySQL Shell

´´´bash
\connect root@localhost
\sql create database bcdsaliva;
´´´
<!---
Ahora usando DataGrip

Crear nuevo proyecto > Nombre de proyecto: "BCDSaliva" > Database Explorer > Icono de base de datos con una herramienta
Data Sources > Icono de "+" > MySQL

Host: localhost
Port: 3306
User: root
Password: password (mismo que al configurar MySQLServer)
Database: BCDSaliva
-->

# Aplicar migraciones de bases de datos

´´´python
py manage.py migrate
´´´

# Crear superusuario

´´´python
py manage.py createsuperuser
´´´

# Correr el servidor

´´´python
python3 manage.py runserver
´´´

# Acceder a la página web

Ir al link http://127.0.0.1:8000/ en cualquier navegador