from database import db as database
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
  pass


class User(Base):
  __tablename__ = "usuarios"
  id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
  nome: Mapped[str] = mapped_column(String(100), nullable=False)
  idade: Mapped[int] = mapped_column(Integer, nullable=False)
  email: Mapped[str] = mapped_column(Integer, nullable=False)
  data_cadastro: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)