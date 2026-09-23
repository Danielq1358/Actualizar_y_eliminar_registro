import os

import pymysql.cursors


class MySQLConnection:
    """Administra una conexion y ejecuta consultas parametrizadas."""

    def __init__(self, db):
        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "1234"),
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                if query.strip().lower().startswith("insert"):
                    return cursor.lastrowid
                return None
        except Exception as error:
            print(f"Error en la consulta: {error}")
            return False
        finally:
            self.connection.close()


def connectToMySQL(db):
    return MySQLConnection(db)
