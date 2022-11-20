from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from balance_domain.settings import UserAlchemyAdapter


class User:
    def __int__(self):
        self.connection = UserAlchemyAdapter()

    def _get_user_by_id(self, user_id: int):
        query = f"SELECT * FROM `balance`.`TB_USER` WHERE `id`={user_id};"
        response = self.connection.execute(query).first()
        user = {}

        for field in response:
            field_formatted = list(field)
            field_key = field_formatted[0]
            field_value = field_formatted[1]
            user[field_key] = field_value
        return user

    def _get_user_by_id(self, user: dict):
        surname = user.surname
        fullname = user.fullname
        email = user.email
        password = user.password

        query = f"INSERT INTO balance.TB_USER(surname, fullname, email, password) \
                VALUES('{surname}', '{fullname}', '{email}', '{password}');"
        response = self.connection.execute(query).first()
        return user





    # id = Column(Integer, primary_key=True, index=True)
    # surname = Column(String)
    # fullname = Column(String)
    # email = Column(String, unique=True, index=True)
    # list_banks = ARRAY(PickleType)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)
    #
    # bank = relationship("Bank", back_populates="user")
    #
    # def to_json(self):
    #     return vars(self)


class Bank(Base):
    __tablename__ = "bank"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Integer)
    token = Column(String)
    cpf = Column(String)
    password = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="bank")

    def to_json(self):
        return vars(self)
