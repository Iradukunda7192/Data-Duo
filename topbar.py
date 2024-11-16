from dash import html

def topbar():
    return html.Div([
        html.Nav([
            # Brand or Title
            html.A("NISR Hackton Competition ", href="/home", className="navbar-brand", 
                   style={"font-weight": "bold", "color": "white"}),

            
                
                    
        ], 
        className="navbar navbar-expand-lg", 
        style={"background-color": "#007bff", "padding": "10px"})
    ])
