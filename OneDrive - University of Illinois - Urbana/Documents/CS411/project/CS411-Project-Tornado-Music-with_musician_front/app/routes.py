""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
# from models import query_user, User
from app import app
from app import database as db_helper
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
items=[{}]
uid=0
global_name='User'
@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
        app.logger.info('deleting')
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return None


@app.route("/like/<int:flag>", methods=['POST'])
def like(flag):
    """ recieved post requests for entry delete """
    global uid
    print(flag,'flag')
    try:
        
        db_helper.like(flag,uid)
        result = {'success': True, 'response': 'LIKE task','flag':flag}
    except:
        result = {'success': False, 'response': 'Something went wrong','flag':flag}

    return jsonify(result)

@app.route("/dislike/<int:flag>", methods=['POST'])
def dislike(flag):
    """ recieved post requests for entry delete """

    try:
        db_helper.dislike(flag,uid)
        result = {'success': True, 'response': 'LIKE task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    
    db_helper.insert_new_task(data['task'],data['tag'])
  
    result = {'success': True, 'response': "DONE"}
    return jsonify(result)


@app.route("/update", methods=['POST'])
def edit():
    """ recieved post requests for entry updates """

    data = request.get_json()
    print(data)

    db_helper.update_tag(data["task"],data["tag1"],data["tag2"])
    result = {'success': True, 'response': 'Status Updated'}
       
    return jsonify(result)

@app.route("/search", methods=['POST','GET'])
def search():
    """ recieved post requests for entry updates """
    global items1,items2
    data = request.get_json()
    if data!=None:
        items1,items2 = db_helper.search(data['search'],data['plt'])
    result = {'success': True, 'response': 'Status Updated'}
    # return jsonify(data)
    return render_template("search_results.html",items1=items1,items2=items2)
    # return render_template("search_results.html", items=items)

@app.route("/acc_search", methods=['POST','GET'])
def acc_search():
    """ recieved post requests for entry updates """
    global items3
    data = request.get_json()
    if data!=None:
        items3= db_helper.acc_search(data['search'])
    result = {'success': True, 'response': 'Status Updated'}
    # return jsonify(data)
    return render_template("acc_search_results.html",items1=items3)


@app.route("/storedProc", methods=['POST','GET'])
def storedProc():
    """ recieved post requests for entry updates """

    data = request.get_json()
    print(data)
    global items4
    if data!=None:
        items4 = db_helper.procedure(data["uid"])
    result = {'success': True, 'response': 'Status Updated'}
    print(items4)
    return render_template("like_score.html",items1=items4)

@app.route("/login", methods=['POST','GET'])
def login():
    """ recieved post requests for entry updates """
    global items6,items7,uid, user_name_, global_name
    print("we are here!")
    data = request.get_json() 
    fff = -1
    if data!=None:
        items6 = data['username']
        user_name_ = items6
        items7 =data['password']
        fff,uid = db_helper.log_in(data['username'],data['password'])
        global_name= user_name_
    result = {'success': True, 'response': 'DONE'}
    print(fff,uid)
    # return jsonify(data)

    return redirect(url_for('about'))

@app.route("/signup", methods=['POST','GET'])
def signup():
    """ recieved post requests for entry updates """
    global items8,items9,uid,global_name
    data = request.get_json()
    fff = -1



    if data!=None:
        print(data)
        items8 = data['username']
        items9 =data['password']
        fff,uid = db_helper.sign_up(data['username'],data['password'])
    result = {'success': True, 'response': 'DONE'}
    global_name=items8
    # return jsonify(data)
    return jsonify(result)




@app.route("/music", methods=['GET', 'POST'])
def music():
    """ recieves post requests to add new task """
    result = {'success': 0, 'response': "DONE"}
    print(1111111)
    data = request.get_json()
    
    global items5
    if data!=None:
        items5 = db_helper.musician(data['search'])
        result = {'success': True, 'response': 'Status Updated'}
    
    # return render_template("like_score.html",items1=items4)
    # db_helper.insert_new_task(data['task'])
  
    return render_template('music.html',items2=items5)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    global uid
    items = db_helper.fetch_todo(uid)
    return render_template("index.html", items=items, item6=global_name, uid=uid)



@app.route("/about")
def about():
    """ returns rendered homepage """
    
    return render_template("about.html", items=items)

@app.route("/signout", methods=['GET', 'POST'])
def signout():
    """ returns rendered homepage """
    print("sign")
    global global_name, uid
    global_name='user'
    uid=0
    return render_template("index.html", items=items, item6=global_name, uid=uid)


