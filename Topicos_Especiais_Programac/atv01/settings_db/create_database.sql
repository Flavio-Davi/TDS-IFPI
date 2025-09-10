CREATE DATABASE escola;

USE escola;

CREATE TABLE professor(
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
	sobrenome VARCHAR(200) NOT NULL,
	matrícula TEXT NOT NULL,
	data_nascimento DATE NOT NULL,
	email VARCHAR(100),

    PRIMARY KEY (id)
);

CREATE TABLE disciplina(
	id INT NOT NULL AUTO_INCREMENT,
    codigo VARCHAR(10) NOT NULL,
	nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    id_professor INT,
    
    PRIMARY KEY (id),
    FOREIGN KEY (id_professor) REFERENCES professor(id)
)
