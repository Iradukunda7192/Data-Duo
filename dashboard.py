import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

# Import sidebar and topbar from their respective files
from sidebar import sidebar
from topbar import topbar

# Create Dash app
app = dash.Dash(__name__)

# Load your cleaned data (assuming CSV files are saved as df1.csv, df2.csv, ... for simplicity)
dfs = [pd.read_csv(f"df{i}.csv") for i in range(1, 6)]  # Load all 5 dataframes for df1, df2, df3, df4, df5
df7 = pd.read_csv("df7_cleaned.csv")  # Load df7 separately

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
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Establishment Type'], y=df['2014 Count'], name='2014 Count', marker_color='skyblue'))
    fig.add_trace(go.Bar(x=df['Establishment Type'], y=df['2017 Count'], name='2017 Count', marker_color='lightgreen'))
    fig.add_trace(go.Bar(x=df['Establishment Type'], y=df['2020 Count'], name='2020 Count', marker_color='orange'))
    fig.add_trace(go.Bar(x=df['Establishment Type'], y=df['2023 Count'], name='2023 Count', marker_color='salmon'))
    
    fig.update_layout(
        title="Comparison of Establishment Counts by Year (df2)",
        barmode="group",
        xaxis_title="Establishment Type",
        yaxis_title="Number of Establishments"
    )
    return fig

# Function to create a graph for df3
def plot_df3(df):
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
    fig = go.Figure()
    fig.add_trace(go.Bar(y=df["District/Province"], x=df["Change 2020-2023 (%)"], orientation="h", name="Percentage Change", marker_color="lightcoral"))
    fig.update_layout(
        title="Percentage Change in Establishments (2020 to 2023) by District/Province (df4)",
        xaxis_title="Percentage Change",
        yaxis_title="District/Province"
    )
    return fig

# Function to create a graph for df5
def plot_df5(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Region'], y=df['Establishment Growth'], marker_color='gold', name='Establishment Growth'))

    fig.update_layout(
        title="Percentage of Enterprises Registered at Different Levels (df5)",
        xaxis_title="Percentage",
        yaxis_title="Region",
        xaxis_tickangle=-45
    )
    return fig

# Function to create a graph for df7
def plot_df7(df):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=df["Registration Level"], x=df["Percentage"], orientation="h", marker_color="teal", name="Percentage"
    ))

    fig.update_layout(
        title="Percentage of Enterprises Registered at Different Levels (df7)",
        xaxis_title="Percentage",
        yaxis_title="Registration Level",
        xaxis=dict(showgrid=True, gridcolor="lightgrey"),
        yaxis=dict(showgrid=False),
        template="plotly_white",
    )
    return fig

# Main layout of the app
app.layout = html.Div([
    topbar(),  # Add the topbar
    sidebar(),  # Add the sidebar

    # Main content (This part will be offset to the right to make room for the sidebar)
    html.Div([
        html.H1("Economic Data Dashboard", style={"text-align": "center", "margin-left": "300px"}),

        dcc.Dropdown(
            id='df-dropdown',
            options=[
                {'label': f'Dataset {i}', 'value': i} for i in range(1, 6)
            ] + [{'label': ' Registration Levels', 'value': 'df7'}],  # Add df7 as an option
            value=1,  # Default value
            style={'width': '50%', 'margin': 'auto'}
        ),

        dcc.Graph(id='data-plot', style={"margin-left": "500px"})  # Offset graph to the right to fit with the sidebar
    ], style={"margin-left": "200px"})  # Push the content to the right for the sidebar space
])

# Callback to update the plot based on selected dataframe
@app.callback(
    Output('data-plot', 'figure'),
    Input('df-dropdown', 'value')
)
def update_graph(selected_df):
    # Check if the selected dataset is df7
    if selected_df == "df7":
        fig = plot_df7(df7)
    else:
        # Otherwise select from the list of datasets
        df = dfs[selected_df - 1]  # Adjust index for 0-based indexing
        if selected_df == 1:
            fig = plot_df1(df)
        elif selected_df == 2:
            fig = plot_df2(df)
        elif selected_df == 3:
            fig = plot_df3(df)
        elif selected_df == 4:
            fig = plot_df4(df)
        elif selected_df == 5:
            fig = plot_df5(df)
        else:
            fig = go.Figure()  # Empty placeholder figure

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
