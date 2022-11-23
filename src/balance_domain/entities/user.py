
class UserEntity:
    def __init__(self,
                 id: int = None,
                 surname: str = "",
                 fullname: str = "",
                 email: str = "",
                 hashed_password: str = "",
                 is_active: bool = False):
        self.id = id
        self.surname = surname
        self.fullname = fullname
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active

