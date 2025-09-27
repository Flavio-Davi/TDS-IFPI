class Querie_professor:
    def create(self):
        QUERY = """INSERT INTO 
                        esc_professores (nome_completo, matricula, data_nascimento, email, status)
                    VALUES
                        (%s, %s, %s, %s, %s);"""
        return QUERY

    def read(self, matricula: bool | None=None):
        if matricula:
            QUERY = "SELECT * FROM esc_professores WHERE matricula = %s"
        else:
            QUERY = "SELECT * FROM esc_professores"
        return QUERY

    def update(self, clause: str):
        QUERY = f"""UPDATE 
                        esc_professores 
                   SET 
                        {clause}
                   WHERE 
                        id=11;"""
        return QUERY
    
    def delete(self):
        QUERY = "DELETE esc_professores FROM esc_professores WHERE id=%s"
        return QUERY