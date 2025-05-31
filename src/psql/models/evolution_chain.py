from psql.models.base import Base
from psql.models.evolution import Evolution

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class EvolutionChain(Base):
    __tablename__ = "evolution_chains"

    id: Mapped[int] = mapped_column(primary_key=True)

    from_: Mapped[Evolution | None] = relationship(
        back_populates="from_chain",
        cascade="all",
    )

    to: Mapped[list[Evolution]] = relationship(
        back_populates="to_chain",
        cascade="all",
    )

    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped["Pokemon"] = relationship(back_populates="evolution")  # type: ignore

    def to_dict(self) -> dict:
        return {
            "from": self.from_.to_dict() if self.from_ else None,
            "to": [evolution.to_dict() for evolution in self.to],
        }

    def __repr__(self) -> str:
        return f"EvolutionChain(from_={self.from_}, to={self.to})"
