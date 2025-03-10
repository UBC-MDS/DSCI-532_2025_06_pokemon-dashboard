from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from .callbacks import (
    display_about,
    update_pkmn_select_options,
    update_pkmn_card,
    create_stats_scatter,
    create_top7_histogram,
    create_type_boxplot,
    create_type_comparison
)

from .components import (
    pkmn_dropdown,
    pkmn_card,
    generation_dropdown,
    type1_dropdown,
    type2_dropdown,
    hp_range_slider,
    attack_range_slider,
    defense_range_slider,
    sp_attack_range_slider,
    sp_defense_range_slider,
    speed_range_slider,
    pkmn_stats_scatterplot,
    top7_pkmn_bar_chart,
    stat_distributions_boxplot,
    type_advantages_bar_chart
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container([
    dbc.Row([
        # Navigation Bar Column
        dbc.Col([
            
# <<<<<<< nv-0309_multiple-files
#             # Title
#             html.Div([
#                 html.H1([
#                     html.Span("Pokédash"),
#                 ]),
            
#             # About Page
#             html.Div([
#                 dcc.Location(id='url', refresh=False),
#                 html.Div(id='about-page-content')
#                 ])
#             ], style={"textAlign": "left"}),

# =======
#             # Welcome Message
#             html.Div(
#                 [
#                     html.H1("Pokédash", className="poke-title"),
#                 ],
#             ),
            
#             html.Div([
#                     dcc.Location(id='url', refresh=False),
#                     html.Div(id='page-content', className="page-content"),
#                 ]
#             ),
            
# >>>>>>> main
            # Pokemon Dropdown
            html.Div([
                html.Div([
                    html.Div(
                        pkmn_dropdown,
                        style={'width': '100%'}
                    ),
                ]),
            ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px'}),
            
            # Pokemon Card
            html.Div([
# <<<<<<< nv-0309_multiple-files
#                 pkmn_card,
# =======
#                 dbc.Card(
#                     dbc.CardBody(
#                             [
#                                 # Pokémon Name Section
#                                 html.Div(
#                                     dbc.Row(
#                                         dbc.Col(html.H1(id='pokemon_name', style={'textAlign': 'center', 'color': 'white'})), 
#                                         justify="center", align="center"
#                                     ),
#                                 ),                                
                                
#                                 # Pokémon Image Section
#                                 html.Div(
#                                     dbc.Row(
#                                         [
#                                             dbc.Col(
#                                                 html.Img(id='pokemon_image', style={'width': '100%'}),
#                                                 md=6,
#                                                 style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'},
#                                                 className="poke-img",
#                                             ),
#                                             dbc.Col(
#                                                 dbc.Row([ 
#                                                     dbc.Col(html.Img(id='pokemon_type_1')),
#                                                     dbc.Col(html.Img(id='pokemon_type_2')) if not None else None,
#                                                 ], justify="center", align="center"),
#                                                 md=6,
#                                                 className="poke-type",
#                                             ),
#                                         ],
#                                         justify="center",
#                                         align="center",
#                                         className="g-2",
#                                     )
#                                 ),                              
                                
#                                 html.Div(
#                                     dbc.Row(
#                                         [
#                                             # Attack, Defense, and Speed
#                                             dbc.Col(
#                                                 html.Div(
#                                                     [
#                                                         html.H3(id='pokemon_attack'),
#                                                         html.P('ATK')
#                                                     ]
#                                                 )
#                                             ),
#                                             dbc.Col(
#                                                 html.Div(
#                                                     [
#                                                         html.H3(id='pokemon_defense'),
#                                                         html.P('DEF')
#                                                     ]
#                                                 )
#                                             ),
#                                             dbc.Col(
#                                                 html.Div(
#                                                     [
#                                                         html.H3(id='pokemon_speed'),
#                                                         html.P('SPD')
#                                                     ]
#                                                 )
#                                             ),
#                                         ],
#                                         justify="center", align="center",
#                                         style={'padding': '6px 0px 0px 0px'}
#                                     )
#                                 ),

#                                 # Special Attack, Special Defense Section
#                                 html.Div(
#                                     dbc.Row(
#                                         [
#                                             dbc.Col(
#                                                 html.Div(
#                                                     [
#                                                         html.H3(id='pokemon_satk'),
#                                                         html.P('Sp. ATK')
#                                                     ]
#                                                 )
#                                             ),
#                                             dbc.Col(
#                                                 html.Div(
#                                                     [
#                                                         html.H3(id='pokemon_sdef'),
#                                                         html.P('Sp. DEF')
#                                                     ]
#                                                 ),
#                                             ),
#                                             dbc.Col(
#                                                 html.Div(
#                                                     [
#                                                         html.H3(id='pokemon_hp'),
#                                                         html.P('HP')
#                                                     ]
#                                                 ),
#                                             ),
#                                         ],
#                                         justify="center", align="center",
#                                         style={'padding': '6px 0px 0px 0px'}
#                                     )
#                                 ),
                                
#                             ]
#                         ),
#                         id="pokemon_card",
#                         className="card-poke",
#                 ),
# >>>>>>> main
                ],style={
                        "width": "100%",
                        "max-width": "400px",
                        "padding": "2vh",
                        "display": "flex",
                        "flex-direction": "column",
                        "align-items": "center",
                        },
            ),

            # Generation Dropdown
            html.Div([
                html.H2("Comparison Filter"),
                generation_dropdown,
            ], style={'width': '100%','margin-bottom': '10px'}),

            # Type Dropdowns
            html.Div([
                # Type 1 Dropdown
                html.Div([
                    type1_dropdown,
                ], style={'margin-bottom': '10px'}), 
                # Type 2 Dropdown
                html.Div([
                    type2_dropdown,
                ]),
            ], style={'width': '100%'}),

            # Stats RangeSliders
            html.Div([
                # Column 1 for RangeSliders
                html.Div([
                    html.H2("HP"),
                    hp_range_slider,
                    html.Br(),            
                    html.H2("Attack"),
                    attack_range_slider,
                    html.Br(),                    
                    html.H2("Defense"),
                    defense_range_slider,
                ], style={'flex': 1, 'marginTop': '1vh'}),  # Right column

                # Column 2 for RangeSliders
                html.Div([
                    html.H2("Sp. Attack"),
                    sp_attack_range_slider,
                    html.Br(),                    
                    html.H2("Sp. Defense"),
                    sp_defense_range_slider,
                    html.Br(),
                    html.H2("Speed"),
                    speed_range_slider,
                ], style={'flex': 1, 'marginTop': '1vh'}),  # Right column
            ], style={'display': 'flex', 'marginTop': '1vh'}),  # Flex container for two columns of RangeSliders

        ],  width=2, style={'backgroundColor': 'white', 'height': '110vh', 'display': 'flex', 'flexDirection': 'column', "padding": "2vh"}),

        # First Output Column
        dbc.Col([
            # First Row
            html.Div([
                pkmn_stats_scatterplot,
            ], style={'padding': '1vh', 'margin': '1vh 0 0 0'}),

            # Second Row
            html.Div([
                top7_pkmn_bar_chart,
            ], style={'padding': '1vh', 'margin': '0 0 1vh 0'})
        ], width=5),  # column width

        # Second Output Column
        dbc.Col([
            # First Row
            html.Div([
                stat_distributions_boxplot,
            ], style={'padding': '1vh', 'margin': '1vh 0 0 0'}),

            # Second Row
            html.Div([
                type_advantages_bar_chart,
            ], style={'padding': '1vh', 'margin': '0 0 1vh 0'}),
        ], width=5)  # Right column width
    ], align="start")
], fluid=True, style={"height": "110vh",})
# <<<<<<< nv-0309_multiple-files
# =======
# index_page = html.Div([
#     dcc.Link('about', href='/page-1'),
#     html.Br()
# ])

# page_1_layout = html.Div([
#     html.H1('About Us'),
#     html.P("Pokédash is your personal Pokéguide to understand your lil pocket monster"),
#     html.P("This is an app created by Agam, Albert, Nicholas, and Shannon"),
#     html.Div(id='page-1-content'),
#     html.Br(),
#     dcc.Link('Close', href='/'),
# ])

# # Update the index
# @callback(Output('page-content', 'children'), Input('url', 'pathname'))
# def display_page(pathname):
#     if pathname == '/page-1':
#         return page_1_layout
#     else:
#         return index_page
#     # You could also return a 404 "URL not found" page here

# @callback(
#     Output("pokemon_dropdown", "options"),
#     Input("pokemon_dropdown", "search_value"),
# )
# def update_options(search_value):
#     """
#     Dynamically updates the options for the Pokemon dropdown based on the search value entered.
#     """
#     options = a.to_dict(orient="records")
#     if not search_value.capitalize():
#         raise PreventUpdate
#     return [o for o in options if search_value.capitalize() in o["label"]]

# type_color = {
#     "bug": "#A6B91A",
#     "dragon": "#6F35FC",
#     "electric": "#F7D02C",
#     "fairy": "#D685AD",
#     "fight": "#C22E28",
#     "fire": "#EE8130",
#     "flying": "#A98FF3",
#     "grass": "#7AC74C",
#     "ground": "#E2BF65",
#     "ghost": "#735797",
#     "ice": "#96D9D6",
#     "normal": "#A8A77A",
#     "poison": "#A33EA1",
#     "psychic": "#F95587",
#     "rock": "#B6A136",
#     "water": "#6390F0",
#     "dark": "#705746",
#     "steel": "#B7B7CE"
# }

# @callback(
#     Output('pokemon_image', 'src'),
#     Output('pokemon_type_1', 'src'),
#     Output('pokemon_type_2', 'src'),
#     Output('pokemon_attack', 'children'),
#     Output('pokemon_defense', 'children'),
#     Output('pokemon_speed', 'children'),
#     Output('pokemon_satk', 'children'),
#     Output('pokemon_sdef', 'children'),
#     Output('pokemon_hp', 'children'),
#     Output('pokemon_name', 'children'),
#     Output('pokemon_card', 'style'), 
#     Input('pokemon_dropdown', 'value')
# )
# def update_image(selected_pokemon_id):
#     """
#     Display image and type of selected Pokémon.
#     """
#     image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/{selected_pokemon_id}.gif"
#     selected_pokemon = df.loc[df['pokedex_number'] == selected_pokemon_id]
#     selected_pokemon_type_1 = selected_pokemon['type1'].values[0]
#     selected_pokemon_type_2 = selected_pokemon['type2'].values[0] if not pd.isna(selected_pokemon['type2'].values[0]) else None
#     type_1_path = f"/assets/types/{selected_pokemon_type_1}.png"
#     type_2_path = f"/assets/types/{selected_pokemon_type_2}.png" if selected_pokemon_type_2 else None
#     pokemon_attack = selected_pokemon['attack']
#     pokemon_defense = selected_pokemon['defense']
#     pokemon_speed = selected_pokemon['speed']
#     pokemon_satk = selected_pokemon['sp_attack']
#     pokemon_sdef = selected_pokemon['sp_defense']
#     pokemon_hp = selected_pokemon['hp']
#     pokemon_name = selected_pokemon['name']
#     pokemon_color = type_color.get(selected_pokemon_type_1.lower(), "#ffffff")
#     card_style = {"--card-color": pokemon_color}
    
#     return image_url, type_1_path, type_2_path, pokemon_attack, pokemon_defense, pokemon_speed, pokemon_satk, pokemon_sdef, pokemon_hp, pokemon_name, card_style

# @callback(
#     Output("scatter", "spec"),
#     Input("x_col", "value"),
#     Input("y_col", "value"),
#     Input("pokemon_dropdown", "value")
# )
# def create_chart(x_col, y_col, selected_pokemon_id):
#     """
#     Create scatterplot of Pokémon stats.
#     """
#     brush = alt.selection_interval()
#     click = alt.selection_point(fields=['generation'], bind='legend', empty='all')
#     base = alt.Chart(df, width="container").mark_point(
#         filled=True,
#         size=100
#     ).encode(
#         x=x_col,
#         y=y_col,
#         tooltip="name",
#         color=alt.condition(brush, 'generation', alt.value('lightgray')),
#         opacity=alt.condition(click, alt.value(0.9), alt.value(0.2))
#     ).properties(
#         height=400
#     ).add_params(brush, click)

#     selected_plot = alt.Chart(
#         df.loc[df['pokedex_number'] == selected_pokemon_id],
#         width="container"
#     ).mark_image(
#         url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png",
#         width=50,
#         height=50
#     ).encode(
#         x=x_col,
#         y=y_col,
#         tooltip="name"
#     )
#     return alt.layer(base, selected_plot).interactive().to_dict()


# def filterData(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
#                selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range):
#     """
#     Filters the Pokémon dataset based on the selected criteria for generation, types, and stat ranges.
#     """
#     # Filter by generation
#     filtered_df = df[df['generation'].isin(selected_generation)].copy()

#     # Filter by types
#     filtered_df = filtered_df[filtered_df['type1'].isin(selected_type_1)]
#     filtered_df = filtered_df[filtered_df['type2'].isin(selected_type_2)]

#     # Filter by stat ranges
#     filtered_df = filtered_df[
#         (filtered_df['hp'] >= selected_hp_range[0]) & (filtered_df['hp'] <= selected_hp_range[1])
#     ]
#     filtered_df = filtered_df[
#         (filtered_df['attack'] >= selected_attack_range[0]) & (filtered_df['attack'] <= selected_attack_range[1])
#     ]
#     filtered_df = filtered_df[
#         (filtered_df['speed'] >= selected_speed_range[0]) & (filtered_df['speed'] <= selected_speed_range[1])
#     ]
#     filtered_df = filtered_df[
#         (filtered_df['sp_defense'] >= selected_sp_defense_range[0]) & (filtered_df['sp_defense'] <= selected_sp_defense_range[1])
#     ]
#     filtered_df = filtered_df[
#         (filtered_df['sp_attack'] >= selected_sp_attack_range[0]) & (filtered_df['sp_attack'] <= selected_sp_attack_range[1])
#     ]
#     filtered_df = filtered_df[
#         (filtered_df['defense'] >= selected_defense_range[0]) & (filtered_df['defense'] <= selected_defense_range[1])
#     ]
#     return filtered_df


# def getTop7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
#             selected_attack_range, selected_speed_range, selected_sp_defense_range,
#             selected_sp_attack_range, selected_defense_range):
#     """
#     Calculate average stats for each Pokémon.
#     """
#     filtered_df = filterData(selected_generation, selected_type_1, selected_type_2, selected_hp_range, selected_attack_range,
#                              selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

#     # Sort by average stats and return top 7
#     top_7 = filtered_df[attributes].sort_values(by='average_stat', ascending=False).head(7)

#     return top_7


# @callback(
#     Output("top_7_chart", "spec"),
#     Input("pokemon_dropdown", "value"),
#     Input("generation_dropdown", "value"),
#     Input("type1_dropdown", "value"),
#     Input("type2_dropdown", "value"),
#     Input("hp_range_slider", "value"),
#     Input("attack_range_slider", "value"),
#     Input("speed_range_slider", "value"),
#     Input("sp_defense_range_slider", "value"),
#     Input("sp_attack_range_slider", "value"),
#     Input("defense_range_slider", "value")
# )
# def create_top7_histogram(selected_pokemon_id, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
#                           selected_attack_range, selected_speed_range, selected_sp_defense_range, selected_sp_attack_range,
#                           selected_defense_range):
#     """
#     Creates a bar chart displaying the top 7 Pokémon based on their average stats and highlights the selected Pokémon.
#     """
#     if not selected_generation:
#         selected_generation = list(range(1, 8))

#     if not selected_type_1:
#         selected_type_1 = [option['value'] for option in type_options]

#     if not selected_type_2:
#         selected_type_2 = [option['value'] for option in type_options]

#     # Filter the selected Pokémon based on the dropdown value
#     attributes = ['name', 'average_stat', 'hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']
#     selected_pokemon = df[df['pokedex_number'] == selected_pokemon_id][attributes]
#     top_7 = getTop7(attributes, selected_generation, selected_type_1, selected_type_2, selected_hp_range,
#                     selected_attack_range, selected_speed_range, selected_sp_defense_range, selected_sp_attack_range, selected_defense_range)

#     # If the selected Pokémon is not in the top 7, we add it
#     if selected_pokemon['name'].values[0] not in top_7['name'].values:
#         top_7 = pd.concat([top_7, selected_pokemon]).drop_duplicates(subset='name').nlargest(7, 'average_stat')  
#     else:
#         top_7 = top_7  # Keep the original top 7 if already in the list

#     # Base bar chart for the top 7 Pokémon
#     base_chart = alt.Chart(top_7, width="container", height=400).mark_bar().encode(
#         x=alt.X('average_stat', title='Average Stats'),
#         y=alt.Y('name', title='Pokémon', sort=top_7['name'].tolist()),
#         tooltip=attributes,
#         color=alt.value('steelblue')
#     )

#     # Highlight the selected Pokémon in red
#     highlight_chart = alt.Chart(selected_pokemon).mark_bar(color='red').encode(
#         x=alt.X('average_stat'),
#         y=alt.Y('name', sort=top_7['name'].tolist()),
#         tooltip=attributes
#     )

#     # Combine the base chart with the highlighted selected Pokémon
#     return alt.layer(base_chart, highlight_chart).to_dict()


# @callback(
#     Output("boxplot", "spec"),
#     Input("x_col_boxplot", "value"),
#     Input("pokemon_dropdown", "value")
# )
# def create_type_boxplot(x_col, selected_pokemon_id):
#     """
#     Creates a boxplot for a given stat (specified by `x_col`) across Pokémon types and highlights the selected Pokémon.
#     """
#     base = alt.Chart(df, width="container").mark_boxplot().encode(
#         x=x_col,   # Chosen stat
#         y="type1",   # Just type1 for now. Can be changed to accomodate dropdown of type1 or type2 later
#         color=alt.Color(
#             "type1:N",  # Categorical color encoding for types
#             scale=alt.Scale(domain=list(type_color.keys()), range=list(type_color.values())),  # Map to custom colors
#             legend=None  # Optional: Hide the legend if not needed
#             )
#     ).properties(
#         height=400
#     )
#     selected_pokemon = alt.Chart(
#         df.loc[df['pokedex_number'] == selected_pokemon_id],
#         width="container"
#     ).mark_image(
#         url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{selected_pokemon_id}.png",
#         width=50,
#         height=50
#     ).encode(
#         x=x_col,
#         y="type1",
#         tooltip="name"    # Add mark of chosen pokemon as a point in the appropriate type
#     )

#     # Return both charts (boxplot, and point of the selected Pokémon) layered together
#     return alt.layer(base, selected_pokemon).to_dict()


# # Create dataframe containing type matchup
# df2 = df[['against_bug', 'against_dark', 'against_dragon',
#           'against_electric', 'against_fairy', 'against_fight', 'against_fire',
#           'against_flying', 'against_ghost', 'against_grass', 'against_ground',
#           'against_ice', 'against_normal', 'against_poison', 'against_psychic',
#           'against_rock', 'against_steel', 'against_water', 'name']]

# # Flip the rows and columns to obtain each pokemon as an iterable
# df2 = df2.set_index("name").transpose()


# @callback(
#     Output("vstype", "spec"),
#     Input("type_matchup", "spec"),
#     Input("pokemon_dropdown", "value")
# )
# def create_type_comparison(x_col, selected_pokemon_id):
#     """
#     Creates a bar chart comparing type matchups for the selected Pokémon.
#     """

#     # Remove 'against_' from each row so the y-axis looks cleaner
#     df2.index = [col.split('_')[-1] for col in df2.index]

#     # Base Plot
#     base = alt.Chart(df2.reset_index(), width="container").mark_bar().encode(
#         x=alt.X(
#             df.loc[df['pokedex_number'] == selected_pokemon_id]['name'].to_list()[-1],
#             axis=alt.Axis(values=[0, 0.5, 1, 1.5, 2, 4],
#                           title = "Strength Against You",
#                           labelExpr="{'0': 'Immune', '0.5': '1/2x', '1': 'Neutral', '1.5': '1.5x', '2': '2x'}[datum.value]"  # Make strength labels clearer
#                           )
#                 ),
#         y=alt.Y(
#             "index", 
#             title = "Opponent Pokémon Type"
#             ),
#             color=alt.Color(
#             "index:N",  # Using the type (index) for the color encoding
#             scale=alt.Scale(domain=list(type_color.keys()), range=list(type_color.values())),  # Mapping to custom colors in type_color dict
#             legend=None 
#         ),
#         tooltip=df.loc[df['pokedex_number'] == selected_pokemon_id]['name'].to_list()[-1]
#     )
# >>>>>>> main


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
