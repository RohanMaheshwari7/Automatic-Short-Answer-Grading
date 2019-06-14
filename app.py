import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


colors = {
    'background': '#ffffff',
    'text': '#111111'
}

app.layout = html.Div(

    style={'textAlign':'center',"backgroundColor":colors['background'],'height':'auto',"color":"black"},
    children=[

    html.H1(children='Hello Student'),
    html.Div(style={
        'textAlign':'center'
    },
    children='''
        Please enter your answer
    ''' ),
    html.Label('Question'),
    dcc.Input(type='text', style={"width":"25vw"}),
    html.P(style={"height":"23px"}),
    html.Label('Ref Ans'),
    dcc.Input(type='text', style={"width":"25vw"}),
    html.P(style={"height":"23px"}),
    html.Label('Stud Ans'),
    dcc.Textarea(style={"width":"25vw"}),
    html.P(style={"height":"23px"}),
    html.Button('Submit', id='button')

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
