from mongo_db.models.pokemon import Pokemon

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection


class PokedexMongoClient:
    def __init__(self, uri: str | None) -> None:
        if uri is None:
            raise ValueError("Database URI must be provided")

        client: AsyncMongoClient = AsyncMongoClient(uri)
        self.client = client

        database = client.get_database("pokedex")
        self._pokemon: AsyncCollection[Pokemon] = database.get_collection("pokemon")

    async def get_pokemon_by_id(self, id: int) -> Pokemon | None:
        query = {"id": id}
        return await self._pokemon.find_one(query)

    async def get_pokemon_by_generation(self, generation: int) -> list[Pokemon]:
        query = {"generation": generation}
        return await self._pokemon.find(query).to_list(length=None)
