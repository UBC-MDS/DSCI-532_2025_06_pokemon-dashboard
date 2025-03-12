import pandas as pd
import os
import requests

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

def get_latest_deployment_date():
    try:
        # Get the latest commit SHA from Render's environment variable
        commit_sha = os.getenv("RENDER_GIT_COMMIT")

        if commit_sha:
            # Fetch the commit date from GitHub
            repo_owner = "UBC-MDS"
            repo_name = "DSCI-532_2025_06_pokemon-dashboard"
            url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{commit_sha}"
            
            response = requests.get(url)
            if response.status_code == 200:
                commit_data = response.json()
                return commit_data["commit"]["committer"]["date"]
        
        return "Deployment date unavailable"

    except Exception as e:
        return f"Error fetching deployment date: {str(e)}"
    
deployment_date = get_latest_deployment_date()
