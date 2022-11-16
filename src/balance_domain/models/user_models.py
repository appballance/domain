from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY, PickleType
from sqlalchemy.orm import relationship
from balance_domain.database.settings import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    list_banks = ARRAY(PickleType)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    bank = relationship("Bank", back_populates="user")

    def to_json(self):
        return vars(self)


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
