# data_analysis.py
from dash import html, dcc
import pandas as pd

def data_analysis_page():
    return html.Div([
        html.H1("Data Analysis", style={"text-align": "center", "margin-top": "20px"}),

        # Display your saved image for registration level percentage
        html.Div([
            html.H2("Visualization for Registration Level Percentage"),
            html.Img(src="/assets/registration_level_percentage.png", 
                     style={"width": "100%", "height": "auto", "margin-bottom": "20px"})
        ], style={"padding": "20px"}),

        # Add a 'Return to Home' button using dcc.Link to navigate back to the home page
        html.Div([
            dcc.Link(
                html.Button("Return to Home", 
                            style={"font-size": "16px", "padding": "10px", "background-color": "#007bff", "color": "white", "border": "none", "cursor": "pointer"}),
                href="/home"  # Links to the home page
            )
        ], style={"text-align": "center", "margin-top": "20px"})
    ], style={"margin-left": "200px", "padding": "20px"})





