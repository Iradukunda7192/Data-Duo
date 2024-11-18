# app.py
import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import seaborn as sns

# Import sidebar and topbar from their respective files
from sidebar import sidebar
from topbar import topbar

# Create Dash app
app = dash.Dash(__name__)

# Load your cleaned data (assuming CSV files are saved as df1.csv, df2.csv, ... for simplicity)
dfs = [pd.read_csv(f"df{i}.csv") for i in range(1, 6)]  # Load all 5 dataframes for df1, df2, df3, df4, df5

# Function to create a graph for df1
def plot_df1(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Institutional Sector'], y=df['2014 Count'], name='2014 Count', marker_color='skyblue'))
    fig.add_trace(go.Bar(x=df['Institutional Sector'], y=df['2017 Count'], name='2017 Count', marker_color='salmon'))
    fig.add_trace(go.Bar(x=df['Institutional Sector'], y=df['2023 Count'], name='2023 Count', marker_color='green'))
    
    fig.update_layout(
        barmode='group',
        title="Comparison of Establishments by Year (df1)",
        xaxis_title="Institutional Sector",
        yaxis_title="Number of Establishments",
        xaxis_tickangle=-45
    )
    return fig

# Function to create a graph for df2
def plot_df2(df):
    # Create a 2x1 subplot for df2
    fig, ax = plt.subplots(2, 1, figsize=(10, 10))

    # Bar plot for the counts
    df.set_index("Establishment Type")[["2014 Count", "2017 Count", "2020 Count", "2023 Count"]].plot(kind="bar", ax=ax[0], color=['skyblue', 'lightgreen', 'orange', 'salmon'])
    ax[0].set_title("Comparison of Establishment Counts (2014, 2017, 2020, 2023)", fontsize=16)
    ax[0].set_ylabel("Number of Establishments")
    ax[0].set_xlabel("Establishment Type")
    ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=45, ha="right")
    ax[0].legend(title="Year")
    ax[0].grid(axis="y", linestyle="--", alpha=0.7)

    # Line plot for the percentage change
    sns.lineplot(x="Establishment Type", y="Percentage Change (2020-2023)", data=df, marker="o", ax=ax[1], color="purple")
    ax[1].set_title("Percentage Change in Establishments (2020-2023)", fontsize=16)
    ax[1].set_ylabel("Percentage Change")
    ax[1].set_xlabel("Establishment Type")
    ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=45, ha="right")
    ax[1].grid(axis="y", linestyle="--", alpha=0.7)

   
    
    # Convert matplotlib figure to plotly for Dash
    fig_plotly = go.Figure()
    fig_plotly.add_trace(go.Bar(x=df['Establishment Type'], y=df['2014 Count'], name='2014 Count', marker_color='skyblue'))
    fig_plotly.add_trace(go.Bar(x=df['Establishment Type'], y=df['2017 Count'], name='2017 Count', marker_color='lightgreen'))
    fig_plotly.add_trace(go.Bar(x=df['Establishment Type'], y=df['2020 Count'], name='2020 Count', marker_color='orange'))
    fig_plotly.add_trace(go.Bar(x=df['Establishment Type'], y=df['2023 Count'], name='2023 Count', marker_color='salmon'))
    
    fig_plotly.update_layout(
        title="Comparison of Establishment Counts by Year (df2)",
        barmode="group",
        xaxis_title="Establishment Type",
        yaxis_title="Number of Establishments"
    )
    return fig_plotly

# Function to create a graph for df3
def plot_df3(df):
    # Create a bar plot for df3
    fig = go.Figure()
    fig.add_trace(go.Bar(y=df["Economic Activity"], x=df["Count"], orientation="h", name="Count", marker_color="skyblue"))
    fig.update_layout(
        title="Distribution of Establishments by Economic Activity (df3)",
        xaxis_title="Number of Establishments",
        yaxis_title="Economic Activity"
    )
    return fig

# Function to create a graph for df4
def plot_df4(df):
    # Create a bar plot for percentage change in establishments from 2020 to 2023
    fig = go.Figure()
    fig.add_trace(go.Bar(y=df["District/Province"], x=df["Change 2020-2023 (%)"], orientation="h", name="Percentage Change", marker_color="lightcoral"))
    fig.update_layout(
        title="Percentage Change in Establishments (2020 to 2023) by District/Province (df4)",
        xaxis_title="Percentage Change",
        yaxis_title="District/Province"
    )
    return fig

# Main layout of the app
app.layout = html.Div([
    topbar(),  # Add the topbar
    sidebar(),  # Add the sidebar

    # Main content (This part will be offset to the right to make room for the sidebar)
    html.Div([
        html.H1("Economic Data Dashboard", style={"text-align": "center", "margin-left": "220px"}),

        dcc.Dropdown(
            id='df-dropdown',
            options=[{'label': f'Dataframe {i}', 'value': i} for i in range(1, 6)],
            value=1,  
            style={'width': '50%', 'margin': 'auto'}
        ),

        dcc.Graph(id='data-plot', style={"margin-left": "220px"})  # Offset graph to the right to fit with the sidebar
    ], style={"margin-left": "220px"})  # Push the content to the right for the sidebar space
])

# Callback to update the plot based on selected dataframe
@app.callback(
    Output('data-plot', 'figure'),
    Input('df-dropdown', 'value')
)
def update_graph(selected_df):
    df = dfs[selected_df - 1]  # Adjust index (0-based indexing for lists)
    
    if selected_df == 1:
        fig = plot_df1(df)
    elif selected_df == 2:
        fig = plot_df2(df)
    elif selected_df == 3:
        fig = plot_df3(df)
    elif selected_df == 4:
        fig = plot_df4(df)
    else:
        fig = plot_df1(df)  # Placeholder for df5 (you can define plot_df5 similarly)
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


