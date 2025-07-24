CREATE DATABASE IF NOT EXISTS pyonerp DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE pyonerp;

-- Tabela de produtos (compatível com backend_mysql.py)
CREATE TABLE IF NOT EXISTS produtos (
    nome VARCHAR(255) PRIMARY KEY,
    quantidade INT,
    preco DOUBLE
);

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARBINARY(255) NOT NULL,
    papel INT NOT NULL,
    FOREIGN KEY (papel) REFERENCES papeis(id)
);

-- Tabela de papéis (roles)
CREATE TABLE IF NOT EXISTS papeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela de permissões
CREATE TABLE IF NOT EXISTS permissoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

-- Relação entre papéis e permissões
CREATE TABLE IF NOT EXISTS papel_permissao (
    papel_id INT,
    permissao_id INT,
    PRIMARY KEY (papel_id, permissao_id),
    FOREIGN KEY (papel_id) REFERENCES papeis(id) ON DELETE CASCADE,
    FOREIGN KEY (permissao_id) REFERENCES permissoes(id) ON DELETE CASCADE
);

-- Inserção dos papéis padrão
INSERT IGNORE INTO papeis (id, nome) VALUES (1, 'admin'), (2, 'usuario');

-- Inserção das permissões padrão
INSERT IGNORE INTO permissoes (id, nome) VALUES (1, 'usuario_ver'), (2, 'usuario_criar');

-- Atribuição de permissões ao papel admin
INSERT IGNORE INTO papel_permissao (papel_id, permissao_id) VALUES 
(1, 1), (1, 2);