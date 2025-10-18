class Friend_query:
    def create(self) -> str:
        QUERY = '''
                    INSERT INTO
                        amizade(user_id, user_id_02, data_hora)
                    VALUES
                        (%s, %s, %s);'''
        return QUERY

    def read(self, id: bool | None=False) -> str:
        if id:
            QUERY = '''
                        SELECT 
                            COUNT(*)
                        FROM
                            amizade
                        WHERE
                            user_id=%s'''
        else:
            QUERY = '''
                        SELECT 
                            COUNT(*)
                        FROM
                            amizade;'''
    
    def delete(self) -> str:
        QUERY = '''
                    DELETE FROM
                        amizade
                    WHERE
                        user_id=%s
                        AND user_id_02=%s'''
        return QUERY

