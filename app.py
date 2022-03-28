from dash import Dash, dcc, html, Input, Output
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Strava segment predictor'),
    html.P("This app will take the segment id of a strava segment and estimate the time it takes to complete it across a range of w/kg values."),
    dcc.Input(id="Segment id", type="text", placeholder="enter a segment id", style={'marginRight':'10px'}),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)