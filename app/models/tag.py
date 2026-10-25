from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class Tag(Base):
    
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)