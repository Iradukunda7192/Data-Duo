from dash import html

def sidebar():
    return html.Div([
        html.Nav([
            html.Div([
                html.Img(
                    src="/assets/logo.png", 
                    style={
                        "width": "200px",  
                        "height": "90px",  
                        "margin-bottom": "40px",
                        "display": "block",
                        "margin": "0 auto"
                    }
                ),
            ], style={"text-align": "center"}),  

            html.Ul([
                html.Li(html.A("Home", href="/home", style={"display": "block", "padding": "10px", "text-decoration": "none"})),
            ], className="nav", style={"list-style": "none", "padding": "0", "margin": "0"})
        ], 
        className="sidebar", 
        style={
            "width": "200px", 
            "background-color": "#f8f9fa", 
            "padding": "10px", 
            "height": "100vh",  
            "position": "fixed", 
            "left": "0", 
            "top": "0",
            "box-shadow": "2px 0 5px rgba(0, 0, 0, 0.1)",  
            "z-index": "1000"
        })
    ])


