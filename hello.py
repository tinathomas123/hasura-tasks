from urllib.request import urlopen
import json
import requests
import sys
import logging
from flask import Flask
from flask import render_template
from flask import Markup
from flask import request,make_response,abort

app=Flask(__name__)
log=logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

#1
@app.route('/')
def hello_world():
	return 'Hello World - Christine'

#2a
@app.route('/authors')
def getAuthors():
        return requests.get('https://jsonplaceholder.typicode.com/users').content

#2b
@app.route('/posts')
def getPosts():
        return requests.get('https://jsonplaceholder.typicode.com/posts').content

#2c
@app.route('/mixed')
def getMixed():
        url_users = 'https://jsonplaceholder.typicode.com/users'
        url_posts='https://jsonplaceholder.typicode.com/posts'

        # download the json string
        json_string_users = urlopen(url_users).read()
        json_string_posts = urlopen(url_posts).read()

        # de-serialize the string so that we can work with it
        the_data_users = json.loads(json_string_users)
        l_users=len(the_data_users)
        list_users=[]

        the_data_posts = json.loads(json_string_posts)
        l_posts=len(the_data_posts)

        obj=''
        
        
        for i in range(l_users):

                count_posts=0
                for j in range(l_posts):

                        if the_data_users[i]['id']==the_data_posts[j]['userId']:
                                count_posts=count_posts+1

                obj=the_data_users[i]['name']+" "+str(count_posts)                
                list_users.append(obj)
        
        return "\n".join(list_users)

        

#3
@app.route('/setcookie')
def setCookie():
        resp=make_response(render_template('hello.html'))
        resp.set_cookie('name','Christine')
        resp.set_cookie('age','24')
        return resp

#4
@app.route('/getcookies')
def getCookie():
        name=request.cookies.get('name')
        age=request.cookies.get('age')
        return "name="+name+" and age="+age
#5
@app.route('/robots.txt')
def denyReq():
        abort(401)

#6
@app.route('/html')
def getHtml():
        return render_template('hello.html')
#7
@app.route('/input')
def getInput():
        return render_template('input.html')
#7
@app.route('/display',methods=['POST'])
def getDisplay():
        data=request.form['someValue']
        log.info(data)
        return data
