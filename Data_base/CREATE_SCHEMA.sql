CREATE SCHEMA ERP;

CREATE TABLE Projetos(
	PCODIGO			CHAR(6) NOT NULL, -- Código único do Projeto
    PNOME			VARCHAR(24), -- Nome Do Projeto
	DCODIGO			CHAR(3), -- Código do Departamento
    RESP			CHAR(6), -- Matrícula do Responsável
    EQUIPE			DEC(5), -- Número de Empregados no Projeto
    DATAINI			DATE, -- Data de início
    DATAFIM			DATE, -- Data do final
    
    PRIMARY KEY (PCODIGO),
    FOREIGN KEY (DCODIGO) REFERENCES Departamentos(DCODIGO),
    FOREIGN KEY (RESP) REFERENCES Empregados(MATR)
);

CREATE TABLE Departamentos(
	DCODIGO			CHAR(3) NOT NULL, -- Código único do departamento 
    DNOME			VARCHAR(36) NOT NULL, -- Nome do departamento 
    GERENTE			CHAR(6), -- Matrícula do Gerente
    
    PRIMARY KEY (DCODIGO),
    FOREIGN KEY (GERENTE) REFERENCES Empregados(MATR)
);


CREATE TABLE Empregados(
	MATR			CHAR(6) NOT NULL, -- Matricula única do empregado 
	NOME			VARCHAR(12) NOT NULL, -- Primeiro name
	SOBRENOME 		VARCHAR(15) NOT NULL, 
    DEPT 			CHAR(3), -- Código de departamento do empregado
    FONE 			CHAR(14),
    DATAADM			DATE,  -- Data de admissão
    CARGO			CHAR(10), -- Cargo do empregado
    NIVELEDUC		DEC,
    SEXO			ENUM("F", "M"),
    DATANASC		DATE,
    SALARIO			DECIMAL(9, 2), -- Salário Anual
    BONUS 			DECIMAL(9, 2),-- Bônus Anual
    COMIS 			DECIMAL(9, 2),-- Comissão Anual

	PRIMARY KEY (MATR),
	FOREIGN KEY (DEPT) REFERENCES Departamentos(DCODIGO)
)
