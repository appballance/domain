from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from balance_domain.database.settings import Base


class User(Base):
    __tablename__ = "TB_USER"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(255))
    fullname = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    bank = relationship("Bank")

    def to_json(self):
        return vars(self)


class Bank(Base):
    __tablename__ = "TB_BANK"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(800))
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("TB_USER.id"))

    def to_json(self):
        return vars(self)
