"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Music limit 10;").fetchall()
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
    
def search()->dict:

    # query = "(Select Music_name, Music_year, musician_name \
    #     FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify)\
    #     Where musician_name LIKE \"%"+search+"%\") \
    #     UNION (Select Music_name, Music_year, musician_name \
    #     FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) \
    #     Where Music_name LIKE \"%"+search+"%\"OR Music_name LIKE \"%"+search + "%\") LIMIT 15;"

    # if len(plt) != 0:
    #     query = "Select Link_id, Link_name from Link l \
    #         Where l.Link_web = 'youtube' AND Music_id_spotify in \
    #         ( \
    #         (Select Music_id_spotify \
    #         FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) \
    #         Where musician_name LIKE \"%"+search+"%\") \
    #         UNION \
    #         (Select Music_id_spotify \
    #         FROM Music NATURAL JOIN Produce JOIN Musician USING (musician_id_spotify) \
    #         Where Music_name LIKE \"%"+search+"%\"OR Music_name LIKE \"%"+search+"%\" ) \
    #         ) \
    #         LIMIT 15;"

    # conn = db.connect()
    # query_results = conn.execute(query).fetchall()
    # conn.close()
    # todo_list = []
    # tag_dic={}
    # for result in query_results:
    #     if result[2] in tag_dic:
    #         mid=tag_dic[result[2]]
    #         tag_dic[result[2]]=mid+","+result[1]
    #     else:
    #         tag_dic[result[2]]=result[1]
    # for result in query_results:
    #     if result[0] in tag_dic:
    #         item = {
    #         "id": result[0],
    #         "name": result[2],
    #         "year": result[3],
    #         "tag":tag_dic[result[0]]
    #         }
    #     else:
    #         item = {
    #         "id": result[0],
    #         "name": result[2],
    #         "year": result[3],
    #         "tag":None
    #         }
            
    #     todo_list.append(item)

    # return todo_list
    item = {
            "id": 1,
            "name": 2,
            "year": 3,
            "tag":4
            }
    return [item]

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
