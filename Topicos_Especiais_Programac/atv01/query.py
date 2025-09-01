class Querie:    
    def create_teacher(self) -> str:
        """Insira cinco argumentos na execução da consulta:
        1. Primeiro nome -> type: str()
        2. Sobrenome -> type: str()
        3. Matrícula -> type: str()
        4. Data de nascimento -> type: date()
        5. E-mail -> type: str()
        """

        QUERY = """INSERT INTO 
    professor (primeiro_nome, sobrenome, matricula, data_nascimento, email)
VALUES
    (%s, %s, %s, %s, %s);"""

        return QUERY
    
    def read_all_teacher(self) -> str:
        """Retorna os dados de todos os professores."""

        QUERY = """SELECT
    *
FROM
    professor"""

        return QUERY

    def read_teacher(self) -> str:
        """Insira a matrícula do professor que deseja consultar as informações na execução da consulta:
        1. matrícula -> type: str()
        """

        QUERY = """SELECT
    *
FROM
    professor
WHERE
    matricula = %s"""

        return QUERY

    def update_teacher(self) -> str:
        """Insira os dados do professor que deseja atualizar na execução da consulta:
        1. primeiro_nome -> type: str()
        2. sobrenome -> type: str()
        3. matricula -> type: str()
        4. data de nascimento -> type: date()
        5. email -> type: str()
        6. id -> type: str()
        """

        QUERY = """UPDATE 
    professor 
SET
    primeiro_nome = %s, sobrenome=%s, matricula=%s, data_nascimento=%s, email=%s
WHERE
    id=%s;"""

        return QUERY

    def update_teacher_firstname(self) -> str:
        """Insira o primeiro nome do professor que deseja atualizar na execução da consulta:
        1. primeiro nome -> type: str()
        """

        QUERY = """UPDATE 
    professor 
SET
    primeiro_nome = %s
WHERE
    id=%s;"""
        
        return QUERY
  
    def update_teacher_lastname(self) -> str:
        """Insira o sobrenome do professor que deseja atualizar na execução da consulta:
        1. sobrenome -> type: str()
        """

        QUERY = """UPDATE 
    professor 
SET
    sobrenome=%s
WHERE
    id=%s;"""
        
        return QUERY

    def update_teacher_registration(self) -> str:
        """Insira a nova matrícula o id do professor que deseja atualizar na execução da consulta:
        1. matrícula nova -> type: str()
        2. id -> type: str()
        """

        QUERY = """UPDATE 
    professor 
SET
    matricula=%s
WHERE
    id=%s;"""
        
        return QUERY

    def update_teacher_birthday(self) -> str:
        """Insira a data de nascimento do professor que deseja atualizar na execução da consulta:
        1. data -> type: date()
        """
        QUERY = """UPDATE 
    professor 
SET
    data_nascimento=%s
WHERE
    id=%s;"""
        
        return QUERY
    
    def update_teacher_email(self) -> str:
        """Insira o email matrícula do professor que deseja atualizar na execução da consulta:
        1. email -> type: str()
        """

        QUERY = """UPDATE 
    professor 
SET
    email=%s
WHERE
    id=%s;"""
        
        return QUERY

    def delete_teacher(self) -> str:
        """Insira o id do professor que deseja DELETAR do banco na execução da consulta:
        1. id -> type: str()
        """

        QUERY = """DELETE FROM
    professor
WHERE
    id = %s"""
        
        return QUERY

    def active_inactive(self) -> str:
        """Insira o valor e o id do professor que deseja ativar/inativar do banco na execução da consulta:
        1. status -> type bool() | (0,1)
        2. id -> type: str()
        """

        QUERY = """UPDATE professor
SET ativo = %s
WHERE id = %s"""

        return QUERY

    def view_registration(self) -> str:
        """Retorna TODAS as matrículas na execução da consulta:
        """

        QUERY = """SELECT matricula FROM professor"""
        
        return QUERY

    def view_firstname(self) -> str:
        """Insira o id do professor na execução da consulta:
        1. id -> type: str()
        """
        
        QUERY = """SELECT
	primeiro_nome
FROM
	professor
WHERE
	id=%s"""
        return QUERY


if __name__ == '__main__':
    Querie()
