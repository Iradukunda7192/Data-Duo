from dash import html

def sidebar():
    return html.Div([
        # Sidebar container
        html.Nav([
            # Logo at the top
            html.Div([
                html.Img(
                    src="/assets/logo.png", 
                    style={
                        "width": "200px",  # Set desired width
                        "height": "90px",  # Set desired height
                        "margin-bottom": "40px",
                        "display": "block",
                        "margin": "0 auto"
                    }
                ),
            ], style={"text-align": "center"}),  # Center the logo

            # Navigation links
            html.Ul([
                html.Li(html.A("Home", href="/home", style={"display": "block", "padding": "10px", "text-decoration": "none"})),
                html.Li(html.A("Data Analysis", href="/data-analysis", style={"display": "block", "padding": "10px", "text-decoration": "none"})),
            ], className="nav", style={"list-style": "none", "padding": "0", "margin": "0"})
        ], 
        className="sidebar", 
        style={
            "width": "200px", 
            "background-color": "#f8f9fa", 
            "padding": "10px", 
            "height": "100vh",  # Full height of the viewport
            "position": "fixed", 
            "left": "0", 
            "top": "0",
            "box-shadow": "2px 0 5px rgba(0, 0, 0, 0.1)",  # Optional: add shadow for visual separation
            "z-index": "1000"  # Make sure it's above other elements
        })
    ])
