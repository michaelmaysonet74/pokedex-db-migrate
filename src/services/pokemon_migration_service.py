from mongo_db.pokedex_mongo_client import PokedexMongoClient
from mongo_db.models.pokemon import Pokemon as SrcPokemon
from mongo_db.models.ability import Ability as SrcAbility
from mongo_db.models.measurement import Measurement as SrcMeasurement
from psql.pokedex_psql_client import PokedexPSQLClient
from psql.models.pokemon import Pokemon
from psql.models.ability import Ability
from psql.models.measurement import Measurement


class PokemonMigrationService:
    def __init__(
        self,
        pokedex_mongo_client: PokedexMongoClient,
        podedex_psql_client: PokedexPSQLClient,
    ) -> None:
        self.pokedex_mongo_client = pokedex_mongo_client
        self.podedex_psql_client = podedex_psql_client

    async def migrate(self) -> None:
        src_pokemon = await self.pokedex_mongo_client.get_pokemon_by_id(id=1)
        sql_pokemon = self._create_pokemon(src=src_pokemon)
        self.podedex_psql_client.insert_pokemon(pokemon=sql_pokemon)

    def _create_pokemon(self, src: SrcPokemon) -> Pokemon:
        return Pokemon(
            id=src["id"],
            name=src["name"],
            abilities=self._create_abilities(src=src["abilities"]),
            category=src["category"],
            entry=src["entry"],
            generation=src["generation"],
            measurement=self._create_measurment(src=src["measurement"]),
            sprite=src["sprite"],
            types=src["types"],
            weaknesses=src["weaknesses"],
        )

    def _create_abilities(self, src: list[SrcAbility]) -> list[Ability]:
        return [
            Ability(
                name=ability["name"],
                effect=ability["effect"],
                is_hidden=ability["isHidden"],
            )
            for ability in src
        ]

    def _create_measurment(self, src: SrcMeasurement) -> Measurement:
        return Measurement(height=src["height"], weight=src["weight"])
