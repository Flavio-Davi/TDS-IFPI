CREATE TABLE usuario(
	id INT NOT NULL AUTO_INCREMENT,
	nome_completo VARCHAR(200) NOT NULL,
    email VARCHAR(50) NOT NULL,
    numero_cel VARCHAR(14),

    PRIMARY KEY (id)
);

CREATE TABLE conversa(
	id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    data_hora DATE NOT NULL,
    conteudo TEXT NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES usuario(id)
);

