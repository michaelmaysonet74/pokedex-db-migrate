from mongo_db.pokedex_mongo_client import PokedexMongoClient
from psql.pokedex_psql_client import PokedexPSQLClient
from services.pokemon_migration_service import PokemonMigrationService

import asyncio
from dotenv import load_dotenv
import os
import time

load_dotenv()


async def main():
    try:
        pokedex_mongo = PokedexMongoClient(uri=os.getenv("MONGO_DB_URI"))
        pokedex_psql = PokedexPSQLClient(uri=os.getenv("PSQL_DB_URI"))

        migration_service = PokemonMigrationService(
            pokedex_mongo_client=pokedex_mongo,
            podedex_psql_client=pokedex_psql,
        )

        await migration_service.migrate()
        await pokedex_mongo.client.close()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.2f} seconds")
