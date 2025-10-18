class Like_query:
    def create(self) -> str:
        QUERY = '''
                    INSERT INTO
                        curtidas(id_post, id_user)
                    VALUES
                        (%s, %s);'''
        return QUERY

    def read(self, id_post: bool | None=False) -> str:
        if id_post:
            QUERY = '''
                        SELECT 
                            COUNT(*)
                        FROM
                            curtidas
                        WHERE
                            id_post=%s'''
        else:
            QUERY = '''
                        SELECT 
                            COUNT(*)
                        FROM
                            curtidas;'''
        
        return QUERY
        
    def delete(self) -> str:
        QUERY = '''
                    DELETE FROM
                        curtidas
                    WHERE
                        id_user=%s
                        AND id_post=%s;'''
        return QUERY

