CREATE DATABASE glr_volei;

USE glr_volei;

CREATE TABLE categorias(
	id INT AUTO_INCREMENT NOT NULL,
	categoria VARCHAR(255) NOT NULL,
    descricao TEXT,

	PRIMARY KEY (id)
);

CREATE TABLE users(
	id INT AUTO_INCREMENT NOT NULL,
    id_categoria INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    sexo VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,

	PRIMARY KEY (id),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

CREATE TABLE arena(
	id INT AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
    endereco VARCHAR(255) NOT NULL,
	coberta BOOLEAN NOT NULL,
    estrela TINYINT UNSIGNED NOT NULL DEFAULT 0,
    revisao TEXT,

	PRIMARY KEY(id),
    FOREIGN KEY (id_user) REFERENCES users(id)
);

CREATE TABLE contatos(
	id INT AUTO_INCREMENT NOT NULL,
    id_users INT NOT NULL,
    id_arena INT,
    contato VARCHAR(255) NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_users) REFERENCES users(id),
    FOREIGN KEY (id_arena) REFERENCES arena(id)
);

CREATE TABLE partidas(
	id INT AUTO_INCREMENT NOT NULL,
	id_usuario INT NOT NULL,
    id_arena INT NOT NULL,
    id_moderador INT,
    nome_partida VARCHAR(255) NOT NULL,
    data DATETIME NOT NULL,
    
	PRIMARY KEY (id),
	FOREIGN KEY (id_usuario) REFERENCES users(id),
    FOREIGN KEY (id_arena) REFERENCES arena(id),
    FOREIGN KEY (id_moderador) REFERENCES users(id)
);
