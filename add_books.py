#!/usr/bin/python3

from flask import Flask,render_template,request,session
import mysql.connector as mariadb

def add_books_page():
	mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
	if mariadb_connection.is_connected():
		cursor = mariadb_connection.cursor()

		# requesting the values from the form
		bname = request.form['b_name']
		bauthor = request.form['b_author']
		btype = request.form['b_type']
		brating = request.form['avg_rating']
		bcount = request.form['b_count']
		byear = request.form['b_year']

		# request for the book_pic upload
		file1 = request.files['upload1']
		file2 = request.files['upload2']
		
		## inserting the values into the table
		cursor.execute("INSERT INTO books_details(b_name,b_author,b_type,b_avg_rating,count) VALUES (%s,%s,%s,%s,%s)",(bname,bauthor,btype,brating,bcount,byear))
		mariadb_connection.commit()

		# for image upload processing
		location1 = 'static/'
		file_name1 = file1.filename

		# for pdf upload procesing
		location2 = 'database/pdfs/'
		file_name2 = file2.filename
		
		# split the file name with '.'
		file_name_split1 = file_name1.split('.')
		file_name_split2 = file_name2.split('.')
		# get the extension
		extension1 = file_name_split1[1]
		extension2 = file_name_split2[1]
		
		# get the book id of the to be upload book
		cursor.execute("select b_id from books_details where b_name = %s and b_author = %s ",(bname,bauthor))
		bid = cursor.fetchall()
		mariadb_connection.commit()
		bid=bid[0][0]
		file1.save(location1+str(bname)+str('.')+extension1)
		file2.save(location2+str(bid)+str('.pdf'))
		
	else:
		return 'error'

