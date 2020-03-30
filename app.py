from flask import Flask
from flask import request
from flask import  session
import mysql.connector
import link
import lala
import get

# 实例化一个Flask类，同时为app设置secret_key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dasdefaf9*&*Tfdad'


if __name__=='__main__':
    app.run()