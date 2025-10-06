CREATE DATABASE startup;

USE startup;

CREATE TABLE usuarios(
	id INT AUTO_INCREMENT NOT NULL,
    nome_completo VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    
    PRIMARY KEY(id)
);

CREATE TABLE posts(
	id INT AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
	data_hora DATETIME NOT NULL,
    conteudo TEXT NOT NULL,
    midia TEXT,
    
	PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES usuarios(id)
);

CREATE TABLE amizade(
	data_hora DATETIME NOT NULL,
    user_id INT NOT NULL, 
    user_id_02 INT NOT NULL,

	PRIMARY KEY (user_id, user_id_02),
    FOREIGN KEY (user_id) REFERENCES usuarios(id),
    FOREIGN KEY (user_id_02) REFERENCES usuarios(id)
);

CREATE TABLE telefones(
	id INT AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
    telefone VARCHAR(20) NOT NULL,    

	PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES usuarios(id)
);

CREATE TABLE comentarios(
	id INT AUTO_INCREMENT  NOT NULL,
    id_user INT NOT NULL,
    id_post INT NOT NULL,
    conteudo TEXT NOT NULL,
    data_hora DATETIME NOT NULL,
    
	PRIMARY KEY (id),
    FOREIGN KEY (id_user) REFERENCES usuarios(id),
    FOREIGN KEY (id_post) REFERENCES posts(id)
);

CREATE TABLE curtidas(
	id INT AUTO_INCREMENT NOT NULL,
    id_post INT NOT NULL,
    id_user INT NOT NULL,

	PRIMARY KEY (id),
    FOREIGN KEY (id_post) REFERENCES posts(id),
    FOREIGN KEY (id_user) REFERENCES usuarios(id)
);