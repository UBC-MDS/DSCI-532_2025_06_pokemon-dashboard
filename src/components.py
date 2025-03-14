from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from .data import (
    type_options,
    scatterplot_options,
    deployment_date
)

### COMPONENTS ###
pkmn_dropdown = dcc.Dropdown(id="pokemon_dropdown", search_value="", value=25, clearable=False, placeholder="Type to Select a Pokémon")

pkmn_card = dbc.Card(
    dbc.CardBody(
            [
                # Pokémon Name Section
                html.Div(
                    dbc.Row(
                        dbc.Col(html.H2(id='pokemon_name', style={'textAlign': 'center',
                                                                  'color': 'white',
                                                                  'font-size': '16px'})), 
                        justify="center", align="center"
                    ),
                ),                                
                
                # Pokémon Image Section
                html.Div(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(id='pokemon_image', style={'height': '100%'}),
                                md=6,
                                style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'},
                                className="poke-img",
                            ),
                            dbc.Col(
                                dbc.Row([ 
                                    dbc.Col(html.Img(id='pokemon_type_1')),
                                    dbc.Col(html.Img(id='pokemon_type_2')) if not None else None,
                                ], justify="center", align="center"),
                                md=6,
                                className="poke-type",
                            ),
                        ],
                        justify="center",
                        align="center",
                        className="g-2",
                    )
                ),                              
                
                # Attack, Defense, and Speed
                html.Div(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H3(id='pokemon_attack'),
                                        html.P('ATK', style={'text-align': 'center'})
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H3(id='pokemon_defense'),
                                        html.P('DEF', style={'text-align': 'center'})
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H3(id='pokemon_speed'),
                                        html.P('SPD', style={'text-align': 'center'})
                                    ]
                                )
                            ),
                        ],
                        justify="center", align="center",
                        style={'padding': '0px 0px 0px 0px', 'text-align': 'center'}
                    )
                ),

                # Special Attack, Special Defense Section
                html.Div(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H3(id='pokemon_satk'),
                                        html.P('Sp. ATK', style={'text-align': 'center'})
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H3(id='pokemon_sdef'),
                                        html.P('Sp. DEF', style={'text-align': 'center'})
                                    ]
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H3(id='pokemon_hp'),
                                        html.P('HP', style={'text-align': 'center'})
                                    ]
                                )
                            ),
                        ],
                        justify="center", align="center",
                        style={'padding': '0px 0px 0px 0px', 'text-align': 'center'}
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

title_and_about = html.Div([
    html.Img(src="/assets/pokeball.png", style={'height': '30px', 'marginRight': '5px', 'marginBottom': '10px'}),
    html.H1("Pokédash", className="poke-title"),
    html.Button('?', 
        id='about-button', 
        style={
            'borderRadius': '50%',
            'width': '30px',
            'height': '30px',
            'fontSize': '20px',
            'cursor': 'pointer',
            'marginLeft': '10px',
            'marginBottom': '10px',
            'border': 'none',
            'backgroundColor': '#f0f0f0',
            'transition': 'background-color 0.3s',
        }
    ),
    html.Div(id='about-page-content'),
], style={'display': 'flex', 'alignItems': 'center'})

def create_popup():
    """Create the about popup content with animations and overlay"""
    return html.Div([
        # Background overlay
        html.Div(
            className='popup-overlay',
            id='popup-overlay',
            n_clicks=0,
            style={
                'position': 'fixed',
                'top': 0,
                'left': 0,
                'width': '100%',
                'height': '100%',
                'backgroundColor': 'rgba(0, 0, 0, 0.5)',
                'zIndex': 999,
                'cursor': 'pointer',
                'animation': 'fade-in 0.3s ease-out forwards',
            }
        ),
        # Popup content with a close button
        html.Div([
            # Close button in the top right
            html.Button(
                "×",
                id='close-popup-button',
                n_clicks=0,
                style={
                    'position': 'absolute',
                    'right': '15px',
                    'top': '15px',
                    'fontSize': '24px',
                    'color': '#666',
                    'padding': '5px 10px',
                    'cursor': 'pointer',
                    'border': 'none',
                    'background': 'none',
                }
            ),
            html.H2('About Pokédash', style={'fontSize': '2em', 'marginBottom': '20px'}),
            html.P("Pokédash is your personal Pokéguide to understand your lil pocket monster", 
                   style={'fontSize': '1.2em', 'marginBottom': '15px'}),
            html.P("This is an app created by Agam, Albert, Nicholas, and Shannon",
                   style={'fontSize': '1.2em', 'marginBottom': '15px'}),
            html.P(f"Deployed on: {deployment_date}",
                   style={'fontSize': '1.2em'}),
        ], 
        className='popup-content',
        style={
            'position': 'fixed',
            'top': '50%',
            'left': '50%',
            'transform': 'translate(-50%, -50%)',
            'backgroundColor': 'white',
            'padding': '40px',
            'borderRadius': '10px',
            'boxShadow': '0 0 20px rgba(0,0,0,0.2)',
            'minWidth': '500px',
            'maxWidth': '80%',
            'zIndex': 1000,
            'animation': 'popup-scale-in 0.3s ease-out forwards',
        })
    ])