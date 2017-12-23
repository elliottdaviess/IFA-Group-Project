import os
from flask import Flask, redirect, request, render_template, make_response
import sqlite3

DATABASE = 'fiscusFactFinder.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#Admin

@app.route("/clientLanding")
def clientLanding():
   return render_template('clientLanding.html', msg = '')

@app.route("/clientLandingPartner")
def clientLandingPartner():
   return render_template('clientLandingPartner.html', msg = '')


@app.route("/")
def home():
   return render_template('home.html', msg = '')

@app.route("/Contact")
def contact():
   return render_template('Contact.html', msg = '')


@app.route("/clientProfile")
def clientProfile():
   return render_template('clientProfile.html', msg = '')

@app.route("/clientPDF")
def clientPDF():
   return render_template('clientPDF.html', msg = '')


@app.route("/clientStats")

def clientStats():
   return render_template('clientstats.html', msg = '')

@app.route("/peopleClient")
def peopleclient():
   return render_template('peopleclient.html', msg = '')

@app.route("/peopleClientPartner")
def peopleClientPartner():
   return render_template('peopleClientPartner.html', msg = '')


@app.route("/peopleDependants")
def peopledependents():
   return render_template('peopleDependants.html', msg = '')

@app.route("/peopleDependantsPartner")
def peopledependentsPartner():
   return render_template('peopleDependantsPartner.html', msg = '')


@app.route("/peopleHealth")
def peoplehealth():
   return render_template('peopleHealth.html', msg = '')

@app.route("/peopleHealthPartner")
def peoplehealthPartner():
   return render_template('peopleHealthPartner.html', msg = '')


@app.route("/peopleOccupations")
def peopleOccupations():
   return render_template('peopleOccupations.html', msg = '')

@app.route("/peopleOccupationsPartner")
def peopleOccupationsPartner():
   return render_template('peopleOccupationPartner.html', msg = '')


@app.route("/peopleTaxStatus")
def peopleTaxStatus():
   return render_template('peopleTaxStatus.html', msg = '')

@app.route("/peopleTaxStatusPartner")
def peopleTaxStatusParnter():
   return render_template('peopleTaxStatusPartner.html', msg = '')


@app.route("/financesIncomePartner")
def financesIncomePartner():
   return render_template('financesIncomePartner.html', msg = '')

@app.route("/financesIncome")
def financesIncome():
   return render_template('financesIncome.html', msg = '')


@app.route("/financesLiabilities")
def financesLiabilities():
   return render_template('financesLiabilities.html', msg = '')

@app.route("/financesLiabilitiesPartner")
def financesLiabilitiesPartner():
   return render_template('financesLiabilitiesPartner.html', msg = '')


@app.route("/financesAssets")
def financesAssets():
   return render_template('financesAssets.html', msg = '')


@app.route("/financesAssetsPartner")
def financesAssetsPartner():
   return render_template('financesAssetsPartner.html', msg = '')


@app.route("/financesExpenditure")
def financesExpenditure():
   return render_template('financesExpenditure.html', msg = '')

@app.route("/financesExpenditurePartner")
def financesExpenditurePartner():
   return render_template('financesExpenditurePartner.html', msg = '')


@app.route("/financesAffordability")
def financesAffordability():
   return render_template('financesAffordability.html', msg = '')


@app.route("/financesAffordabilityPartner")
def financesAffordabilityPartner():
   return render_template('financesAffordabilityPartner.html', msg = '')


@app.route("/newPassword")
def newPassword():
   return render_template('newPassword.html', msg = '')

@app.route("/Login")
def login():
   return render_template('logIn.html', msg = '')
# app.secret_key = 'bubbles'
# @app.route("/Login")
# def login():
#     email = request.form.get('email', default="Error")
#     password = request.form.get('password', default="Error")
#     try:
#         request.method=='GET';
#         conn = sqlite3.connect(DATABASE)
#         cur = conn.cursor()
#         cur.execute("SELECT email FROM client_register WHERE email=?;", [email])
#         cur.execute("SELECT password FROM client_register WHERE password=?;", [password])
#         if checkCredentials(email, password): # if
#             resp = make_response(render_template('clientLanding.html', msg='hello '+uName, username = uName))
#             session['username'] = request.form['username']
#         else:
#             username = 'none'
#             if 'username' in session:
#                username = escape(session['username'])
#             return render_template('login.html', msg = '', username = username)
#         finally:
#             conn.close()


