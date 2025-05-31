from psql.models.base import Base

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class BaseStats(Base):
    __tablename__ = "base_stats"

    id: Mapped[int] = mapped_column(primary_key=True)
    hp: Mapped[int] = mapped_column(Integer)
    attack: Mapped[int] = mapped_column(Integer)
    defense: Mapped[int] = mapped_column(Integer)
    special_attack: Mapped[int] = mapped_column(Integer)
    special_defense: Mapped[int] = mapped_column(Integer)
    speed: Mapped[int] = mapped_column(Integer)

    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped["Pokemon"] = relationship(back_populates="base_stats")  # type: ignore

    def to_dict(self) -> dict:
        return {
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "special_attack": self.special_attack,
            "special_defense": self.special_defense,
            "speed": self.speed,
        }

    def __repr__(self) -> str:
        return (
            f"BaseStats(hp={self.hp}, attack={self.attack}, "
            f"defense={self.defense}, special_attack={self.special_attack}, "
            f"special_defense={self.special_defense}, speed={self.speed})"
        )
