import pandas as pd

df = pd.read_csv("data/raw/pokemon.csv")
df['generation'] = df['generation'].astype('category')
df = df.rename(columns={"against_fight": "against_fighting"})
stats_columns = ['sp_attack', 'sp_defense', 'attack', 'defense', 'hp', 'speed']
df['average_stat'] = df[stats_columns].mean(axis=1)

pkmn_labels = df[["name", "pokedex_number"]]
pkmn_labels = pkmn_labels.rename(columns={"name": "label", "pokedex_number": "value"})

type_colour = {
    "bug": "#A6B91A",
    "dragon": "#6F35FC",
    "electric": "#F7D02C",
    "fairy": "#D685AD",
    "fighting": "#C22E28",
    "fire": "#EE8130",
    "flying": "#A98FF3",
    "grass": "#7AC74C",
    "ground": "#E2BF65",
    "ghost": "#735797",
    "ice": "#96D9D6",
    "normal": "#A8A77A",
    "poison": "#A33EA1",
    "psychic": "#F95587",
    "rock": "#B6A136",
    "water": "#6390F0",
    "dark": "#705746",
    "steel": "#B7B7CE"
}

type_options = [
    {'label': 'Normal', 'value': 'normal'},
    {'label': 'Fire', 'value': 'fire'},
    {'label': 'Water', 'value': 'water'},
    {'label': 'Electric', 'value': 'electric'},
    {'label': 'Grass', 'value': 'grass'},
    {'label': 'Ice', 'value': 'ice'},
    {'label': 'Fighting', 'value': 'fighting'},
    {'label': 'Poison', 'value': 'poison'},
    {'label': 'Ground', 'value': 'ground'},
    {'label': 'Flying', 'value': 'flying'},
    {'label': 'Psychic', 'value': 'psychic'},
    {'label': 'Bug', 'value': 'bug'},
    {'label': 'Rock', 'value': 'rock'},
    {'label': 'Ghost', 'value': 'ghost'},
    {'label': 'Dragon', 'value': 'dragon'},
    {'label': 'Dark', 'value': 'dark'},
    {'label': 'Steel', 'value': 'steel'},
    {'label': 'Fairy', 'value': 'fairy'}
]

scatterplot_options = [
    {"label": "Attack", "value": "attack"},
    {"label": "Defense", "value": "defense"},
    {"label": "Special Attack", "value": "sp_attack"},
    {"label": "Special Defense", "value": "sp_defense"},
    {"label": "Speed", "value": "speed"},
    {"label": "HP", "value": "hp"},
    {"label": "Height (m)", "value": "height_m"},
    {"label": "Weight (kg)", "value": "weight_kg"},
]

# Create dataframe containing type matchup
type_effectiveness = df[['against_bug', 'against_dark', 'against_dragon',
                         'against_electric', 'against_fairy', 'against_fighting', 'against_fire',
                         'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                         'against_ice', 'against_normal', 'against_poison', 'against_psychic',
                         'against_rock', 'against_steel', 'against_water', 'name']]

# Flip the rows and columns to obtain each pokemon as an iterable
type_effectiveness = type_effectiveness.set_index("name").transpose()

### FUNCTIONS ###
def filter_data(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
               selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range):
    """
    Filters the Pokémon dataset based on the selected criteria for generation, types, and stat ranges.
    """
    # Filter by generation
    filtered_df = df[df['generation'].isin(selected_generation)].copy()

    # Filter by types
    filtered_df = filtered_df[filtered_df['type1'].isin(selected_type_1)]
    filtered_df = filtered_df[filtered_df['type2'].isin(selected_type_2)]

    # Filter by stat ranges
    filtered_df = filtered_df[
        (filtered_df['hp'] >= selected_hp_range[0]) & (filtered_df['hp'] <= selected_hp_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['attack'] >= selected_attack_range[0]) & (filtered_df['attack'] <= selected_attack_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['speed'] >= selected_speed_range[0]) & (filtered_df['speed'] <= selected_speed_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['sp_defense'] >= selected_sp_defense_range[0]) & (filtered_df['sp_defense'] <= selected_sp_defense_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['sp_attack'] >= selected_sp_attack_range[0]) & (filtered_df['sp_attack'] <= selected_sp_attack_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df['defense'] >= selected_defense_range[0]) & (filtered_df['defense'] <= selected_defense_range[1])
    ]
    return filtered_df

def get_top_7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
            selected_attack_range, selected_speed_range, selected_sp_defense_range,
            selected_sp_attack_range, selected_defense_range):
    """
    Calculate average stats for each Pokémon.
    """
    filtered_df = filter_data(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
                             selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

    # Sort by average stats and return top 7
    top_7 = filtered_df[attributes].sort_values(by='average_stat', ascending=False).head(7)

    return top_7
