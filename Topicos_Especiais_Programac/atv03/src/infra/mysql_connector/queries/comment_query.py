class Comment_query:
    def create(self) -> str:
        QUERY = '''
                    INSERT INTO
                        comment(id_user, id_post, conteudo, data_hora)
                    VALUES
                        (%s, %s, %s, %s);'''
        return QUERY

    def read(self, id: bool | None=False, id_post: bool | None=False) -> str:
        if id:
            QUERY = '''SELECT conteudo, data_hora FROM comentarios WHERE id=%s;'''
        elif id_post:
            QUERY = '''SELECT conteudo, data_hora FROM comentarios WHERE id_post=%s;'''
        else:
            QUERY = '''SELECT conteudo, data_hora FROM comentarios;'''
        return QUERY
    
    def update(self, **kwargs) -> str:
        '''
            id 
            id_user 
            id_post 
            conteudo 
            data_hora'''
        
        if 'id' not in kwargs:
            raise ValueError('Necessário ID do telefone para atualização.')
        
        kwargs.pop('id')
        kwargs.pop('data_hora')
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

