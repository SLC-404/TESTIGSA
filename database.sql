IF DB_ID('tareas') IS NULL
    CREATE DATABASE tareas;
GO

USE tareas;
GO

CREATE TABLE tasks (
    id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    title NVARCHAR(150) NOT NULL,
    description NVARCHAR(MAX) NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    created_at DATETIME NOT NULL DEFAULT GETDATE()
);
GO

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL PRIMARY KEY
);
GO

INSERT INTO alembic_version (version_num) VALUES ('28487ee2fe86');
GO
