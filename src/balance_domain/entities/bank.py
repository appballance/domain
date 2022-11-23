
class BankEntity:
    def __init__(self,
                 id: int = None,
                 token: str = "",
                 number: str = "",
                 is_active: bool = False,
                 user_id: int = None,):
        self.id = id
        self.token = token
        self.number = number
        self.is_active = is_active
        self.user_id = user_id
