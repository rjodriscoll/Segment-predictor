<<<<<<< HEAD
=======

from dash import html, dcc
import plotly.express as px
>>>>>>> 2f3ba9daf5448020ba2afa3e30cd5d6b369e40d9
from dash import Dash, dcc, html, Input, Output
import os


<<<<<<< HEAD
=======



>>>>>>> 2f3ba9daf5448020ba2afa3e30cd5d6b369e40d9
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

<<<<<<< HEAD
app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'
=======
app.layout = html.Div(
    [
        dcc.Input(
            id="input_{}".format("text"),
            type="text",
            placeholder="input type {}".format("text"),
        )
    ]
    + [html.Div(id="Input")]
)

@app.callback(
    Output("out-all-types", "children"),
    Input("input_{}".format("text"), "value"),
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))
>>>>>>> 2f3ba9daf5448020ba2afa3e30cd5d6b369e40d9

if __name__ == '__main__':
    app.run_server(debug=True)