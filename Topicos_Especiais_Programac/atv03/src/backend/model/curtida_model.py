class Curtida:
    def __init__(self, id_user: int = None, id_post: int = None):
        self.id_user = id_user
        self.id_post = id_post

    def __repr__(self):
        return f"Curtida(id_user={self.id_user}, id_post={self.id_post})"

