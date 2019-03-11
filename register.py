#!/usr/bin/python3

from flask import Flask,render_template,request
import imaplib
import numpy as np
import email
from bs4 import BeautifulSoup
import getpass

import mysql.connector as mariadb
import smtplib
from email.mime.text import MIMEText


from flask import Flask,render_template,request,session
import mysql.connector as mariadb


def register_page():
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		name = request.form['name']
		email = request.form['email']
		user = request.form['username']
		pass1 = request.form['password']
		cursor.execute("INSERT INTO user_details(p_name,p_email,p_uname,p_pass) VALUES (%s,%s,%s,%s)",(name,email,user,pass1))
		mariadb_connection.commit()
		

		msg_content = str("Thannkyou!!!!!!!!!!")
		#creating message instance
		message = MIMEText(msg_content,'html')
		
		message['From'] = str('pranavfunny1@gmail.com')
		message['To'] = str(email)
		message['Subject'] = str('Mail Verificcation')
	
		msg_full = message.as_string()
	
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(message['From'],str('amigovoltzaryon'))
		server.sendmail(message['From'],message['To'],msg_full)
		server.quit()
	else:
		return 'error'

