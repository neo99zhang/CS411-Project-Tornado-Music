"""Defines all the functions related to the database"""
from app import db
from flask_login import UserMixin

class User(UserMixin):
    pass



def like(flag:int,uid:int)->None:
    print('abcd')
    conn=db.connect()
    user_id=1
    flag=1
    print('abc')
    #query_if_exist = 'select * from LIKE_LIST WHERE User_id='+ str(user_id) +' AND Music_id='+str(flag)+';'

    # print(conn.execute(query_if_exist).fetchall()==[])
    # print("3")

    # if(conn.execute(query_if_exist).fetchall()==[]):
    #     query='INSERT INTO LIKE_LIST VALUES ('+ str(user_id)+','+str(flag)+','+'0);'
    # else:
    #     query='UPDATE LIKE_LIST SET How_much=How_much+1 WHERE User_id='+ str(user_id) +' AND Music_id='+str(flag)+';'
    query='INSERT INTO LIKE_LIST VALUES ('+ str(user_id)+','+str(flag)+','+'0);'
    # print(query)
    conn.execute(query)
    conn.close()
    
    
def dislike(flag:int)->None:
    #print('abc')
    conn=db.connect()
    
    user_id=uid
    
    if(conn.execute(query_if_exist).fetchall()!=[]):
        query='UPDATE LIKE_LIST SET How_much=How_much-1 WHERE User_id='+ str(user_id) +' AND Music_id='+str(flag)+';'
    
    # print("333")
    # print(query)
    conn.execute(query)
    conn.close()
    
    
    
    
    
def musician(musician:str)->dict:
    conn=db.connect()
    query="SELECT Music_name FROM Musician NATURAL JOIN  Produce JOIN Music USING(Music_id_spotify) WHERE musician_name='"+musician+"' LIMIT 30;"
    print(query)
    conn = db.connect()
 
    query_results = conn.execute(query).fetchall()
    print([x for x in query_results])
    conn.close()
 
    # print(query_results)
    items1=[{}]
    for i,result in enumerate(query_results):
        item={
            "id":i,
            "Music_name": result[0],
           
            "musician_name": musician
            
        }
        items1.append(item)
    print(items1)
    return items1


# def signup_user(user:str, password:str) -> None:
    
#     conn = db.connect()
#     query_results = conn.execute("Select count(*) from User ").fetchall()
#     print(query_results[0][0])
#     id=query_results[0][0]
#     query = 'Insert Into User (User_id,User_password,User_nickname) VALUES ("{}", "{}","{}");'.format(
#         id,password,user)
#     print(query)
#     conn.execute(query)
#     conn.close()
    
    
# def query_user(user_id:str)->dict:
#     conn = db.connect()
#     query_results = conn.execute("Select * from User WHERE User_nickname='"+ user_id+"' LIMIT 10;").fetchall()
#     conn.close()
#     user = None

#     for result in query_results:
#         user={'id':result[0],'username':result[2],'password':result[1]}
    
   

#     return user
        

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Music limit 30;").fetchall()
    query_results1 = conn.execute("Select * from TAG;").fetchall()
    conn.close()
    todo_list = []
    tag_dic={}
    for result in query_results1:
        if result[2] in tag_dic:
            mid=tag_dic[result[2]]
            tag_dic[result[2]]=mid+","+result[1]
        else:
            tag_dic[result[2]]=result[1]
    for result in query_results:
        if result[0] in tag_dic:
            item = {
            "id": result[0],
            "name": result[2],
            "year": result[3],
            "tag":tag_dic[result[0]]
            }
        else:
            item = {
            "id": result[0],
            "name": result[2],
            "year": result[3],
            "tag":None
            }
            
        todo_list.append(item)

    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()

def update_tag(task_id: int, tag1: str,tag2:str) -> None:
    conn = db.connect()
    query = 'Update TAG set TAG_name = "{}" where TAG_name = "{}" and Music_id={};'.format(tag2,tag1,task_id)
    conn.execute(query)
    conn.close()
    
