from psql.models.base import Base
from psql.models.pokemon import Pokemon

from rich import print as rprint
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class PokedexPSQLClient:
    def __init__(self, uri: str) -> None:
        self.engine = create_engine(url=uri, echo=True)
        Base.metadata.create_all(self.engine)

    def insert_pokemon(self, pokemon: Pokemon) -> None:
        with Session(self.engine) as session:
            session.add(pokemon)
            session.commit()

    def get_pokemon_by_id(self, id: int) -> dict | None:
        with Session(self.engine) as session:
            pokemon = session.query(Pokemon).get(id)
            return pokemon.to_dict() if pokemon else None
