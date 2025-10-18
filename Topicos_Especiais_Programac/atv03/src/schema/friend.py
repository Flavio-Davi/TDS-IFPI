from datetime import datetime


class BaseFriend:
    def __init__(self, data_hora: datetime):
        self.data_hora = data_hora

    def __str__(self):
        data = {
            'data_hora': self.data_hora
        }
        return data


class CreateFrien(BaseFriend):
    pass


class UpdateFriend(BaseFriend):
    def __init__(self, user_id: int, user_id_02: int):
        super().__init__()
        self.user_id = user_id
        self.user_id_02 = user_id_02
