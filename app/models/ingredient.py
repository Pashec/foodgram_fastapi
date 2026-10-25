from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class Ingredient(Base):

    __tablename__ = 'ingredients'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False, index=True)
    measurement_unit: Mapped[str] = mapped_column(String(64), nullable=False)
