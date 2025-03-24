import pandas as pd


def get_pokedex_entry(df, poke_name):
    pokemon = df["name"].str.lower() == poke_name.lower()
    if not pokemon.any():
        print(f"No Pókemon with the name '{poke_name}' found.")
        return

    pkmn = df[pokemon].squeeze()
    print(f"Pokédex Entry #{pkmn.pokedex_number}")
    print("=" * 30)
    print(f"Name: {pkmn['name']}")
    print(f"Type: {pkmn.type1}" +
          (f" / {pkmn.type2}" if not pd.isna(pkmn.type2) else ""))
    print(f"HP: {pkmn.hp}")
    print(f"Attack: {pkmn.attack}")
    print(f"Defense: {pkmn.defense}")
    print(f"Speed: {pkmn.speed}")
    print(f"Sp. Atk: {pkmn.sp_attack}")
    print(f"Sp. Def: {pkmn.sp_defense}")
    print("=" * 30)
