from datetime import datetime

class Amizade:
    def __init__(self, user_id: int = None, user_id_02: int = None, data_hora: datetime = None):
        self.user_id = user_id
        self.user_id_02 = user_id_02
        self.data_hora = data_hora

    def __repr__(self):
        return f"Amizade(user_id={self.user_id}, user_id_02={self.user_id_02}, data_hora={self.data_hora})"

