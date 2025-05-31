from psql.models.base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY, JSONB


class EvolutionChain(Base):
    __tablename__ = "evolution_chains"

    id: Mapped[int] = mapped_column(primary_key=True)
    from_: Mapped[dict] = mapped_column(JSONB, nullable=True, default=None)
    to: Mapped[list[dict]] = mapped_column(ARRAY(JSONB), nullable=True, default=[])

    pokemon_id: Mapped[int] = mapped_column(ForeignKey("pokemon.id"))
    pokemon: Mapped["Pokemon"] = relationship(back_populates="evolution")  # type: ignore

    def to_dict(self) -> dict:
        return {
            "from": self.from_ if self.from_ else None,
            "to": self.to if self.to else [],
        }

    def __repr__(self) -> str:
        return f"EvolutionChain(from_={self.from_}, to={self.to})"
