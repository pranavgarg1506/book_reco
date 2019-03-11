#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def get_user_name_page(id_u):
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		cursor.execute("select p_name from user_details where p_id = %s",[id_u])
		name = cursor.fetchall()
		ans = name[0][0].split(' ')
		return ans[0]








