from flask import Flask, json
from flask import request
from flask import redirect
from flask import session
from flask import render_template
from flask import jsonify
import mysql.connector
import configparser
from flask_cors import cross_origin

# 建立 flask 物件
app = Flask(__name__,static_folder = 'static', static_url_path='')
app.config["JSON_AS_ASCII"] = False # 回傳的 json 不要照字母排

# 讀取 ini 檔
config = configparser.ConfigParser()
config.read('config.ini')

# 連結 mysql 資料庫
sysdb = mysql.connector.connect(
    host = config["mysql"]["host"],
    user = config["mysql"]["user"],
    password = config["mysql"]["password"]
)
mycursor = sysdb.cursor()

# Back-end routes
@app.route("/")
@cross_origin()
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    pass

@app.route("/recommend")
def recommend():
    pass

@app.route("/history")
def history():
    pass

# APIs
@app.route("/api/symptoms-departments")
@cross_origin()
def symptoms_departments():
    keyword = request.args.get("keyword", None)
    query = '''
            SELECT * FROM awan_project.symptoms
            INNER JOIN awan_project.departments
            ON awan_project.symptoms.id = awan_project.departments.symptoms_id 
            WHERE symptom_name = (%s);
    '''
    mycursor.execute(query, (keyword,))
    results = mycursor.fetchall()
    data = []
    for result in results:
        data.append(
            {
                result[1]: result[4]
            }
        )

    return jsonify(data)


app.run(host="0.0.0.0", port=3000)
