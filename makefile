all:

run: 
	pipenv run python app.py
install:
	pip install pipenv
	pipenv shell
	pip install -r requirements.txt

db :
	yum install mysql

	sql -uroot -vvv -p -vvv awan_project > ./sql_scripts/test.sql