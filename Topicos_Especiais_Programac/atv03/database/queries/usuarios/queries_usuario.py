class Queries_usuario:
    def create(self):
        QUERY = """INSERT INTO
                        usuarios(nome_completo, email, data_nascimento)
                    VALUES
                        (%s, %s, %s);"""
        return QUERY

    def read(self, param: bool=False):
        if param:
            QUERY = """SELECT
                            *
                        FROM
                            usuarios
                        WHERE
                            id=%s;"""
        else:
            QUERY = """SELECT
                            *
                        FROM
                            usuarios;"""
        return QUERY
    
    def update(self):
        QUERY = """UPDATE
                        usuarios
                    SET
                        id=%s, nome_completo=%s, email=%s, data_nascimento=%s
                    WHERE
                        id=%s;"""
        return QUERY
        
    def delete(self):
        QUERY = """DELETE FROM
                        usuarios
                    WHERE
                        id=%s;"""
        return QUERY

