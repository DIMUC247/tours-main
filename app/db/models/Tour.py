from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean

from app.db import Base


class Tour(Base):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    name: Mapped[Optional[str]] = mapped_column((String(50)), nullable=True)
    is_reserved: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __str__(self):
        return f"Тур до№ {self.number}: {self.name}"
