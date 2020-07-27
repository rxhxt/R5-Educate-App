import _sqlite3
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots 
import plotly.graph_objects as go
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

conn = _sqlite3.connect('./r5.db',check_same_thread=False)
data = pd.read_sql('Select exam,subject,score from studentrecords',conn)
#print(data)
total_rows = len(data.axes[0])
#print(total_rows)

fig=px.bar(data, x="exam", y="score", color="subject", barmode="group")
app.layout = html.Div(children=[
    html.H1('Scoresheet'),
    dcc.Graph(
        id='bar-graph',
        figure=fig
    ), 

])

if __name__ == '__main__':
    app.run_server(debug=True,port=8000)