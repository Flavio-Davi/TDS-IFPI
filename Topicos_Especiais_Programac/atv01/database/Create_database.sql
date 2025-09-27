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

CREATE TABLE aluno(
	matricula VARCHAR(10) UNIQUE NOT NULL,
    nome_completo VARCHAR(200) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    
    PRIMARY KEY (matricula) 
);

CREATE TABLE endereco_aluno(
	id INT NOT NULL AUTO_INCREMENT,
	rua VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100) NOT NULL,
	cep VARCHAR(100),
    matricula_aluno VARCHAR(100) UNIQUE,
    
    PRIMARY KEY (id),
    FOREIGN KEY (matricula_aluno) REFERENCES aluno(matricula)
);
