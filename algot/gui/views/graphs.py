# Third Party Imports
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import random

# Local Imports
from gui.app import app

colors = {
    'bg': '#000000',
    'pie_chart': ['#07BEB8','#3DCCC7','#68D8D6','#9CEAEF']
}

pie_data = {
    'FNV': 189.25,
    'SAND': 120.86,
    'GOOG': 215.89,
    'QQQ': 286.14
}

scatter_data = {
    '1': 20,
    '2': 21.2,
    '3': 21.3,
    '4': 22.1,
    '5': 22,
    '6': 22.5,
    '7': 22.9,
    '8': 23.4,
    '9': 23.5,
    '10': 23.2,
    '11': 23.1,
    '12': 23.5,
}

# def _update_pie_chart_layout(fig):
#     fig = fig.update_layout(
#         title={
#             'text': 'Investment Spread',
#             'x': 0.5,
#             'xanchor': 'center',
#             'yanchor': 'top'
#         },
#         # width=400, 
#         # height=400,
#         autosize=True,
#         paper_bgcolor='rgba(0,0,0,0)',
#         showlegend=False
#     )
#     fig = fig.update_traces(marker=dict(colors=colors['pie_chart'], line=dict(color='#ffffff', width=2)))

#     return fig

@app.callback(
    Output('home-chart', 'figure'),
    [Input('app-interval', 'n_intervals')])
def update_home_subplot(n):
    pie_data['FNV'] += 1
    scatter_data['12'] += .1
    fig = make_subplots(rows=2, cols=1, specs=[[{'type':'domain'}],[{'type':'xy'}]])
    fig.add_trace(go.Pie(labels=list(pie_data.keys()), values=list(pie_data.values()), hole=.3),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(scatter_data.keys()), y=list(scatter_data.values())),row=2,col=1)
    # fig = fig.update_traces(marker=dict(colors=colors['pie_chart']))
    fig = fig.update_layout(
        title={
            'text': 'Investment Spread',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(
            l=30,
            r=30,
            b=0,
            t=50
        ),
        autosize=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False
    )

    return fig


# @app.callback(Output('pie-chart', 'figure'),
#                 [Input('app-interval', 'n_intervals')])
# def update_investement_spread(n):
#     pie_data['FNV'] += 1
#     fig = go.Figure(data=[go.Pie(labels=list(pie_data.keys()), values=list(pie_data.values()), hole=.3)])
#     fig = _update_pie_chart_layout(fig)
    
#     return fig

# @app.callback(Output('scatter-chart', 'figure'),
#                 [Input('app-interval', 'n_intervals')])
# def update_investement_return(n):
#     scatter_data['12'] += .1
#     fig = go.Figure(data=go.Scatter(x=list(scatter_data.keys()), y=list(scatter_data.values())))
#     fig = fig.update_layout(
#         title={
#             'text': 'Investment Spread',
#             'x': 0.5,
#             'xanchor': 'center',
#             'yanchor': 'top'
#         },
#         margin=dict(
#             l=0,
#             r=0,
#             b=0,
#             t=0
#         ),
#         # width=400, 
#         # height=400,
#         autosize=True,
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         showlegend=False
#     )

#     return fig 