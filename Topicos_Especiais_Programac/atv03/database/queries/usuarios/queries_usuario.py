class Queries_usuario:
    @staticmethod
    def create():
        QUERY = """INSERT INTO
                        usuarios(nome_completo, email, data_nascimento)
                    VALUES
                        (%s, %s, %s);"""
        return QUERY

    @staticmethod
    def read(param: bool=False):
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
    
    @staticmethod
    def update():
        QUERY = """UPDATE
                        usuarios
                    SET
                        id=%s, nome_completo=%s, email=%s, data_nascimento=%s
                    WHERE
                        id=%s;"""
        return QUERY
    
    @staticmethod
    def delete():
        QUERY = """DELETE FROM
                        usuarios
                    WHERE
                        id=%s;"""
        return QUERY
