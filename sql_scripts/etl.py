import crawler_1 as c1
import crawler_2 as c2
import mysql.connector
import configparser
import json

# 讀取 ini 檔
config = configparser.ConfigParser()
config.read(r'../config.ini')

# 連結 mysql 資料庫
sysdb = mysql.connector.connect(
    host = config["mysql"]["host"],
    user = config["mysql"]["user"],
    password = config["mysql"]["password"]
)
mycursor = sysdb.cursor()

# 整併資料到 result2
result1 = c1.crawler()
result2 = c2.crawler()

for i in result1:
    if i not in result2:
        result2[i] = result1[i]
    else:
        result2[i] = list(set(result2[i]).union(set(result1[i])))

# 將資料匯入 DB
symptom_names = list(result2.keys())
department_names = list(result2.values())
query_insert_symptoms = "INSERT INTO awan_project.symptoms (symptom_name) VALUES (%s);"
query_insert_departments = "INSERT INTO awan_project.departments (symptoms_id, department) VALUES (%s, %s);"

for i, symptom_name in zip(range(len(symptom_names)), symptom_names):
    print("Inserting symptoms data...")
    mycursor.execute(query_insert_symptoms, (str(symptom_name),))
    print("Inserting departments data...")
    for department_name in department_names[i]:
        mycursor.execute(query_insert_departments, (i+1, str(department_name)))

sysdb.commit()
print("Done")