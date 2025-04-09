CREATE DATABASE firma;

CREATE TABLE pedido(
	numero INT AUTO_INCREMENT NOT NULL,
    data DATETIME,
    quantidade INT,
    
    PRIMARY KEY (numero)
);

CREATE TABLE cliente(
	id_cliente INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    endereco VARCHAR(150),
    telefone CHAR(11),
    status VARCHAR(20),
    limite_creditos INT,
    numero_pedido INT,
    
    PRIMARY KEY(id_cliente),
    FOREIGN KEY (numero_pedido) REFERENCES pedido(numero)    
);

CREATE TABLE produto(
	id_produto INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    categoria VARCHAR(20),
    preco FLOAT,
    numero_pedido INT,
    codigo_cliente INT,
    
    PRIMARY KEY (id_produto),
    FOREIGN KEY (numero_pedido) REFERENCES pedido(numero),
    FOREIGN KEY (codigo_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE auxiliar_pedido_produto(
	id_produto INT NOT NULL,
    numero_pedido INT NOT NULL,
	
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
    FOREIGN KEY (numero_pedido) REFERENCES pedido(numero)
);

SHOW TABLES;