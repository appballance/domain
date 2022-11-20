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

    bank = relationship("TB_BANK", back_populates="user")

    def to_json(self):
        return vars(self)


class Bank(Base):
    __tablename__ = "TB_BANK"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(800))
    user_id = Column(Integer, ForeignKey("TB_USER.id"))
    is_active = Column(Boolean, default=True)

    user = relationship("TB_USER", back_populates="bank")

    def to_json(self):
        return vars(self)
