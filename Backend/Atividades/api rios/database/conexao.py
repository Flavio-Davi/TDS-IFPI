from mysql import connector

class Conexao:
    def __init__(self):
        try:
            self.__cnx = connector.connect(
                user = "root", password="mysql123",
                host = "127.0.0.1",
                database = "cidades"
            )
            self.__cursor = self.__cnx.cursor()
        except Exception as e:
            raise(e)
        
    
    def read(self, query: str, param: None | tuple):
        try:
            if param:
                self.__cursor.execute(query, param)
                dados = self.__cursor.fetchall()
            else:
                self.__cursor.execute(query)
                dados = self.__cursor.fetchall()
                
        except Exception as e:
            raise(e)
        
        return dados
    

    def update(self, query: str, param: tuple):
        try:
            self.__cursor.execute(query, param)
            self.__cnx.commit()
        except Exception as e:
            raise(e)


    def close_connection(self):
        self.__cursor.close()
        self.__cnx.close()
       

if __name__ == '__main__':
    Conexao()