@app.route("/Reg")
def reg():
   return render_template('register.html', msg = '')

@app.route("/Reg-ifa")
def reg_ifa():
   return render_template('register_ifa.html', msg = '')

@app.route("/ifalist")
def ifalist():
   return render_template('IFAClientList.html', msg = '')

@app.route("/ifalanding")
def ifaland():
        firsname = "Aaron"
        return render_template('ifaLanding.html', msg = '')



@app.route("/ifastats")
def ifastat():
   return render_template('ifaStats.html', msg = '')

@app.route("/web")
def web():
   return render_template('index.html', msg = '')

# ---- SEARCH ---- #

@app.route("/SearchClients", methods = ['GET'])                                             #rendering search page
def staffsearchPage():
    return render_template('IFASearchPage.html', msg = '')

@app.route("/Client/Search/Surname", methods = ['GET'])                                                      # GETTING USER INPUT FROM DB (SEARCH)
def surnameSearch():
    surname = request.args.get('surname', default="Error") #rem: args for get form for post
    surname_ifa_code = request.args.get('surname_ifa_code', default ="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    print(surname, surname_ifa_code)
    cur.execute("SELECT * FROM client_details WHERE surname=?;", [surname])
    #cur.execute("SELECT * FROM client_details WHERE surname=? AND ifa_code=?;", [surname, surname_ifa_code])
    data = cur.fetchall()
    conn.close()
    return render_template('ListCustomers.html', data = data)

@app.route("/Client/Search/FirstName", methods = ['GET'])                                                      # GETTING USER INPUT FROM DB (SEARCH)
def firstnameSearch():
    firstname = request.args.get('firstname', default="Error") #rem: args for get form for post
    firstname_ifa_code = request.args.get('firstname_ifa_code', default ="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_details WHERE first_name=?;", [firstname])
    data = cur.fetchall()
    conn.close()
    return render_template('ListCustomers.html', data = data)

@app.route("/Client/Search/Email", methods = ['GET'])                                                      # GETTING USER INPUT FROM DB (SEARCH)
def emailSearch():
    email = request.args.get('email', default="Error") #rem: args for get form for post
    email_ifa_code = request.args.get('email_ifa_code', default ="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM client_details WHERE email=?;", [email])
    data = cur.fetchall()
    conn.close()
    return render_template('ListCustomers.html', data = data)

# ---- END SEARCH ---- #


@app.route("/Reg-ifa", methods = ['POST'])
def IFA_Reg():
    firstName = request.form.get('first_name', default="Error")#rem: args for get form for post
    surname = request.form.get('surname', default="Error")
    email = request.form.get('email', default="Error")
    password = request.form.get('password', default="Error")
    if ifacheckemail(email):
        resp = make_response(render_template('register_ifa.html', msg='Sorry, that email is already affiliated with an exisiting IFA account'))
        return resp
    if clientcheckemail(email):
        resp = make_response(render_template('register_ifa.html', msg='Sorry, that email is already affiliated with an exisiting Client account'))
        return resp
    else:
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO adviser_details ('firstName', 'surname', 'email', 'password')\
                     VALUES (?,?,?,?)",(firstName, surname, email, password) )
            conn.commit()
            msg = "Record successfully added"

        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            return msg
            conn.close()

@app.route("/Reg", methods = ['POST'])
def Client_reg():
    first_name = request.form.get('first_name', default="Error")#rem: args for get form for post
    surname = request.form.get('surname', default="Error")
    email = request.form.get('email', default="Error")
    password = request.form.get('password', default="Error")
    confirm_password = request.form.get('confirm_password', default="Error")
    singlepartner = request.form.get('singlepartner', default="Error")
    ifa_code = request.form.get('ifa_code', default="Error")
    if ifacheckemail(email):
        resp = make_response(render_template('register.html', msg='Sorry, that email is already affiliated with an exisiting IFA account'))
        return resp
    if clientcheckemail(email):
        resp = make_response(render_template('register.html', msg='Sorry, that email is already affiliated with an exisiting Client account'))
        return resp
    else:
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO client_details('first_name', 'surname', 'email', 'password', 'confirm_password','singlepartner','ifa_code')\
                        VALUES (?,?,?,?,?,?,?)",(first_name, surname, email, password, confirm_password, singlepartner,ifa_code) )
            conn.commit()
            msg = "Record successfully added"

        except Exception as e:
            conn.rollback()
            msg = "error in insert operation"
            print(e)
        finally:
            return msg
            conn.close()

def clientcheckemail(email): # checking that email is in the client_registration table
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT email FROM client_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if email in str(data):
      return email

def ifacheckemail(email): # checking that email is in the client_registration table
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT email FROM adviser_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if email in str(data):
      return email

@app.route("/peopleClient", methods = ['POST'])
def clientAddDetailsClient():
    title= request.form.get('title', default="Error")
    #first_name = request.form.get('first_name', default="Error")#rem: args for get form for post
    initials = request.form.get('initials', default="Error")
    #surname = request.form.get('surname', default="Error")
    prefers = request.form.get('prefers', default="Error")
    sex = request.form.get('sex', default="Error")#rem: args for get form for post
    marital_status = request.form.get('marital_status', default="Error")
    dob = request.form.get('dob', default="Error")
    maiden_name = request.form.get('maiden_name', default="Error")
    retire_age = request.form.get('retire_age', default="Error")#rem: args for get form for post
    religious = request.form.get('religious', default="Error")
    changes = request.form.get('changes', default="Error")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO client_details ('title', 'initials', 'prefers', 'sex', 'marital_status','dob', 'maiden_name', 'retire_age', 'religious', 'changes')\
                         VALUES (?,?,?,?,?,?,?,?,?,?)",(title, initials, prefers, sex, marital_status,dob, maiden_name, retire_age, religious, changes) )
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return render_template('peopleClient.html', msg = msg)
        conn.close()

@app.route("/peopleTaxStatus", methods = ['POST'])
def clientAddDetailsTax():
    nationality= request.form.get('nationality', default="Error")
    domicile = request.form.get('domicile', default="Error")#rem: args for get form for post
    uk_res = request.form.get('uk_res', default="Error")
    tax_payer = request.form.get('tax_payer', default="Error")
    live_abroad = request.form.get('live_abroad', default="Error")
    NINO = request.form.get('NINO', default="Error")#rem: args for get form for post
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO client_details ('nationality','domicile', 'uk_res', 'tax_payer', 'live_abroad', 'NINO')\
                         VALUES (?,?,?,?,?,?)",(nationality, domicile, uk_res, tax_payer, live_abroad, NINO) )
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return render_template('peopleOccupations.html', msg = msg)
        conn.close()

@app.route("/peopleOccupations", methods = ['POST'])
def clientAddDetailsOccupations():
    occupation = request.form.get('occupation', default="Error")
    employment_status = request.form.get('employment_status', default="Error")
    self_employed = request.form.get('self_employed', default="Error")
    employer = request.form.get('employer', default="Error")
    date_joined = request.form.get('date_joined', default="Error")
    ideal_ret_age = request.form.get('ideal_ret_age', default="Error")
    leaving_soon = request.form.get('leaving_soon', default="Error")
    finish_date = request.form.get('finish_date', default="Error")
    ret_age = request.form.get('ret_age', default="Error")
    leaving_reason = request.form.get('leaving_reason', default="Error")
    return_date = request.form.get('return_date', default="Error")
    gcse = request.form.get('gcse', default="Error")
    alevel_btec = request.form.get('alevel_btec', default="Error")
    other = request.form.get('other', default="Error")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO client_details ('occupation','employment_status','self_employed','employer','date_joined','ideal_ret_age','leaving_soon','finish_date','ret_age','leaving_reason','return_date','gcse','alevel_btec','other')\
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(occupation, employment_status, self_employed, employer, date_joined, ideal_ret_age, leaving_soon, finish_date, ret_age, leaving_reason, return_date, gcse, alevel_btec, other) )
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        conn.close()