def search(search1:str,plt:str)->dict:
    # item={
    #         "id": 1,
    #         "name": 2,
    #         "year": 3,
    #         "tag":4
    #     }
    # return [item]
    #query = '(Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where musician_name LIKE "%%{}%%") UNION (Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where Music_name LIKE "%%{}%%" OR Music_name LIKE "%%{}%%") LIMIT 15;'.format(search1,search1,search1)
    if len(plt) != 0:
        query = 'Select Link_id, Link_name from Link l Where l.Link_web LIKE "%%{}%%" AND Music_id_spotify in ( (Select Music_id_spotify FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where musician_name LIKE "%%{}%%") UNION (Select Music_id_spotify FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where Music_name LIKE "%%{}%%"OR Music_name LIKE "%%{}%%" )) LIMIT 15;'.format(plt,search1,search1,search1)
    else:
        query = '(Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where musician_name LIKE "%%{}%%") UNION (Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where Music_name LIKE "%%{}%%" OR Music_name LIKE "%%{}%%") LIMIT 15;'.format(search1,search1,search1)
       
    print(query)
    conn = db.connect()
 
    query_results = conn.execute(query).fetchall()
    # print([x for x in query_results])
    conn.close()
 
    print(query_results)
    items2=[{}]
    items1=[{}]
    if len(query_results[0].keys()) == 3:
        for i,result in enumerate(query_results):
            item={
                "id":i,
                "Music_name": result[0],
                "Music_year": result[1],
                "musician_name": result[2],
                "tag":None
            }
            items1.append(item)
    else:
        
        for i,result in enumerate(query_results):
            item={
                "id":i,
                "Link_id": result[0],
                "Link_name": result[1],
                "tag":None
            }
            items2.append(item)

    return items1,items2
    
def acc_search(search1:str)->dict:
    # item={
    #         "id": 1,
    #         "name": 2,
    #         "year": 3,
    #         "tag":4
    #     }
    # return [item]
    #query = '(Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where musician_name LIKE "%%{}%%") UNION (Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where Music_name LIKE "%%{}%%" OR Music_name LIKE "%%{}%%") LIMIT 15;'.format(search1,search1,search1)

    query = '(Select Music_name, Music_year, musician_name FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) Where Music_name LIKE "%%{}%%")  LIMIT 15;'.format(search1)
 
    print(query)
    conn = db.connect()
 
    query_results = conn.execute(query).fetchall()
    # print([x for x in query_results])
    conn.close()
 
    print(query_results)
    items1=[{}]
    for i,result in enumerate(query_results):
        item={
            "id":i,
            "Music_name": result[0],
            "Music_year": result[1],
            "musician_name": result[2],
            "tag":None
        }
        items1.append(item)

    return items1

def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(task: int,tag:str) ->  int:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query_results = conn.execute("Select MAX(TAG_id) from TAG;").fetchall()
    tag_max=query_results[0][0]
    query = 'Insert Into TAG (TAG_id,TAG_name,Music_id) VALUES ("{}", "{}","{}");'.format(
       tag_max+1,tag,task)
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    print(query_results)
    # task_id = query_results[0][0]
    conn.close()

    return 


def remove_task_by_id(task_id: int) -> None:
    """ remove entries based on task ID """
   
    conn = db.connect()
    query = 'Delete From TAG where Music_id={};'.format(task_id)
    conn.execute(query)
    conn.close()

def procedure(input_user_id: int) -> dict:
    query = 'CALL recommand_follow({});'.format(input_user_id)
 
    print(query)
    conn = db.connect()
 
    query_results = conn.execute(query).fetchall()
    # print([x for x in query_results])
    conn.close()
 
    print(query_results)
    items1=[{}]
    for i,result in enumerate(query_results):
        item={
            "id":i,
            "friend_id": result[0],
            "like_score": result[1]
        }
        items1.append(item)

    return items1

def sign_up(username:str,password:str) -> int:
    if len(username) > 10 or len(password)>10:
        print('password or username too long')
        return -1

    res = 0
    for x in username:
        res*=256
        res+= ord(x)
    res=res%(2**32)
    conn = db.connect()
    query = 'select * from User WHERE User_id = '+ str(res) + ';'
    query_results = conn.execute(query).fetchall()
    if  not len(query_results) == 0:
        print("user already exist")
        return -1

    query = 'insert into User VALUES  ("{}", "{}","{}");'.format(res,password,username)
    conn.execute(query)
    conn.close()
    return 1



def log_in(username:str,password:str) -> int:
    success = -1
    if len(username) > 10 or len(password)>10:
        print('password or username too long')
        return -1
    res = 0
    for x in username:
        res*=256
        res+= ord(x)
    res=res%(2**32)
    conn = db.connect()
    query = 'select * from User WHERE User_id = '+ str(res) + ' AND User_nickname = \''+username+'\';'
    query_results = conn.execute(query).fetchall()
    if len(query_results) == 0:
        print("user_name not exit")
    if len(query_results) > 1:
        print("unexpected error")
    if query_results[0]['User_password'] == password:
        user_id=res;
        print("login success!")
        success = 1
    else:
        print("password error!")
        res = -1
    return success,res
