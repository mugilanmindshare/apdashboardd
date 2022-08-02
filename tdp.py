import gunicorn
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'tdp': 'tdp@2024'
}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
        html.Iframe(
            src='https://app.powerbi.com/view?r=eyJrIjoiOGM2MzE0NTEtODYyZC00OWM5LWI2YzAtZDhjNWZjMWE3MDE5IiwidCI6Ijk1ZmVmOGY3LWQ1NzQtNDNjYi1hYzUwLTE1NWViZDA2MTFmNSJ9&pageName=ReportSection149e1f7d5c0978f8f6e1',style={"title":"TDP Candidate Profile - TDP","width":1250,"height":650,"frameborder":0,"allowFullScreen":True})])


if __name__ == '__main__':
    app.run_server(debug=False)
