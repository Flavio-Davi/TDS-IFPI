class Post_query:
    def create(self) -> str:
        QUERY = '''
                    INSERT INTO
                        posts(id_user, data_hora, conteudo, midia)
                    VALUES
                        (%s, %s, %s, %s);'''
        return QUERY

    def read(self, id: bool | None=False) -> str:
        if id:
            QUERY = '''SELECT data_hora, conteudo, midia FROM posts WHERE id=%s;'''
        else:
            QUERY = '''SELECT data_hora, conteudo, midia FROM telefones;'''
        return QUERY
    
    def update(self, **kwargs) -> str:
        if 'id' not in kwargs:
            raise ValueError('Necessário ID do telefone para atualização.')
        
        kwargs.pop('id')
        set_querie = [f'{ch} = %s' for ch in kwargs.keys()]
        set_querie = ', '.join(set_querie)

        QUERY = f'''
                    UPDATE 
                        posts
                    SET
                        {set_querie}
                    WHERE 
                        id = %s'''
        return QUERY
    
    def delete(self) -> str:
        QUERY = '''
                    DELETE FROM
                        posts
                    WHERE
                        id=%s;'''
        return QUERY

