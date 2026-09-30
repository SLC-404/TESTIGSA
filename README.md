# Tareas (Windows)

## 1. Instalar

```cmd
git clone https://github.com/TU_USUARIO/examenigsa.git
cd examenigsa
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## 2. Configurar

```cmd
copy .env.example .env
```

En `.env` poner el servidor y la base:

```
DB_HOST=localhost\SQLEXPRESS
DB_DATABASE=tareas
```

## 3. Base de datos

En SQL Server:

```sql
CREATE DATABASE tareas;
```

Luego:

```cmd
flask db upgrade
```

## 4. Ejecutar

```cmd
flask run
```

Abrir http://127.0.0.1:5000

