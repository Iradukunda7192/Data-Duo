from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from sidebar import sidebar
import matplotlib
matplotlib.use('Agg')  # Use the non-GUI backend for matplotlib
import matplotlib.pyplot as plt

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Assuming df7 is already defined somewhere in your code, like this:
# df7 = pd.DataFrame({
#     "Registration Level": ["Sector", "District", "Rwanda cooperative Agency (RCA)", "Private sector Federation (PSF)"],
#     "Total": [261549.0, 261549.0, 2286.0, 253016.0],
#     "Registered": [194332.0, 185496.0, 1193.0, 28389.0],
#     "Percentage": [74.23, 70.90, 52.20, 11.20]
# })

# Create the figure (using matplotlib to save the plot as an image)
def create_plot(df):
    plt.figure(figsize=(10, 6))
    plt.barh(df["Registration Level"], df["Percentage"], color="teal")
    plt.title("Percentage of Enterprises Registered at Different Levels", fontsize=16)
    plt.xlabel("Percentage")
    plt.ylabel("Registration Level")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()

    # Save the plot to the "assets" folder
    plt.savefig("assets/registration_level_percentage.png")
    plt.close()  # Close the plot to avoid memory issues

# Define the layout of the app (including topbar, sidebar, and page content)
app.layout = html.Div([
    sidebar(),  # Sidebar with navigation
    dcc.Location(id="url", refresh=False),  # Location to handle URL changes
    html.Div([  # Main content area
        html.Div(id="page-content", children=[
            # Display the plot image saved in the assets folder
            html.H1("Registration Levels vs Percentage", style={"text-align": "center"}),
            html.Img(src="/assets/registration_level_percentage.png", style={"width": "100%", "height": "auto"}),
            dcc.Interval(id='interval-update', interval=5*1000, n_intervals=0)  # Update every 5 seconds
        ])
    ], style={"margin-left": "200px", "padding": "20px"})
])

# Callback to update the image every 5 seconds (or on button click, etc.)
@app.callback(
    Output('page-content', 'children'),
    Input('interval-update', 'n_intervals')
)
def update_image(n_intervals):
    # Update the data (simulating a change in the Percentage column here)
    df7["Percentage"] = np.random.randint(50, 100, size=len(df7))  # Example of data update

    # Recreate and save the plot with the updated data
    create_plot(df7)

    # Return the updated image in the layout
    return [
        html.H1("Registration Levels vs Percentage", style={"text-align": "center"}),
        html.Img(src="/assets/registration_level_percentage.png", style={"width": "100%", "height": "auto"})
    ]

if __name__ == "__main__":
    app.run_server(debug=True)



