from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Principle(Base):
    __tablename__ = "principles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    principle: Mapped[str] = mapped_column(String, nullable=False)
