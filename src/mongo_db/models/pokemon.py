from mongo_db.models.ability import Ability
from mongo_db.models.base_stats import BaseStats
from mongo_db.models.evolution_chain import EvolutionChain
from mongo_db.models.measurement import Measurement

from typing import TypedDict


class Pokemon(TypedDict):
    id: int
    name: str
    abilities: list[Ability]
    baseStats: BaseStats
    category: str
    entry: str
    evolution: EvolutionChain
    generation: int
    measurement: Measurement
    sprite: str
    types: list[str]
    immunities: list[str]
    resistances: list[str]
    weaknesses: list[str]
