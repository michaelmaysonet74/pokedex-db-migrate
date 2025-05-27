from psql.models.base import Base

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Measurement(Base):
    __tablename__ = "measurement"

    id: Mapped[int] = mapped_column(primary_key=True)
    height: Mapped[str] = mapped_column(String)
    weight: Mapped[str] = mapped_column(String)

    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped["Pokemon"] = relationship(back_populates="measurement")  # type: ignore

    def __repr__(self) -> str:
        return f"Measurement(height={self.height}, weight={self.weight})"
