#!/usr/bin/python3

import os
import numpy as np
from flask import Flask,render_template,request,session,redirect, url_for,send_file
import mysql.connector as mariadb
from register import register_page
from login import login_page
from user import user_page
from admin_login import admin_login_page
from view_users import view_users_page
from view_books import view_books_page
from add_books import add_books_page
from person_recommend import person_recommend_page
from book import book_page
from rating_update import rating_update_page
from final_update import final_update_page
from search_h import search_h_page
from search_u import search_u_page
from get_user_name import get_user_name_page
#from werkzeug.utils import secure_filename




mariadb_connection = mariadb.connect(user='pranav', password='funny', database='major', host='localhost')
cursor = mariadb_connection.cursor()

#______________________________________________________________________________________________________________________________

app = Flask(__name__)
app.secret_key = os.urandom(24)

#_______________________________________________________________________________________________________________________________


@app.route('/')
def home():
	return render_template('home.html')






# ALL ABOUT USER REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def reg():
	return render_template('register.html')

@app.route('/add_data', methods=['GET', 'POST'])
def add():
	register_page()
	return render_template('login.html')







# ALL ABOUT USER LOGIN AND ITS OPERATION PAGE
@app.route('/login', methods=['GET', 'POST'])
def log():
	return render_template('login.html')

@app.route('/check_data', methods=['GET', 'POST'])
def check():
	answer = login_page()
	if answer[0]==1:
		name = user_page(answer[1])
		personal_books = person_recommend_page(answer[1])
		return render_template('user.html',uname=name,p_books=personal_books,id_u=answer[1][0][0])
	else:
		return render_template('login.html')





# ALL ABOUT PAGE DESCRIPTION
@app.route('/book_description<int:b_id><int:u_id><string:u_name>', methods=['GET', 'POST'])
def des(b_id,u_id,u_name):
	book_desc = book_page(b_id)
	return render_template('book.html',results=book_desc,u_id=u_id,u_name=u_name)




# ALL ABOUT BOOK RATING UPDATION
@app.route('/rate_update<int:b_id><int:u_id><string:u_name>', methods=['GET', 'POST'])
def update(b_id,u_id,u_name):
	u_rate = rating_update_page()
	final_update_page(b_id, u_id, u_rate)
	book_desc = book_page(b_id)
	return render_template('book.html',results=book_desc,u_id=u_id,u_name=u_name)



# ALL ABOUT DOWNLOADING BOOKS
@app.route('/download_file1<int:b_id>', methods=['GET', 'POST'])
def downloa1(b_id):
	present_location = os.getcwd()
	precise_location = present_location+"/database/pdfs/"
	return send_file(precise_location+str(b_id)+str(".pdf"), as_attachment=True)

# ALL ABOUT READING BOOKS
@app.route('/download_file2<int:b_id>', methods=['GET', 'POST'])
def downloa2(b_id):
	present_location = os.getcwd()
	precise_location = present_location+"/database/pdfs/"
	return send_file(precise_location+str(b_id)+str(".pdf"))



# ABOUT ADMIN INFORMATION AND PERMISSIONS
@app.route('/admin',methods=['GET','POST'])
def admin1():
	return render_template('admin/index.html')

@app.route('/check_data_admin', methods=['GET', 'POST'])
def check_admin():
	answer = admin_login_page()
	if answer==1:
		return render_template('admin/admin.html')
	else:
		return render_template('admin/index.html')

@app.route('/view_users', methods=['GET','POST'])
def show_view_users():
	users_info = view_users_page()
	return render_template('admin/view_users.html',results=users_info)

@app.route('/view_books', methods=['GET','POST'])
def show_view_books():
	books_info = view_books_page()
	return render_template('admin/view_books.html',results1=books_info)

@app.route('/add_books')
def addb():
	return render_template('admin/add_books.html')

@app.route('/add_books_data', methods=['GET', 'POST'])
def addbd():
	add_books_page()
	return render_template('admin/add_books.html')





# LOGOUT
@app.route('/logout')
def out():
	#session.pop('user',None)
	return render_template('login.html')




#ALL ABOUT SEARCH IN HOME
@app.route('/action_page_home',methods=['POST','GET'])
def search1():
	query = request.form['search1']
	results = search_h_page(query)
	return render_template('/search_h.html',results=results)





# ALL ABOUT SEARCH IN USER
@app.route('/action_page_user<int:id_u>',methods=['POST','GET'])
def search2(id_u):
	query = request.form['search2']
	results = search_u_page(query)
	name = get_user_name_page(id_u)
	return render_template('/search_u.html',results=results,id_u=id_u,uname=name)


#____________________________________________________________________________________________________________________________________


if __name__ == '__main__':
	app.run(host='192.168.43.168',debug = True)

#app.run(host, port, debug, options)
