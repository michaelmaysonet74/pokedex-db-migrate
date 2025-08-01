SELECT p.id,
    p.name,
    p.category,
    p.entry,
    p.generation,
    p.sprite,
    p.types,
    p.weaknesses,
    p.resistances,
    p.immunities,
    JSON_BUILD_OBJECT(
        'hp', bs.hp,
        'atk', bs.attack,
        'def', bs.defense,
        'spAtk', bs.special_attack,
        'spDef', bs.special_defense,
        'speed', bs.speed
    ) AS base_stats,
    JSON_AGG(JSON_BUILD_OBJECT(
        'name', a.name,
        'effect', a.effect,
        'isHidden', a.is_hidden
    )) AS abilities,
    JSON_BUILD_OBJECT(
        'height', m.height,
        'weight', m.weight
    ) AS measurements,
    JSON_BUILD_OBJECT(
        'from', ec.from_,
        'to', ec.to
    ) AS evolution
FROM pokemon p
    JOIN abilities a ON a.pokemon_id = p.id
    JOIN measurements m ON m.pokemon_id = p.id
    JOIN evolution_chains ec ON ec.pokemon_id = p.id
    JOIN base_stats bs ON bs.pokemon_id = p.id
GROUP BY 
    p.id,
    p.name,
    bs.hp,
    bs.attack,
    bs.defense,
    bs.special_attack,
    bs.special_defense,
    bs.speed,
    ec.from_,
    ec.to,
    m.height,
    m.weight
ORDER BY p.id
;
