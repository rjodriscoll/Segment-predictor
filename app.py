
from dash import html, dcc
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import os





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

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

if __name__ == '__main__':
    app.run_server(debug=True)