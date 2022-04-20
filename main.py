from flask import render_template
from flask import request
from app.db.users import find_users
from app.initialise import app


# test with http://localhost:5000
@app.route("/")
def home():
    return render_template('home.html')


# test with http://localhost:5000/?partial_email=ant
# test with http://localhost:5000/?partial_email=unknown
@app.route("/search")
def finduser():

    # f"...{aVariable}.." --> f means format the string that is between the quotes and insert
    #                           the variables value between the curly brackets
    print(f"received request to path {request.path}")

    partial_email_address = request.args['partial_email']
    partial_email_address = f"%{partial_email_address}%"  # add percent signs coz sql will use LIKE

    # call the function to find users with the partial email address that is in the URL
    users = find_users(partial_email_address)
    if len(users) == 0:
        return render_template('404.html'), 404
    else:
        return render_template('user.html', user=users[0])


# RUN THIS HERE, using the green arrow to the left in PyCharm
if __name__ == "__main__":
    app.run(host='0.0.0.0')
