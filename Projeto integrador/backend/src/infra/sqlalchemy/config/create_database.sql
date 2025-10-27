CREATE DATABASE chat;
USE chat;

CREATE TABLE status(
	id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    situacao TINYINT DEFAULT 1 NOT NULL,

	PRIMARY KEY (id)
);

CREATE TABLE enderecos (
	id INT AUTO_INCREMENT NOT NULL,
    rua VARCHAR(50),
    bairro VARCHAR(50),
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,

	PRIMARY KEY (id)
);

CREATE TABLE empresas(
	id INT AUTO_INCREMENT NOT NULL,
    id_endereco INT NOT NULL,
    id_responsavel INT,
    nome_fantasia VARCHAR(100),
    CNPJ VARCHAR(50),
    situacao TINYINT DEFAULT 1 NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_endereco) REFERENCES enderecos(id)
);

CREATE TABLE cargos(
	id INT AUTO_INCREMENT NOT NULL,
    id_empresa INT NOT NULL,
    cargo VARCHAR (50) NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_empresa) REFERENCES empresas(id)
);

CREATE TABLE usuarios(
	id INT AUTO_INCREMENT NOT NULL,
    id_endereco INT NOT NULL,
    id_cargo INT NOT NULL,
    id_status INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_endereco) REFERENCES enderecos(id),
    FOREIGN KEY (id_cargo) REFERENCES cargos(id),
    FOREIGN KEY (id_status) REFERENCES status(id)
);

CREATE TABLE contatos(
	id INT AUTO_INCREMENT NOT NULL,
    id_usuario INT NOT NULL,
    numero VARCHAR(20) NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

ALTER TABLE empresas
ADD CONSTRAINT id_responsavel
FOREIGN KEY (id_responsavel) REFERENCES usuarios(id);

CREATE TABLE chats(
	id INT AUTO_INCREMENT NOT NULL,
    id_empresa INT NOT NULL,
    nome VARCHAR(255),
    tipo ENUM('privada', 'grupo'),
    situacao TINYINT DEFAULT 1 NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_empresa) REFERENCES empresas(id)
);

CREATE TABLE chat_participantes(
	id_chat INT NOT NULL,
    id_usuario INT NOT NULL,
    papel ENUM('administrador', 'membro'),
    data_entrada TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

	FOREIGN KEY (id_chat) REFERENCES chats(id) ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
);

CREATE TABLE mensagens(
	id INT AUTO_INCREMENT NOT NULL,
    id_chat INT NOT NULL,
    id_remetente INT NOT NULL,
    id_destinatario INT NOT NULL,
    mensagem TEXT NOT NULL,
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

	PRIMARY KEY (id),
    FOREIGN KEY (id_chat) REFERENCES chats(id) ON DELETE CASCADE,
    FOREIGN KEY (id_remetente) REFERENCES usuarios(id),
    FOREIGN KEY (id_destinatario) REFERENCES usuarios(id)
);

