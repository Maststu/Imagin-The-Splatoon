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

@app.route("/show_winrate",methods=["GET","POST"])
def show_winrate():
    with open('./templates/results.json') as f:
        df = json.load(f)
    
    if request.method == 'POST':
        weapon=request.form['weapon']
    else:
        weapon =request.args.get('weapon','all')
        
        
    return render_template("show_winrate.html",df=df,weapon=weapon)

@app.route('/name_search',methods=["GET","POST"])
def name_search():
    with open('./templates/results.json') as f:
        df = json.load(f)
    
    if request.method == 'POST':
        username = request.form['username']
    else:
        username = request.args.get('username', 'noname')
    return render_template("name_search.html", df=df, username=username)




@app.route('/config',methods=["POST"])
def config():
    return request.form.get('user')
    

@app.route("/show_json")
def show_json():
    with open('./templates/results.json') as f:
        df = json.load(f)
    file=open('./templates/test.json','w')
    df_team = df[124]['data']['vsHistoryDetail']
    
    for i in range(len(df_team['myTeam']['players'])):
        
        df_team['myTeam']['players'][i].pop('clothingGear')
        df_team['myTeam']['players'][i].pop('headGear')
        df_team['myTeam']['players'][i].pop('shoesGear')
        df_team['myTeam']['players'][i].pop('nameplate')
    file.write(json.dumps(df_team,sort_keys=True,indent=4))    
    file.close()
    return render_template("show_json.html",df=df)

@app.route("/show_all_json")
def show_all_json():
    with open('./templates/all.json') as f:
        df = json.load(f)
    
    df_player = df['data']['vsHistoryDetail']['myTeam']['players']
    
    return render_template("show_all_json.html",df=df_player)
    return "hello"

