from psql.models.base import Base
from psql.models.ability import Ability
from psql.models.measurement import Measurement

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY


class Pokemon(Base):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    abilities: Mapped[list[Ability]] = relationship(  # type: ignore
        back_populates="pokemon", cascade="all, delete-orphan"
    )

    category: Mapped[str] = mapped_column(String)
    entry: Mapped[str] = mapped_column(String)
    sprite: Mapped[str] = mapped_column(String)
    generation: Mapped[int] = mapped_column(Integer)

    measurement: Mapped[Measurement] = relationship(  # type: ignore
        back_populates="pokemon", cascade="all, delete-orphan"
    )

    types: Mapped[list[str]] = mapped_column(ARRAY(String))
    weaknesses: Mapped[list[str]] = mapped_column(ARRAY(String))

    def __repr__(self) -> str:
        return (
            f"Pokemon(id={self.id}, name={self.name}, abilities={self.abilities}, "
            f"category={self.category}, entry={self.entry}, sprite={self.sprite}, "
            f"generation={self.generation}, measurement={self.measurement}, "
            f"types={self.types}, weaknesses={self.weaknesses})"
        )
