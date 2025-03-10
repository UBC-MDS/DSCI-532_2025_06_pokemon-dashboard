from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

from callbacks import (
    display_about,
    update_pkmn_select_options,
    update_pkmn_card,
    create_stats_scatter,
    create_top7_histogram,
    create_type_boxplot,
    create_type_comparison
)

from components import (
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
            
            # Title
            html.Div([
                html.H1([
                    html.Span("Pokédash"),
                ]),
            
            # About Page
            html.Div([
                dcc.Location(id='url', refresh=False),
                html.Div(id='page-content')
                ])
            ], style={"textAlign": "left"}),

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
                        'height': 'fit-content',
                        'width': 'fit-content',
                        "padding": '2vh',
                        "display": "flex",
                        "justifyContent": "center",
                        "alignItems": "center",
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


# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=True)
