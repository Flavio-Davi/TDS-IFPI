CREATE TABLE agencia(
	numero INT PRIMARY KEY NOT NULL,
    cidade VARCHAR(45) NOT NULL,
    estado CHAR(2) NOT NULL
);

CREATE TABLE cliente(
	cpf CHAR(11) PRIMARY KEY NOT NULL,
    nome VARCHAR(100),
    rg VARCHAR(13),
    cidade VARCHAR(30),
    estado CHAR(2)
);

CREATE TABLE transacao(
		numero_transacao INT PRIMARY KEY NOT NULL,
        tipo VARCHAR (10),
        data DATETIME,
        valor INT
);

CREATE TABLE conta(
	numero INT PRIMARY KEY NOT NULL,
    saldo INT,
    agencia_numero INT NOT NULL,
    cliente_cpf  CHAR(11) NOT NULL,
    FOREIGN KEY (agencia_numero) REFERENCES agencia(numero),
    FOREIGN KEY (cliente_cpf ) REFERENCES cliente(cpf)
);

CREATE TABLE conta_has_transacao(
	conta_numero INT NOT NULL,
    conta_agencia_numero INT NOT NULL,
    transacao_numero_transacao INT NOT NULL,
    FOREIGN KEY (conta_numero) REFERENCES conta(numero),
    FOREIGN KEY (conta_agencia_numero) REFERENCES conta(agencia_numero),
    FOREIGN KEY (transacao_numero_transacao) REFERENCES transacao(numero_transacao)
);

SHOW TABLES;

SELECT * FROM conta_has_transacao;