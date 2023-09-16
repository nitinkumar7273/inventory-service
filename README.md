# inventory-service

Migration Script to create a DB:

* Instruction to run following commands on terminal:

1. $env:FLASK_APP = "main.py"
2. flask db init

   After that update the "alembic.ini" file which is under "migrations" folder, write following lines:
   [alembic]
   sqlalchemy.url = 'mysql+pymysql://root:admin1234@127.0.0.1:3306/inventory-service'

   Notes: Here in above "sqlalchemy.url"; username = "root",
   password = "admin1234",
   url: "127.0.0.1",
   port: "3306", please update it with your current DB credentials

3. flask db migrate
4. flask db upgrade#   i n v e n t o r y - s e r v i c e  
 #   i n v e n t o r y - s e r v i c e  
 #   i n v e n t o r y - s e r v i c e  
 