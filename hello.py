import _sqlite3
import pandas as pd
import dash
from flask import Flask
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots 
import plotly.graph_objects as go
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',"./static/da_style.css"]
# server = Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

conn = _sqlite3.connect('./r5.db',check_same_thread=False)
data = pd.read_sql('Select roll_no,subject,marks from scorekids',conn)
data1=pd.read_sql('Select roll_no,status from result',conn)
#print(data)
total_rows = len(data.axes[0])
#print(total_rows)
fig = make_subplots(rows=1, cols=2)

fig=px.bar(data, x="roll_no", y="marks", color="subject", barmode="group")
fig1=px.pie(data1, values='roll_no', names='status')
app.layout = html.Div(children=[
    html.H1('Scoresheet',style={'textAlign':'center',}),
    dcc.Graph(
        id='bar-graph',
        figure=fig
    ),
    html.Hr(),
    html.H1('Pie Chart',style={'textAlign':'center','paddingTop':20}),
    dcc.Graph(
        id='pie-chart',
        figure=fig1
    ),
    
],style={'backgroundColor':'white'})

if __name__ == '__main__':
    app.run_server(debug=True)