CREATE TABLE especialidade(
	id INT NOT NULL,
    especialidade VARCHAR (45),
    
    PRIMARY KEY (id)
);

CREATE TABLE medico(
	CRM INT NOT NULL,
    nome VARCHAR(100),
    cpf CHAR (11),
    telefone INT(11),
    codigo_especialidade INT,
    
    PRIMARY KEY (CRM),
    FOREIGN KEY (codigo_especialidade) REFERENCES especialidade(id)
);

CREATE TABLE bebe(
	numero_registro INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100),
    nascimento DATETIME,
    peso DECIMAL,
    altura DECIMAL,
    medico_crm INT NOT NULL,
    codigo_especialidade_medica INT NOT NULL,
    
    PRIMARY KEY(numero_registro),
    FOREIGN KEY (medico_crm) REFERENCES medico(CRM),
    FOREIGN KEY (codigo_especialidade_medica) REFERENCES medico(codigo_especialidade)
    
);

CREATE TABLE mae(
	nome VARCHAR(100) NOT NULL,
	cpf CHAR(11) NOT NULL,
    endereco VARCHAR(150) NOT NULL,
    telefone INT(11) NOT NULL,
    nascimento DATE,
    registro_bebe INT NOT NULL,
    crm_medico_parto INT NOT NULL,
    codigo_especialidade_medica INT NOT NULL,

	PRIMARY KEY (cpf),
    FOREIGN KEY (registro_bebe) REFERENCES bebe(numero_registro),
    FOREIGN KEY (crm_medico_parto) REFERENCES bebe(medico_crm),
    FOREIGN KEY (codigo_especialidade_medica) REFERENCES bebe(codigo_especialidade_medica)
);
