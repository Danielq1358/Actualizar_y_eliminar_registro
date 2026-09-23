CREATE DATABASE IF NOT EXISTS esquema_estudiantes;

USE esquema_estudiantes;

CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO estudiantes (nombre, email)
SELECT 'Joe Doe', 'joedoe@email.com'
WHERE NOT EXISTS (SELECT 1 FROM estudiantes);

INSERT INTO estudiantes (nombre, email)
SELECT 'Ana Perez', 'ana@email.com'
WHERE (SELECT COUNT(*) FROM estudiantes) = 1;

INSERT INTO estudiantes (nombre, email)
SELECT 'Carlos Soto', 'carlos@email.com'
WHERE (SELECT COUNT(*) FROM estudiantes) = 2;

INSERT INTO estudiantes (nombre, email)
SELECT 'Maria Gonzalez', 'maria@email.com'
WHERE (SELECT COUNT(*) FROM estudiantes) = 3;
