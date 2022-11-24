
class UserEntity:
    def __init__(self,
                 id: int = None,
                 surname: str = "",
                 fullname: str = "",
                 email: str = "",
                 password: str = "",
                 is_active: bool = False):
        self.id = id
        self.surname = surname
        self.fullname = fullname
        self.email = email
        self.password = password
        self.is_active = is_active

    def to_json(self):
        return vars(self)
