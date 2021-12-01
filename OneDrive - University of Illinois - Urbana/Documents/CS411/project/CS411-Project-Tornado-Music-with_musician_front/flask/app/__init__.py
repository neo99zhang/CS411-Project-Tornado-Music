"""Setup at app startup"""
import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader



#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
# Remember - storing secrets in plaintext is potentially unsafe. Consider using
# something like https://cloud.google.com/secret-manager/docs/overview to help keep
# secrets secret.

    db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_password,  # e.g. "my-database-password"
            database=db_name,  # e.g. "my-database-name"
            query={
                "unix_socket": "{}/{}".format(
                    db_socket_dir,  # e.g. "/cloudsql"
                    db_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        ),
        #**db_config
    )
    # unix_socket = '/cloudsql/{}'.format(db_connection_name)
    # try:
    #     if os.environ.get('GAE_ENV') == 'standard':
    #         conn = pymysql.connect(user=db_user, password=db_password,
    #                             unix_socket=unix_socket, db=db_name,
    #                             cursorclass=pymysql.cursors.DictCursor
    #                             )
    # except pymysql.MySQLError as e:
    #     print(e)

    return pool


def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """


    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )

    return pool


app = Flask(__name__)
# db = init_connection_engine()
db = open_connection()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
