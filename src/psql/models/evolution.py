from psql.models.base import Base

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Evolution(Base):
    __tablename__ = "evolutions"

    _pk: Mapped[int] = mapped_column(primary_key=True)

    id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String)

    evolution_chain_id: Mapped[int] = mapped_column(ForeignKey("evolution_chains.id"))

    from_chain: Mapped["EvolutionChain"] = relationship(  # type: ignore
        back_populates="from_"
    )

    to_chain: Mapped["EvolutionChain"] = relationship(  # type: ignore
        back_populates="to"
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self) -> str:
        return f"Evolution(id={self.id}, name={self.name}"
