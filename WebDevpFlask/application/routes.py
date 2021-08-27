from application import app, db
from flask import render_template, request, json, Response

users = [{"id": 1, "first_name": "Jacques", "last_name": "Blazewicz", "email": "jblazewicz0@posterous.com",
          "password": "k9doaly"},
         {"id": 2, "first_name": "Budd", "last_name": "Zellick", "email": "bzellick1@uol.com.br",
          "password": "kik8N0cyKG"},
         {"id": 3, "first_name": "Simone", "last_name": "Brenston", "email": "sbrenston2@squarespace.com",
          "password": "9BO7nEvdci8"},
         {"id": 4, "first_name": "Waneta", "last_name": "Stading", "email": "wstading3@google.es",
          "password": "GpzWY536X"},
         {"id": 5, "first_name": "Barbey", "last_name": "Corder", "email": "bcorder4@csmonitor.com",
          "password": "BXFkbgEz"},
         {"id": 6, "first_name": "Becca", "last_name": "Hartington", "email": "bhartington5@wsj.com",
          "password": "ijh3RfxcGB"},
         {"id": 7, "first_name": "Elyse", "last_name": "Eddy", "email": "eeddy6@archive.org", "password": "QJHg5Gc0V"},
         {"id": 8, "first_name": "Reggie", "last_name": "Souster", "email": "rsouster7@4shared.com",
          "password": "nmCeQGRC"},
         {"id": 9, "first_name": "Brnaby", "last_name": "Abrahmson", "email": "babrahmson8@digg.com",
          "password": "BqOgwfIMJmTx"},
         {"id": 10, "first_name": "Yuma", "last_name": "Graine", "email": "ygraine9@tmall.com", "password": "4VpkAWyL"},
         {"id": 11, "first_name": "Quinton", "last_name": "Chater", "email": "qchatera@squarespace.com",
          "password": "7x6IYp"},
         {"id": 12, "first_name": "Raymund", "last_name": "Moorman", "email": "rmoormanb@indiatimes.com",
          "password": "aRgaXm1"},
         {"id": 13, "first_name": "Boycey", "last_name": "Ferrelli", "email": "bferrellic@cnet.com",
          "password": "VCKtIJEUi"},
         {"id": 14, "first_name": "Ty", "last_name": "Raffeorty", "email": "traffeortyd@cnet.com",
          "password": "wVOd2oi"},
         {"id": 15, "first_name": "Judie", "last_name": "Penella", "email": "jpenellae@psu.edu",
          "password": "0WP0F6516"},
         {"id": 16, "first_name": "Alden", "last_name": "Gemlett", "email": "agemlettf@independent.co.uk",
          "password": "3rAW4wlTsCWz"},
         {"id": 17, "first_name": "Josephina", "last_name": "MacLeod", "email": "jmacleodg@livejournal.com",
          "password": "gQ7ytj7CtA6"},
         {"id": 18, "first_name": "Lorene", "last_name": "Lindeberg", "email": "llindebergh@chron.com",
          "password": "Q4WU8aHkm"},
         {"id": 19, "first_name": "Lamar", "last_name": "Sotham", "email": "lsothami@rediff.com",
          "password": "5yyhnYPTDs"},
         {"id": 20, "first_name": "Derek", "last_name": "Breakey", "email": "dbreakeyj@home.pl",
          "password": "jrz2kl2jeX"}]

courseData = [
    {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4, "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
     "term": "Fall"},
    {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4, "term": "Fall"}]


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if idx == None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata), mimetype="application/json")


class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=30)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)


@app.route("/user")
def user():
    # User(user_id=1, first_name="Rohan", last_name="Pathak",
    #     email="bruh@bruh.com", password="bruh0511").save()
    # User(user_id=2, first_name="Sri", last_name="Pathak",
    #    email="sri@sri.com", password="sri0511").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
