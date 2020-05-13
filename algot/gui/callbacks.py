# Third Party Imports
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Local Imports
from gui.app import app
from gui.serve import Serve

server = Serve()

# Set app interval

@app.callback(Output('app-interval', 'interval'),
                [Input('settings-local-store', 'data')])
def get_app_interval(data):
    if data is None:
        raise PreventUpdate
    return data['refresh_slide']*1000


# Data Input

@app.callback(Output('settings-local-store', 'data'),
                [Input('refresh-slider', 'value')])
def update_app_interval(value):
    if value is None:
        raise PreventUpdate
    return {'refresh_slide': value}


# Data Loading

@app.callback(Output('refresh-slider', 'value'),
                [Input('nav-bar', 'value')],
                [State('settings-local-store', 'data')])
def load_settings_data(value, data):
    # print(data)
    if value == 'settings':
        return data['refresh_slide']


# Securities

@app.callback(Output('local-security-modal', 'is_open'),
                [Input('local-security-modal-button', 'n_clicks')],
                [State('local-security-modal', 'is_open')])
def open_local_security_modal(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

@app.callback(Output('local-security-dropdown', 'value'),
                [Input('local-security-button', 'n_clicks')],
                [State('local-security-dropdown', 'value'),
                State('local-security-slider', 'value')])
def save_security(n_clicks, dropdown_value, slider_value):
    if n_clicks:
        server.save_security_local(symbols=dropdown_value, period=slider_value)
        return None