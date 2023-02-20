"""
Create dash application for user to visualise fruit taxonomy and fruit nutrition information.
Display all nutrition info as bar graph. Take input as the fruit required.
"""

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import fruits_api as fa

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.Div(
        children=[
            html.H1(
                'Fruits Information Dashboard',
                style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
            ),

            html.H2(
                'Discover the fruits that you enjoy so much!',
                style={'textAlign': 'center', 'color': '#503D36', 'font-size': 25}
            ),

            html.Br(),

            html.Div(
                children=[
                    dcc.Dropdown(
                        id='',
                        options=[],
                        value='Apple',
                        placeholder='Select your fruit here'
                    ),
                    html.Br(),
                    dcc.Dropdown(
                        id='',
                        options=[],
                        value='',
                        placeholder='Select the fruit information to view'
                    )
                ]
            ),


        ]
    )
])


@app.callback(

)
def display_fruit_table():
    """Show a table indicating the information corresponding to the fruit(s) selected by the user"""
    pass


if __name__ == "__main__":
    app.run_server(port=8052)
