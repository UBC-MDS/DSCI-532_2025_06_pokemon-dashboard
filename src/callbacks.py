from dash import dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate
from datetime import datetime
import pandas as pd
import altair as alt

### DATA IMPORT AND PROCESSING ###
df = pd.read_csv("data/raw/pokemon.csv")
df['generation'] = df['generation'].astype('category')
stats_columns = ['sp_attack', 'sp_defense', 'attack', 'defense', 'hp', 'speed']
df['average_stat'] = df[stats_columns].mean(axis=1)

### GLOBAL VARS ###
type_color = {
    "bug": "#A6B91A",
    "dragon": "#6F35FC",
    "electric": "#F7D02C",
    "fairy": "#D685AD",
    "fight": "#C22E28",
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

### ABOUT PAGE ###
deployment_date = datetime.now().strftime('%Y-%m-%d')
index_page = html.Div([
    dcc.Link('Go to About Page', href='/page-1'),
    html.Br()
])

page_1_layout = html.Div([
    html.H1('About Page '),
    html.P("Pokédash is your personal Pokéguide to understand your lil pocket monster"),
    html.P("This is an app created by Agam, Albert, Nicholas, and Shannon"),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

@callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
)
def display_about(pathname):
    """
    This toggles the "About" page; displays the layout of
    the page based on the selected pathname.
    """
    if pathname == '/page-1':
        return page_1_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


### POKEMON DROPDOWN ###
pkmn_labels = df[["name", "pokedex_number"]]
pkmn_labels = pkmn_labels.rename(columns={"name": "label", "pokedex_number": "value"})
pkmn_labels["search"] = pkmn_labels["label"].str.lower()

@callback(
    Output("pokemon_dropdown", "options"),
    Input("pokemon_dropdown", "search_value"),
)
def update_pkmn_select_options(search_value):
    """
    Dynamically updates the options for the Pokemon dropdown based on the search value entered.
    """
    options = pkmn_labels.to_dict(orient="records")
    if not search_value.capitalize():
        raise PreventUpdate
    return [o for o in options if search_value.capitalize() in o["label"]]


### POKEMON IMAGE CARD ###
@callback(
    Output('pokemon_image', 'src'),
    Output('pokemon_type_1', 'src'),
    Output('pokemon_type_2', 'src'),
    Output('pokemon_attack', 'children'),
    Output('pokemon_defense', 'children'),
    Output('pokemon_speed', 'children'),
    Output('pokemon_satk', 'children'),
    Output('pokemon_sdef', 'children'),
    Output('pokemon_hp', 'children'),
    Output('pokemon_name', 'children'),
    Output('pokemon_card', 'style'), 
    Input('pokemon_dropdown', 'value')
)
def update_pkmn_card(selected_pokemon_id):
    """
    Display image and type of selected Pokémon.
    """
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/{selected_pokemon_id}.gif"
    selected_pokemon = df.loc[df['pokedex_number'] == selected_pokemon_id]
    selected_pokemon_type_1 = selected_pokemon['type1'].values[0]
    selected_pokemon_type_2 = selected_pokemon['type2'].values[0] if not pd.isna(selected_pokemon['type2'].values[0]) else None
    type_1_path = f"/assets/types/{selected_pokemon_type_1}.png"
    type_2_path = f"/assets/types/{selected_pokemon_type_2}.png" if selected_pokemon_type_2 else None
    pokemon_attack = selected_pokemon['attack']
    pokemon_defense = selected_pokemon['defense']
    pokemon_speed = selected_pokemon['speed']
    pokemon_satk = selected_pokemon['sp_attack']
    pokemon_sdef = selected_pokemon['sp_defense']
    pokemon_hp = selected_pokemon['hp']
    pokemon_name = selected_pokemon['name']
    pokemon_color = type_color.get(selected_pokemon_type_1.lower(), "#ffffff")
    card_style = {"--card-color": pokemon_color}
    
    return image_url, type_1_path, type_2_path, pokemon_attack, pokemon_defense, pokemon_speed, pokemon_satk, pokemon_sdef, pokemon_hp, pokemon_name, card_style


### POKEMON STATS SCATTERPLOT ###
@callback(
    Output("scatter", "spec"),
    Input("x_col", "value"),
    Input("y_col", "value"),
    Input("pokemon_dropdown", "value")
)
def create_stats_scatter(x_col, y_col, selected_pokemon_id):
    """
    Create scatterplot of Pokémon stats.
    """
    brush = alt.selection_interval()
    click = alt.selection_point(fields=['generation'], bind='legend', empty='all')
    base = alt.Chart(df, width="container").mark_point(
        filled=True,
        size=100
    ).encode(
        x=x_col,
        y=y_col,
        tooltip="name",
        color=alt.condition(brush, 'generation', alt.value('lightgray')),
        opacity=alt.condition(click, alt.value(0.9), alt.value(0.2))
    ).properties(
        height=400
    ).add_params(brush, click)

    selected_plot = alt.Chart(
        df.loc[df['pokedex_number'] == selected_pokemon_id],
        width="container"
    ).mark_image(
        url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png",
        width=50,
        height=50
    ).encode(
        x=x_col,
        y=y_col,
        tooltip="name"
    )
    return alt.layer(base, selected_plot).interactive().to_dict()

### TOP 7 POKEMON BAR CHART ###
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

def filterData(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
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

def getTop7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
            selected_attack_range, selected_speed_range, selected_sp_defense_range,
            selected_sp_attack_range, selected_defense_range):
    """
    Calculate average stats for each Pokémon.
    """
    filtered_df = filterData(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
                             selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

    # Sort by average stats and return top 7
    top_7 = filtered_df[attributes].sort_values(by='average_stat', ascending=False).head(7)

    return top_7

@callback(
    Output("top_7_chart", "spec"),
    Input("pokemon_dropdown", "value"),
    Input("generation_dropdown", "value"),
    Input("type1_dropdown", "value"),
    Input("type2_dropdown", "value"),
    Input("hp_range_slider", "value"),
    Input("attack_range_slider", "value"),
    Input("speed_range_slider", "value"),
    Input("sp_defense_range_slider", "value"),
    Input("sp_attack_range_slider", "value"),
    Input("defense_range_slider", "value")
)
def create_top7_histogram(selected_pokemon_id, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
                          selected_attack_range, selected_speed_range, selected_sp_defense_range, selected_sp_attack_range,
                          selected_defense_range):
    """
    Creates a bar chart displaying the top 7 Pokémon based on their 
    average stats and highlights the selected Pokémon.
    """
    if not selected_generation:
        selected_generation = list(range(1, 8))

    if not selected_type_1:
        selected_type_1 = [option['value'] for option in type_options]

    if not selected_type_2:
        selected_type_2 = [option['value'] for option in type_options]

    # Filter the selected Pokémon based on the dropdown value
    attributes = ['name', 'average_stat', 'hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']
    selected_pokemon = df[df['pokedex_number'] == selected_pokemon_id][attributes]
    top_7 = getTop7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
                    selected_attack_range, selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

    # If the selected Pokémon is not in the top 7, we add it
    if selected_pokemon['name'].values[0] not in top_7['name'].values:
        top_7 = pd.concat([top_7, selected_pokemon]).drop_duplicates(subset='name').nlargest(7, 'average_stat')  
    else:
        top_7 = top_7  # Keep the original top 7 if already in the list

    # Base bar chart for the top 7 Pokémon
    base_chart = alt.Chart(top_7, width="container", height=400).mark_bar().encode(
        x=alt.X('average_stat', title='Average Stats'),
        y=alt.Y('name', title='Pokémon', sort=top_7['name'].tolist()),
        tooltip=attributes,
        color=alt.value('steelblue')
    )

    # Highlight the selected Pokémon in red
    highlight_chart = alt.Chart(selected_pokemon).mark_bar(color='red').encode(
        x=alt.X('average_stat'),
        y=alt.Y('name', sort=top_7['name'].tolist()),
        tooltip=attributes
    )

    # Combine the base chart with the highlighted selected Pokémon
    return alt.layer(base_chart, highlight_chart).to_dict()


### STAT DISTRIBUTIONS BOX PLOT ###
@callback(
    Output("boxplot", "spec"),
    Input("x_col_boxplot", "value"),
    Input("pokemon_dropdown", "value")
)
def create_type_boxplot(x_col, selected_pokemon_id):
    """
    Creates a boxplot for a given stat (specified by `x_col`) across Pokémon types and highlights the selected Pokémon.
    """
    base = alt.Chart(df, width="container").mark_boxplot().encode(
        x=x_col,   # Chosen stat
        y="type1",   # Just type1 for now. Can be changed to accomodate dropdown of type1 or type2 later
        color=alt.Color(
            "type1:N",  # Categorical color encoding for types
            scale=alt.Scale(domain=list(type_color.keys()), range=list(type_color.values())),  # Map to custom colors
            legend=None  # Optional: Hide the legend if not needed
            )
    ).properties(
        height=400
    )
    selected_pokemon = alt.Chart(
        df.loc[df['pokedex_number'] == selected_pokemon_id],
        width="container"
    ).mark_image(
        url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png",
        width=50,
        height=50
    ).encode(
        x=x_col,
        y="type1",
        tooltip="name"    # Add mark of chosen pokemon as a point in the appropriate type
    )

    # Return both charts (boxplot, and point of the selected Pokémon) layered together
    return alt.layer(base, selected_pokemon).to_dict()


### TYPE ADVANTAGES BAR CHART ###
# Create dataframe containing type matchup
type_effectiveness = df[['against_bug', 'against_dark', 'against_dragon',
                         'against_electric', 'against_fairy', 'against_fight', 'against_fire',
                         'against_flying', 'against_ghost', 'against_grass', 'against_ground',
                         'against_ice', 'against_normal', 'against_poison', 'against_psychic',
                         'against_rock', 'against_steel', 'against_water', 'name']]

# Flip the rows and columns to obtain each pokemon as an iterable
type_effectiveness = type_effectiveness.set_index("name").transpose()

@callback(
    Output("vstype", "spec"),
    Input("type_matchup", "spec"),
    Input("pokemon_dropdown", "value")
)
def create_type_comparison(x_col, selected_pokemon_id):
    """
    Creates a bar chart comparing type matchups for the selected Pokémon.
    """
    # Remove 'against_' from each row so the y-axis looks cleaner
    type_effectiveness.index = [col.split('_')[-1] for col in type_effectiveness.index]

    # Base Plot
    base = alt.Chart(type_effectiveness.reset_index(), width="container").mark_bar().encode(
        x=alt.X(
            df.loc[df['pokedex_number'] == selected_pokemon_id]['name'].to_list()[-1],
            axis=alt.Axis(values=[0, 0.5, 1, 1.5, 2, 4],
                          title = "Strength Against You",
                          labelExpr="{'0': 'Immune', '0.5': '1/2x', '1': 'Neutral', '1.5': '1.5x', '2': '2x'}[datum.value]"  # Make strength labels clearer
                          )
                ),
        y=alt.Y(
            "index", 
            title = "Opponent Pokémon Type"
            ),
            color=alt.Color(
            "index:N",  # Using the type (index) for the color encoding
            scale=alt.Scale(domain=list(type_color.keys()), range=list(type_color.values())),  # Mapping to custom colors in type_color dict
            legend=None 
        ),
        tooltip=df.loc[df['pokedex_number'] == selected_pokemon_id]['name'].to_list()[-1]
    )

    # Add plot title
    plot = alt.layer(base).configure_axis(grid=False).properties(
        title = "Pokémon Type Strength Against You"
    )
    return plot.to_dict()