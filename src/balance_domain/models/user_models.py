from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY, PickleType
from sqlalchemy.orm import relationship
from balance_domain.database.settings import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(255))
    fullname = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    bank = relationship("Bank", back_populates="user")

    def to_json(self):
        return vars(self)


class Bank(Base):
    __tablename__ = "bank"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(800))
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="bank")

    def to_json(self):
        return vars(self)
