from typing import TypedDict


class BaseStats(TypedDict):
    hp: int
    attack: int
    defense: int
    specialAttack: int
    specialDefense: int
    speed: int
