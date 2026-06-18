from db_config import get_connection
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    plan = request.form.get('plan')

    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    INSERT INTO members(name, email, phone, plan)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (name, email, phone, plan))
    connection.commit()
    cursor.close()
    connection.close()
    return {"status":"success","message":"Membership Registration Successful"}


@app.route('/contact', methods=['POST'])
def contact():

    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    INSERT INTO contacts(name, email, message)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (name, email, message))
    connection.commit()
    cursor.close()
    connection.close()
    return {"status":"success","message":"Our team will contact you soon"}
@app.route('/trial', methods=['POST'])
def trial():

    name = request.form.get('name')
    email = request.form.get('email')
    date = request.form.get('date')

    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    INSERT INTO trial_bookings(name, email,  trial_date)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (name, email, date))
    connection.commit()
    cursor.close()
    connection.close()
    return {"status":"success","message":"Trial Booked Successfully"}


@app.route('/admin')
def admin():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM members")
    members_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM contacts")
    contacts_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM trial_bookings")
    trials_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        'admin.html',
        members_count=members_count,
        contacts_count=contacts_count,
        trials_count=trials_count
    )

if __name__ == '__main__':
    app.run(debug=True)