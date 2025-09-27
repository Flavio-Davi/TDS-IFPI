class Querie_aluno:
    def create(self) -> str:
        QUERY = """INSERT INTO 
                        esc_alunos (matricula, nome_completo, data_nascimento, cpf)
                    VALUES
                        (%s, %s, %s, %s)"""
        return QUERY
    
    def read(self, matricula: bool | None=None) -> str:
        if matricula:
            QUERY = f"""SELECT * FROM esc_alunos WHERE matricula=%s"""
        else:
            QUERY = """SELECT * FROM esc_alunos"""
        return QUERY
    
    def update(self, clause: str) -> str:
        QUERY = f"""UPDATE
                        esc_alunos
                    SET
                        {clause}
                    WHERE
                        matricula=%s"""
        return QUERY

    def delete(self) -> str:
        QUERY = """DELETE FROM esc_alunos WHERE matricula=%s;"""
        return QUERY
