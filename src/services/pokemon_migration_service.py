from mongo_db.pokedex_mongo_client import PokedexMongoClient
from mongo_db.models.pokemon import Pokemon as SrcPokemon
from mongo_db.models.ability import Ability as SrcAbility
from mongo_db.models.base_stats import BaseStats as SrcBaseStats
from mongo_db.models.evolution import Evolution as SrcEvolution
from mongo_db.models.evolution_chain import EvolutionChain as SrcEvolutionChain
from mongo_db.models.measurement import Measurement as SrcMeasurement
from psql.pokedex_psql_client import PokedexPSQLClient
from psql.models.pokemon import Pokemon
from psql.models.ability import Ability
from psql.models.base_stats import BaseStats
from psql.models.evolution_chain import EvolutionChain
from psql.models.measurement import Measurement

LATEST_GENERATION: int = 9


class PokemonMigrationService:

    def __init__(
        self,
        pokedex_mongo_client: PokedexMongoClient,
        podedex_psql_client: PokedexPSQLClient,
    ) -> None:
        self.pokedex_mongo_client = pokedex_mongo_client
        self.podedex_psql_client = podedex_psql_client

    async def migrate(self) -> None:
        for gen in range(1, LATEST_GENERATION + 1):
            src_pokemon_list = sorted(
                await self.pokedex_mongo_client.get_pokemon_by_generation(gen),
                key=lambda pokemon: pokemon["id"],
            )
            for src_pokemon in src_pokemon_list:
                if src_pokemon != None:
                    sql_pokemon = self._create_pokemon(src=src_pokemon)
                    self.podedex_psql_client.insert_pokemon(pokemon=sql_pokemon)

    def _create_pokemon(self, src: SrcPokemon) -> Pokemon:
        return Pokemon(
            id=src["id"],
            name=src["name"],
            abilities=self._create_abilities(src=src["abilities"]),
            base_stats=self._create_base_stats(src=src["baseStats"]),
            category=src["category"],
            entry=src["entry"],
            evolution=self._create_evolution_chain(src=src["evolution"]),
            generation=src["generation"],
            measurement=self._create_measurment(src=src["measurement"]),
            sprite=src["sprite"],
            types=src["types"],
            immunities=src["immunities"],
            resistances=src["resistances"],
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

    def _create_base_stats(self, src: SrcBaseStats) -> BaseStats:
        return BaseStats(
            hp=src["hp"],
            attack=src["attack"],
            defense=src["defense"],
            special_attack=src["specialAttack"],
            special_defense=src["specialDefense"],
            speed=src["speed"],
        )

    def _create_evolution_chain(self, src: SrcEvolutionChain) -> EvolutionChain:
        return EvolutionChain(
            from_=self._create_evolution(src["from"]) if src["from"] else None,  # type: ignore
            to=(
                [self._create_evolution(evolution) for evolution in src["to"]]
                if src["to"]
                else None
            ),
        )

    def _create_evolution(self, src: SrcEvolution) -> dict:
        return {
            "id": int(src["id"]),
            "name": src["name"],
        }

    def _create_measurment(self, src: SrcMeasurement) -> Measurement:
        return Measurement(height=src["height"], weight=src["weight"])
