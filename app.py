import dash
import dash_core_components as dcc
import dash_html_components as html
import pickle
import pandas as pd
infile = open("files/senti_prediction_NB.pickle",'rb')
data = pickle.load(infile)
infile.close()
#print('im')
x=data[data==2]

#print(x)
y=data[data==1]
z=data[data==0]
######################################
infile = open("files/CCC.pickle",'rb')
data1 = pickle.load(infile)
infile.close()
print(data1.head())
y_val=list(data1['cc_cons'])
x_val=list(data1['id'])
#print(x_val)
#print(y_val)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(children='Welcome to Iventura Platform',style={
        'textAlign': 'center',
        'color': colors['text']}),
    dcc.Graph(id='project1',
        figure={
            'data': [
                {'x ':y,'y': [1],'type': 'bar', 'name': 'Negative sentiment'},
                {'x ':z,'y':[0],'type': 'bar', 'name': 'Positive sentiment'},
                
                {'x ':x,'y': [2],'type': 'bar', 'name': 'Neutral sentiment'},
            ],
            'layout': {
                'title': 'Sentiment Analysis for drugs/medicines',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']}
            }
        }
           ),
    dcc.Graph(id='project2',
        figure={
            'data': [
                {'y': x_val,'x ':y_val,'type': 'line', 'name': 'Credit card consumption'},
                               
               
            ],
            'layout': {
                'title': 'Predict Credit card consumption',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']}
            }
        }
            )])
    


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
