
class BankEntity:
    def __init__(self,
                 id: int = None,
                 token: str = "",
                 code: str = "",
                 certificate_url: str = "",
                 is_active: bool = False,
                 user_id: int = None,):
        self.id = id
        self.token = token
        self.code = code
        self.certificate_url = certificate_url
        self.is_active = is_active
        self.user_id = user_id

    def to_json(self):
        return vars(self)
