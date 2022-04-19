# see https://pypi.org/project/PyMySQL/#example
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=30300,
                             user='root',
                             password='secret',
                             database='test',
                             cursorclass=pymysql.cursors.DictCursor)


def find_users(email_like):

    # "with" is used to automatically call the close function on the object, so that there are no resource leaks
    # for writing, don't forget: connection.commit()

    with connection.cursor() as cursor:
        sql = "SELECT id, email FROM users WHERE email like %s"  # never select the password or send it to the browser
        cursor.execute(sql, (email_like,))  # the second parameter is a python "tuple"
        result = cursor.fetchall()
        print(result)
        return result
