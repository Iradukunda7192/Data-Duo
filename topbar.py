# topbar.py
import dash
from dash import html

def topbar():
    return html.Div([
        html.Nav([
            # Move the text 30 cm (about 1134 pixels) to the right
            html.A("NISR Hackton Competition", href="/home", className="navbar-brand", 
                   style={
                       "font-weight": "bold", 
                       "color": "black",
                       "margin-left": "1190px"  # Move the text 30 cm to the right
                   })
        ], 
        className="navbar navbar-expand-lg", 
        style={"background-color": "#007bff", "padding": "10px"})
    ])

