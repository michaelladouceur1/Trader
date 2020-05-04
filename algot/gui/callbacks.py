from dash.dependencies import Input, Output

from gui.app import app

@app.callback(Output('app-interval', 'interval'),
                [Input('refresh-slider', 'value')])
def update_app_interval(value):
    return value*1000