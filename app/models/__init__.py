import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

try:
    con = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'), password=os.getenv('PASSWORD'), database=os.getenv('DATABASE'))
    con.autocommit=True
    cur = con.cursor(dictionary=True)
    #print("connected successfully")
except Exception as e:
    print("error - ",e)
    
    
    
    