from components.layout import layout
from dotenv import load_dotenv
import os, ast, dash_auth, dash

load_dotenv()

login = ast.literal_eval(os.environ.get("LOGIN")) 

app = dash.Dash(__name__)

auth = dash_auth.BasicAuth(app, login)

app.title = "YH-statistik"
app.layout = layout

server = app.server

if __name__ == "__main__":
    app.run_server(debug = True, host = "0.0.0.0", port = 80)
