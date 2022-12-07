import json
from pprint import pprint

from flask import (Flask, current_app, g, redirect, render_template, request,
                   url_for)

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/show_json")
def show_json():
    with open('./templates/results.json') as f:
        df = json.load(f)
    file =open('./templates/test.json','w')
    
    sum_kill,sum_death,sum_assist=0,0,0
    df_team = df[124]['data']['vsHistoryDetail']
    
    for i in range(len(df_team['myTeam']['players'])):
        
        df_team['myTeam']['players'][i].pop('clothingGear')
        df_team['myTeam']['players'][i].pop('headGear')
        df_team['myTeam']['players'][i].pop('shoesGear')
        df_team['myTeam']['players'][i].pop('nameplate')
    
    pprint(df_team,stream=file)
    file.close()
    return render_template("show_json.html",df=df,sum_kill=sum_kill,sum_death=sum_death,sum_assist=sum_assist)


