from psql.models.base import Base
from psql.models.ability import Ability
from psql.models.base_stats import BaseStats
from psql.models.evolution_chain import EvolutionChain
from psql.models.measurement import Measurement

import json
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY


class Pokemon(Base):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    abilities: Mapped[list[Ability]] = relationship(
        back_populates="pokemon",
        cascade="all, delete-orphan",
    )

    base_stats: Mapped[BaseStats] = relationship(
        back_populates="pokemon",
        cascade="all, delete-orphan",
    )

    category: Mapped[str] = mapped_column(String)
    entry: Mapped[str] = mapped_column(String)

    evolution: Mapped[EvolutionChain] = relationship(
        back_populates="pokemon",
        cascade="all, delete-orphan",
    )

    generation: Mapped[int] = mapped_column(Integer)

    measurement: Mapped[Measurement] = relationship(
        back_populates="pokemon",
        cascade="all, delete-orphan",
    )

    sprite: Mapped[str] = mapped_column(String)
    types: Mapped[list[str]] = mapped_column(ARRAY(String))
    immunities: Mapped[list[str]] = mapped_column(ARRAY(String))
    resistances: Mapped[list[str]] = mapped_column(ARRAY(String))
    weaknesses: Mapped[list[str]] = mapped_column(ARRAY(String))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "abilities": [ability.to_dict() for ability in self.abilities],
            "base_stats": self.base_stats.to_dict(),
            "category": self.category,
            "entry": self.entry,
            "evolution": self.evolution.to_dict(),
            "generation": self.generation,
            "measurement": self.measurement.to_dict(),
            "sprite": self.sprite,
            "types": self.types,
            "immunities": self.immunities,
            "resistances": self.resistances,
            "weaknesses": self.weaknesses,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self) -> str:
        return (
            f"Pokemon(id={self.id}, name={self.name}, abilities={self.abilities}, "
            f"base_stats={self.base_stats}, category={self.category}, entry={self.entry}, "
            f"evolution={self.evolution} sprite={self.sprite}, generation={self.generation}, "
            f"measurement={self.measurement}, types={self.types}, "
            f"immunities={self.immunities}, resistances={self.resistances}, weaknesses={self.weaknesses})"
        )
