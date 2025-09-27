class Querie_disciplina:
    def create(self):
        QUERY = f"""INSERT INTO
                        esc_disciplinas (codigo_disc, nome, descricao, id_professor, carga_horaria)
                    VALUES 
                        (%s, %s, %s, %s, %s);
                """
        return QUERY
    
    def read(self, id: bool | None=None):
        if id:
            QUERY = """SELECT * FROM esc_disciplinas WHERE id=%s;"""
        else:
            QUERY = """SELECT * FROM esc_disciplinas;"""
        return QUERY
    
    def update(self, campos):
        QUERY = f"UPDATE disciplina SET {', '.join(campos)} WHERE codigo = %s"
        return QUERY
    
    def delete(self, id: int):
        QUERY = "DELETE esc_disciplinas FROM esc_disciplinas WHERE id=%s"
        return QUERY