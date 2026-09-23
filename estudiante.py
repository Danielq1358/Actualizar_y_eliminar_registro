from mysqlconnection import connectToMySQL


class Estudiante:
    """Representa un registro de la tabla estudiantes."""

    def __init__(self, data):
        self.id_estudiante = data["id_estudiante"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.created_at = data.get("created_at")

    @classmethod
    def get_all(cls):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            ORDER BY id_estudiante;
        """
        resultados = connectToMySQL("esquema_estudiantes").query_db(query)
        if resultados is False:
            return []
        return [cls(estudiante) for estudiante in resultados]

    @classmethod
    def get_by_id(cls, id_estudiante):
        query = """
            SELECT id_estudiante, nombre, email, created_at
            FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s;
        """
        data = {"id_estudiante": id_estudiante}
        resultados = connectToMySQL("esquema_estudiantes").query_db(query, data)
        if resultados:
            return cls(resultados[0])
        return None

    @classmethod
    def actualizar(cls, data):
        query = """
            UPDATE estudiantes
            SET nombre = %(nombre)s, email = %(email)s
            WHERE id_estudiante = %(id_estudiante)s;
        """
        return connectToMySQL("esquema_estudiantes").query_db(query, data)

    @classmethod
    def eliminar(cls, data):
        query = """
            DELETE FROM estudiantes
            WHERE id_estudiante = %(id_estudiante)s;
        """
        return connectToMySQL("esquema_estudiantes").query_db(query, data)
