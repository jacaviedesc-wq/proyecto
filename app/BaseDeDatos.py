import MySQLdb
from flask import Flask
from flask_mysqldb import MySQL

class ConfiguracionBD:
    def __init__(self, app):
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'Margareth20071227.'
        app.config['MYSQL_DB'] = 'db_ecorisk'
        #app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Para recibir resultados como diccionarios

        self.mysql = MySQL(app)

    def get_cursor(self, dict_cursor=True):
        if dict_cursor:
            return self.mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        else:
            return self.mysql.connection.cursor()
