from psql.models.base import Base
from psql.models.pokemon import Pokemon
from psql.models.ability import Ability
from psql.models.measurement import Measurement

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, selectinload


class PokedexPSQLClient:
    def __init__(self, uri: str) -> None:
        self.engine = create_engine(url=uri, echo=True)
        Base.metadata.create_all(self.engine)

    def insert_pokemon(self, pokemon: Pokemon) -> None:
        with Session(self.engine) as session:
            session.add(pokemon)
            session.commit()

    def get_pokemon_by_id(self, id: int) -> Pokemon | None:
        with Session(self.engine) as session:
            stmt = (
                select(Pokemon)
                .options(
                    selectinload(Pokemon.abilities),
                    selectinload(Pokemon.measurement),
                )
                .where(Pokemon.id == id)
            )
            return session.execute(stmt).scalar_one_or_none()
