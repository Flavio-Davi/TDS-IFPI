CREATE DATABASE biblioteca;

CREATE TABLE editora(
	CNPJ CHAR(14) NOT NULL,
    Razão_Social VARCHAR(45) NOT NULL,
    
    PRIMARY KEY (CNPJ)
);

CREATE TABLE categoria(
	codigo INT NOT NULL,
    descricao VARCHAR(45),
    
    PRIMARY KEY (codigo)
);

CREATE TABLE nacionalidade(
	codigo INT NOT NULL,
    descricao VARCHAR(45),
    
    PRIMARY KEY (codigo)
);

CREATE TABLE autor(
	passaporte CHAR(8),
    nome VARCHAR(100),
    cod_nacionalidade INT,
    
    PRIMARY KEY (passaporte),
    FOREIGN KEY (cod_nacionalidade) REFERENCES nacionalidade(codigo)
);

CREATE TABLE  livro(
	ISBN INT NOT NULL,
    titulo VARCHAR(45),
    ano YEAR,
    CNPJ_editora CHAR(14),
    cod_categoria INT,
    
    PRIMARY KEY (ISBN),
    FOREIGN KEY (CNPJ_editora) REFERENCES editora(CNPJ),
    FOREIGN KEY (cod_categoria) REFERENCES categoria(codigo)
);

CREATE TABLE auxiliar_autor_livro(
	passaporte CHAR(8) NOT NULL,
    ISBN INT NOT NULL,
    CNPJ CHAR(14) NOT NULL,
    
    FOREIGN KEY (passaporte) REFERENCES autor(passaporte),
    FOREIGN KEY (ISBN) REFERENCES livro(ISBN),
    FOREIGN KEY (CNPJ) REFERENCES editora(CNPJ)
);

SHOW TABLES;