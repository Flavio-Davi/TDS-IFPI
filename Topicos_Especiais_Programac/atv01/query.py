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
        QUERY = """UPDATE 
    professor 
SET
    primeironome = %s, sobrenome=%s, matricula=%s, data_nascimento=%s, email=%s
WHERE
    id=%s;"""

        return QUERY

    def update_teacher_firstname(self) -> str:
        QUERY = """UPDATE 
    professor 
SET
    primeironome = %s
WHERE
    id=%s;"""
        
        return QUERY
  
    def update_teacher_lastname(self) -> str:
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
        QUERY = """UPDATE 
    professor 
SET
    data_nascimento=%s
WHERE
    id=%s;"""
        
        return QUERY
    
    def update_teacher_email(self) -> str:
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


if __name__ == '__main__':
    Querie()
