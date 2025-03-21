from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from .callbacks import (
    toggle_popup,
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
    type_advantages_bar_chart,
    title_and_about
)

app = Dash(
    __name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
    suppress_callback_exceptions=True,
    title='Pokédash'
)
server=app.server
# Layout

app.layout = dbc.Container([
    dcc.Store(id='pkmn-data'),
    dbc.Row([
        # Navigation Bar Column
        dbc.Col([
            # Title and About Section
            title_and_about,

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
                pkmn_card,
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

        ],  width=2, style={'backgroundColor': 'white', 'height': '130vh', 'display': 'flex', 'flexDirection': 'column', "padding": "2vh"}),

        dbc.Col([
            dbc.Row([
                # First Row
                dbc.Col([
                    # Left Column Top Row
                    html.Div([
                        pkmn_stats_scatterplot,
                    ], style={'padding': '1vh', 'margin': '1vh 0 0 0'})
                ], width=5),  # column width

                dbc.Col([
                    # Right Column Top Row
                    html.Div([
                        stat_distributions_boxplot,
                    ], style={'padding': '1vh', 'margin': '1vh 0 0 0'})
                ], width=5),  # Right column width
            ]),
            dbc.Row([
                # Second Row
                dbc.Col([
                    # Left Column Second Row
                    html.Div([
                        top7_pkmn_bar_chart,
                    ], style={'padding': '1vh', 'margin': '0 0 1vh 0'})
                ], width=5),  # column width
                
                dbc.Col([
                    # Right Column Second Row
                    html.Div([
                        type_advantages_bar_chart,
                    ], style={'padding': '1vh', 'margin': '0 0 1vh 0'})
                ], width=5),  # Right column width
            ])
        ])
    ], align="start")
], fluid=True, style={"height": "110vh",})

# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
