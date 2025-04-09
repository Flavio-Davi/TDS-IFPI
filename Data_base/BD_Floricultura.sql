CREATE DATABASE floricultura;

CREATE TABLE compras(
	nota_fiscal INT NOT NULL,
    data DATE,
    valor FLOAT,
    quantidade INT,
    
    PRIMARY KEY (nota_fiscal)
);

CREATE TABLE cliente(
	id_cliente INT AUTO_INCREMENT NOT NULL,
    CPF CHAR(11),
    RG VARCHAR(13),
    nome VARCHAR(100),
    telefone CHAR(11),
    endereco VARCHAR(150),
    
	PRIMARY KEY (id_cliente)
);

CREATE TABLE produto(
	codigo INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    preco FLOAT NOT NULL,
    quantidade_estoque INT NOT NULL,
    
	PRIMARY KEY(codigo)
);

CREATE TABLE auxiliar_produto_cliente(
	codigo_produto INT NOT NULL,
    id_cliente INT NOT NULL,
    
    FOREIGN KEY (codigo_produto) REFERENCES produto(codigo),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

SHOW TABLES;