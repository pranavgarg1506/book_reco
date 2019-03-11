#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def search_u_page(query):
	total_ids=[]
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()
		#query = request.form['search2']
		query = query.split()
		for data in query:
			cursor.execute("select b_id from books_details where b_name like '%"+data+"%' || b_author like '%"+data+"%' || b_type like '%"+data+"%'")
			ids = cursor.fetchall()
			for i in ids:
				total_ids.append(i[0])
			mariadb_connection.commit()
		
		# to find only the unique ids
		set_ids = set(total_ids)
		# conversion of set into list
		list_ids = list(set_ids)
		#print(list_ids)
		answer=[]
		for ids in list_ids:
			cursor.execute("select * from books_details where b_id = " + str(ids)+"")
			ans = cursor.fetchall()
			answer.append(ans)
			mariadb_connection.commit()
		return answer








