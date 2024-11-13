from peewee import PostgresqlDatabase, Model

pg_db = PostgresqlDatabase('rasengan', user='postgres', password='postgres',
                           host='localhost', port=5435, options='-c client_encoding=utf8')

class BaseModel (Model):
    class Meta: database = pg_db

try:
    pg_db.connect()
    print("Conexão bem-sucedida ao banco de dados PostgreSQL.")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
