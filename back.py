import sqlite3
import mysql.connector
import sys

def enter(login,password):

    
    try:
        dbase = mysql.connector.connect(
            host = "localhost",
            #username and password of your db connection
            user = str(login),
            password = str(password),
            database = "db_gerenciador"
        )

        return dbase
    except:
        #print (sys.exc_info())
        return None

def selectData(con):

    c = con.cursor()

    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS tb_user_login (
	    usl_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	    usl_service VARCHAR(45) NOT NULL,
	    usl_login	VARCHAR(45) NOT NULL,
	    usl_password VARCHAR(32) NOT NULL
        );
        '''
    )

    con.commit()

    selectLogins = ''' SELECT * FROM tb_user_login '''

    c.execute(selectLogins)

    resultLogins = c.fetchall()

    return resultLogins


def insertLogin(con, service, login, password):

    c = con.cursor()

    insert = '''INSERT INTO tb_user_login (usl_service, usl_login, usl_password) VALUES 
    ("'''+service+'''","'''+login+'''", "'''+password+'''") '''

    c.execute(insert)
    con.commit()

def delete(con, idd):

    c = con.cursor()

    insert = '''DELETE tb_user_login FROM tb_user_login WHERE usl_id = {}  '''.format(idd)

    c.execute(insert)
    con.commit()
