# https://pypi.org/project/PyMySQL/#example
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
# https://docs.sqlalchemy.org/en/14/dialects/mysql.html#dialect-mysql
# https://chartio.com/resources/tutorials/how-to-execute-raw-sql-in-sqlalchemy/
# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
from sqlalchemy import text
from app.initialise import db


def find_users(email_like):

    # never select the password or send it to the browser
    sql = text("SELECT id, email FROM users WHERE email like :mail")

    result = db.session.execute(sql, {"mail": email_like})

    rows = result.all()

    print(rows)

    return rows


def create_user(email, password):
    """ returns the id of the newly created user """
    sql = text("insert into users (email, password) values (:email, MD5(:password))")  # let mysql auto increment the id

    # create a "dictionary" which maps the names used above, to the values passed into this function
    parameters = {"email": email, "password": password}

    # execute the sql using the parameters
    db.session.execute(sql, parameters)

    # now fetch the last auto_increment value, i.e. the PK of the new user
    result = db.session.execute(text("SELECT LAST_INSERT_ID()"))

    user_id = result.fetchone()
    print(f"new user's id: {user_id}")
    db.session.commit()  # don't forget to commit, so that the data is saved in the DB
    return user_id[0]  # it's in the zeroth column of the table that was returned


def delete_user(user_id):

    sql = text("delete from users where id = :id")
    result = db.session.execute(sql, {"id": user_id})
    print(f"deleted {result.rowcount} rows")
    db.session.commit()
