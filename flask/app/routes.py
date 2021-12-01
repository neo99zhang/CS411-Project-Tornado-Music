""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from models import query_user, User
from app import app
from app import database as db_helper
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
items=[{}]
@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
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

app.secret_key = '1234567' # random
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Please Login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        curr_user = User()
        curr_user.id = user_id

        return curr_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        user = query_user(user_id)
        if user is not None and request.form['password'] == user['password']:

            curr_user = User()
            curr_user.id = user_id

            login_user(curr_user)

            return 'Login successfully'

        #flash('Wrong username or password!')

    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'

@app.route('/signin')
def signin():
    
    return render_template('signin.html')




@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)
