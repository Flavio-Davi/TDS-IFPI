class Phone_query:
    def create(self) -> str:
        QUERY = '''
                    INSERT INTO
                        telefones(id_user, telefone)
                    VALUES
                        (%s, %s);'''
        return QUERY

    def read(self, id: bool | None=False) -> str:
        if id:
            QUERY = '''SELECT telefone FROM telefones WHERE id=%s;'''
        else:
            QUERY = '''SELECT telefone FROM telefones;'''
        return QUERY
    
    def update(self, **kwargs) -> str:
        if 'id' not in kwargs:
            raise ValueError('Necessário ID do telefone para atualização.')
                        
        QUERY = f'''
                    UPDATE 
                        telefones 
                    SET
                        telefone
                    WHERE 
                        id = %s'''
        return QUERY
    
    def delete(self) -> str:
        QUERY = '''
                    DELETE FROM
                        usuario
                    WHERE
                        id=%s;'''
        return QUERY

