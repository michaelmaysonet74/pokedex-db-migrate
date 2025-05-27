from psql.models.base import Base

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Ability(Base):
    __tablename__ = "abilities"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    effect: Mapped[str] = mapped_column(String)
    is_hidden: Mapped[bool] = mapped_column(Boolean)

    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped["Pokemon"] = relationship(back_populates="abilities")  # type: ignore

    def __repr__(self) -> str:
        return f"Ability(name={self.name}, effect={self.effect}, is_hidden={self.is_hidden})"
