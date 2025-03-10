from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

### DATA ###
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

### COMPONENTS ###
pkmn_dropdown = dcc.Dropdown(id="pokemon_dropdown", search_value="Pikachu", value=25, clearable=False)

pkmn_card = dbc.Card(
    dbc.CardBody(
            [
                # Pokémon Name Section
                html.Div(
                    dbc.Row(
                        dbc.Col(html.H1(id='pokemon_name', style={'textAlign': 'center', 'color': 'white'})), 
                        justify="center", align="center"
                    ),
                ),                                
                
                # Pokémon Image Section
                html.Div(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(id='pokemon_image', style={'width': '100%'}),
                                width=6,
                                style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'},
                                className="poke-img",
                            ),
                            dbc.Col(
                                dbc.Row([ 
                                    dbc.Col(html.Img(id='pokemon_type_1')),
                                    dbc.Col(html.Img(id='pokemon_type_2')) if not None else None,
                                ], justify="center", align="center") ,
                                className="poke-type",
                            ),
                        ],
                        justify="center",
                        align="center",
                    )
                ),                              
                
                html.Div(
                    dbc.Row(
                        [
                            # Attack, Defense, and Speed
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H2(id='pokemon_attack'),
                                        html.P('Attack')
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H2(id='pokemon_defense'),
                                        html.P('Defense')
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H2(id='pokemon_speed'),
                                        html.P('Speed')
                                    ]
                                )
                            ),
                        ],
                        justify="center", align="center", 
                        style={'padding': '20px 0px 0px 0px'}
                    )
                ),

                # Special Attack, Special Defense Section
                html.Div(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H2(id='pokemon_satk'),
                                        html.P('Special Attack')
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H2(id='pokemon_sdef'),
                                        html.P('Special Defense')
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H2(id='pokemon_hp'),
                                        html.P('HP')
                                    ]
                                )
                            ),
                        ],
                        justify="center", align="center",
                        style={'padding': '20px 0px 0px 0px'}
                    )
                ),
                
            ]
        ),
        id="pokemon_card",
        className="card-poke",
)

generation_dropdown = dcc.Dropdown(
                    id="generation_dropdown",
                    options=[{'label': str(i), 'value': i} for i in range(1, 8)],  # Generations 1 to
                    multi=True,
                    placeholder="Select Generation(s)",
                    value=[1, 3, 5],
                    style={'width': '100%'}
                )

type1_dropdown = dcc.Dropdown(
                        id="type1_dropdown",
                        className="type-dropdown-style",
                        options=type_options,
                        multi=True,
                        placeholder="Select Type 1",
                        style={'width': '100%'}
                    )

type2_dropdown = dcc.Dropdown(
                        id="type2_dropdown",
                        className="type-dropdown-style",
                        options=type_options,
                        multi=True,
                        placeholder="Select Type 2",
                        style={'width': '100%'}
                    )

hp_range_slider = dcc.RangeSlider(
                        id="hp_range_slider",
                        min=0,
                        max=255,
                        step=1,
                        value=[0, 255],
                        marks={0: '0', 255: '255'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    )

attack_range_slider = dcc.RangeSlider(
                        id="attack_range_slider",
                        min=0,
                        max=200,
                        step=1,
                        value=[0, 200],
                        marks={0: '0', 200: '200'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    )

defense_range_slider = dcc.RangeSlider(
                        id="defense_range_slider",
                        min=0,
                        max=250,
                        step=1,
                        value=[0, 250],
                        marks={0: '0', 250: '250'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    )

sp_attack_range_slider = dcc.RangeSlider(
                        id="sp_attack_range_slider",
                        min=0,
                        max=250,
                        step=1,
                        value=[0, 250],
                        marks={0: '0', 250: '250'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    )

sp_defense_range_slider = dcc.RangeSlider(
                        id="sp_defense_range_slider",
                        min=0,
                        max=250,
                        step=1,
                        value=[0, 250],
                        marks={0: '0', 250: '250'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    )

speed_range_slider = dcc.RangeSlider(
                        id="speed_range_slider",
                        min=0,
                        max=200,
                        step=1,
                        value=[0, 200],
                        marks={0: '0', 200: '200'},
                        tooltip={"placement": "bottom", "always_visible": True},
                    )

pkmn_stats_scatterplot = dbc.Card(
                    dbc.CardBody(
                        [
                            html.H2('Scatterplot: Comparing Pokémon Metrics'),
                            html.Div([
                                html.Label("x-axis metric:", style={"marginRight": "10px"}),
                                dcc.Dropdown(
                                    id="x_col",
                                    options=scatterplot_options,
                                    value="speed",
                                    clearable=False,
                                    placeholder="x-axis property",
                                    style={"minWidth": "100px", "flex": "1"},
                                ),
                                ],
                                style={"display": "flex", "alignItems": "center"},
                            ),
                            html.Div([
                                html.Label("y-axis metric:", style={"marginRight": "10px"}),
                                dcc.Dropdown(
                                    id="y_col",
                                    options=scatterplot_options,
                                    value="attack",
                                    clearable=False,
                                    placeholder="y-axis property",
                                    style={"minWidth": "100px", "flex": "1"},
                                ),
                                ],
                                style={"display": "flex", "alignItems": "center"},
                            ),
                            html.Br(),
                            dvc.Vega(id='scatter', spec={}, style={'width': '100%'}),
                        ]
                    ),
                    className="card-chart",
                )

top7_pkmn_bar_chart = dbc.Card(
                    dbc.CardBody(
                        [
                            html.H2("Comparison with Top 7 Pokémon by Avg Stats"),
                            dvc.Vega(id='top_7_chart', spec={}, style={'width': '100%'})
                        ]
                    ),
                    className="card-chart",
                )

stat_distributions_boxplot = dbc.Card(
                    dbc.CardBody(
                        [
                            html.H2('Boxplot: Examining Pokémon Stat Distributions by Type'),
                            html.Div([
                                html.Label("x-axis label:", style={"marginRight": "10px"}),
                                dcc.Dropdown(
                                    id="x_col_boxplot",
                                    options=scatterplot_options,
                                    value="speed",
                                    clearable=False,
                                    placeholder="x-axis property",
                                    style={"minWidth": "100px", "flex": "1"},
                                ),
                                ],
                                style={"display": "flex", "alignItems": "center", 'height': '100%'},
                            ),
                            html.Br(),
                            dvc.Vega(id='boxplot', spec={}, style={'width': '100%'}),
                        ]
                    ),
                    className="card-chart",
                )

type_advantages_bar_chart = dbc.Card(
                    dbc.CardBody(
                        [
                            html.H2('Type Disadvantage: Examining Pokémon Weaknesses'),
                            html.Div([
                                dvc.Vega(
                                    id="type_matchup",
                                    style={'width': '100%'},
                                ),
                                ],
                                style={"display": "flex", "alignItems": "center", 'height': '100%'},
                            ),
                            html.Br(),
                            dvc.Vega(id='vstype', spec={}, style={'width': '100%'}),
                        ]
                    ),
                    className="card-chart",
                )