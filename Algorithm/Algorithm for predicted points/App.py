from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def get_data(file):
    return pd.read_csv(file).to_dict(orient="records")



@app.route("/")
def home():
    week1 = pd.read_csv('gameweek1.csv').to_dict(orient='records')
    week2= pd.read_csv('gameweek2.csv').to_dict(orient='records')
    return render_template("index.html", week1=week1, week2=week2)


if __name__ == "__main__":
    app.run(debug=True)


