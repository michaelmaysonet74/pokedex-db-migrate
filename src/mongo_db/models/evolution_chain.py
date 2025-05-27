from mongo_db.models.evolution import Evolution

from typing import TypedDict


class EvolutionChain(TypedDict):
    from_: Evolution | None  # Use pokemon["evolution"]["from"]
    to: list[Evolution] | None