@app.route("/peopleHealth", methods = ['POST'])
def clientAddDetailsHealth():
    health_state = request.form.get('health_state', default="Error")
    smoker = request.form.get('smoker', default="Error")
    cigarette_number = request.form.get('cigarette_number', default="")
    drinker = request.form.get('drinker', default="Error")
    drinking_unit = request.form.get('drinking_unit', default="")
    height_feet_inches = request.form.get('height_feet_inches', default="Error")
    specify_st_lb = request.form.get('specify_st_lb', default="Error")
    specify_kg = request.form.get('specify_kg', default="Error")
    hazard_pastime = request.form.get('hazard_pastime', default="Error")
    specify_hazard = request.form.get('specify_hazard', default="")
    health_issues = request.form.get('health_issues', default="Error")
    specify_health_issues = request.form.get('specify_health_issues', default="")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO client_details ('health_state','smoker','cigarette_number','drinker','drinking_unit','height_feet_inches','specify_st_lb','specify_kg','hazard_pastime','specify_hazard','health_issues','specify_health_issues')\
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(health_state, smoker, cigarette_number, drinker, drinking_unit, height_feet_inches, specify_st_lb, specify_kg, hazard_pastime, specify_hazard, health_issues, specify_health_issues) )
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        conn.close()




app.secret_key = 'fj590Rt?h40gg'

