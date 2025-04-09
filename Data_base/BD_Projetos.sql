CREATE DATABASE projetos;

CREATE TABLE cliente(
	CPF CHAR(11) NOT NULL,
    nome VARCHAR(100), 
    endereco VARCHAR(150),
    telefone INT(11),
    
    PRIMARY KEY (CPF)
);

CREATE TABLE desenvolvedor(
	id_desenvolvedor INT AUTO_INCREMENT NOT NULL,
    inicio_projeto DATETIME NOT NULL,
    fim_projeto DATETIME NOT NULL,
    CPF CHAR(11) NOT NULL,
    nome VARCHAR(100),
    valor_hora FLOAT,
	
    PRIMARY KEY (id_desenvolvedor)
);

CREATE TABLE projeto(
	codigo INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    data_inicio DATETIME,
    fim_projeto DATETIME,
    CPF_cliente CHAR(11) NOT  NULL,
    
    PRIMARY  KEY(codigo),
    FOREIGN KEY (CPF_cliente) REFERENCES cliente(CPF)
);

CREATE TABLE auxiliar_projeto_desenvolvedor(
	codigo_projeto INT NOT NULL,
    CPF_cliente CHAR(11) NOT NULL,
    id_desenvolvedor INT NOT NULL,
    
    FOREIGN KEY (codigo_projeto) REFERENCES projeto(codigo),
	FOREIGN KEY (CPF_cliente) REFERENCES cliente(CPF),
    FOREIGN KEY (id_desenvolvedor) REFERENCES desenvolvedor(id_desenvolvedor)
);

SHOW TABLES