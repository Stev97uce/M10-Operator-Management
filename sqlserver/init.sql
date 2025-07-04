USE master;
GO
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'operator_db')
BEGIN
    CREATE DATABASE operator_db;
END;
GO
USE operator_db;
GO

CREATE TABLE operators (
    id INT PRIMARY KEY IDENTITY(1,1),
    user_id NVARCHAR(100) NOT NULL,
    branch_id INT NOT NULL,
    role NVARCHAR(50),
    is_active BIT DEFAULT 1
);
