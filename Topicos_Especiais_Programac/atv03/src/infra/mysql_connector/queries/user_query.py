class User_query:
    def create(self) -> str:
        QUERY = '''
                    INSERT INTO
                        usuarios(nome_completo, email, data_nascimento)
                    VALUES
                        (%s, %s, %s);'''
        return QUERY

    def read(self, id: bool | None=False, nome: bool | None=False) -> str:
        if id:
            QUERY = '''SELECT * FROM usuarios WHERE id=%s;'''
        else:
            QUERY = '''SELECT * FROM usuarios;'''
        
        return QUERY
    
    def update(self, **kwargs) -> str:
        if 'id' not in kwargs:
            raise ValueError('Necessário ID de usuário para atualização.')
        
        kwargs.pop('id')
        set_querie = [f'{ch} = %s' for ch in kwargs.keys()]
        set_querie = ', '.join(set_querie)
        
        QUERY = f'''
                    UPDATE 
                        usuarios
                    SET
                        {set_querie}
                    WHERE 
                        id = %s'''
        return QUERY
    
    def delete(self) -> str:
        QUERY = '''
                    DELETE FROM
                        usuarios
                    WHERE
                        id=%s;'''
        return QUERY

