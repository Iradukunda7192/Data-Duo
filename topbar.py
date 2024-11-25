# topbar.py
import dash
from dash import html, dcc, Input, Output, State

def topbar():
    return html.Div([
        html.Nav([
            html.A(
                "NISR Hackton Competition", 
                href="/home", 
                className="navbar-brand",
                style={
                    "font-weight": "bold", 
                    "color": "black",
                    "margin-left": "250px"
                }
            ),
            # Add a search bar with a button
            html.Div(
                [
                    dcc.Input(
                        id="search-bar",
                        type="text",
                        placeholder="Search...",
                        style={
                            "padding": "5px",
                            "border-radius": "5px",
                            "width": "200px",
                            "margin-left": "200px"
                        }
                    ),
                    html.Button(
                        "Search",
                        id="search-button",
                        n_clicks=0,
                        style={
                            "padding": "5px 10px",
                            "border-radius": "5px",
                            "background-color": "white",
                            "border": "1px solid #ccc",
                            "cursor": "pointer",
                            "margin-right": "200px"
                        }
                    )
                ],
                style={"margin-left": "auto", "margin-right": "200px", "display": "flex", "align-items": "center"}
            )
        ], 
        className="navbar navbar-expand-lg", 
        style={"background-color": "darkseagreen", "padding": "10px"}
        )
    ])