#Cookie sessions
@app.route("/Login", methods = ['POST'])
def userlogin():
    if request.method=='POST':
        email = request.form.get('email', default="Error")
        password = request.form.get('password', default="Error")
        accounttype = request.form.get('accounttype', default="Error")
        resp = ""
        if accounttype == "Client":
            if ClientVerifyEmail(email):
                if ClientVerifyPassword(email, password):
                    if singlepartner(email) == "Single":
                        resp = make_response(render_template('clientLanding.html', msg='hello '+email, username = email))
                    elif singlepartner(email) == "Partner":
                        resp = make_response(render_template('clientLandingPartner.html', msg='hello '+email, username = email))
                else:
                  resp = make_response(render_template('logIn.html', msg='Incorrect  password'))
            else:
                resp = make_response(render_template('logIn.html', msg='Incorrect  email'))
        elif accounttype == "IFA":
            if AdviserVerifyEmail(email):
                if AdviserVerifyPassword(email, password):
                    resp = make_response(render_template('ifaLanding.html', msg='hello '+email, username = email))
                else:
                  resp = make_response(render_template('logIn.html', msg='Incorrect  password'))
            else:
                resp = make_response(render_template('logIn.html', msg='Incorrect  email'))
        elif accounttype != "IFA" and accounttype != "Client":
            resp = make_response(render_template('logIn.html', msg='Please input account type'))
        return resp

# -- EMAIL ALREADY EXISTS? -- #


# -- CLIENT -- #

def ClientVerifyEmail(email): # checking that email is in the client_registration table
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT email FROM client_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if email in str(data):
      return email

def ClientVerifyPassword(email, password): #checking that password is in the same row in client_registration table as email
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT password FROM client_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if password in str(data):
      return password

def singlepartner(email): # checking that if single or partner account
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT singlepartner FROM client_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if str(data) == "[('Single',)]":
      return "Single"
  elif str(data) == "[('Partner',)]":
      return "Partner"

#def ClientGetName(email): #Getting the users name fronm DB
#  conn = sqlite3.connect(DATABASE)
#  cur = conn.cursor()
#  cur.execute("SELECT first_name FROM client_details WHERE email=?;", [email])
#  data = cur.fetchall()
#  conn.close()
#  return str(data)


# -- IFA -- #

def AdviserVerifyEmail(email): # checking that email is in the adviser_details table
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT email FROM adviser_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if email in str(data):
      return email

def AdviserVerifyPassword(email, password): #checking that password is in the same row in adviser_details table as email
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  cur.execute("SELECT password FROM adviser_details WHERE email=?;", [email])
  data = cur.fetchall()
  conn.close()
  if password in str(data):
      return password




if __name__ == "__main__":
   # createDB()
   # populateCustomers()
   app.run(debug=True)
   #app.run(host='0.0.0.0', port=8080)
