from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.db import connection
from schoolpro import dbhelper as db
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    t=loader.get_template("index.html")  
    return HttpResponse(t.render({"usr":checkuuser(request)}))

# def home(request):
#     return HttpResponse(t.render({"usr":checkuuser(request)}))

# def about (request):
#     return HttpResponse(t.render({"usr":checkuuser(request)}))

def principal_quotes (request):
    t=loader.get_template('principal_quotesro.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def acc_users (request):
    t=loader.get_template("acc_users.html") 
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def profile (request):
    t=loader.get_template('profile.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def contact (request):
    t = loader.get_template('contact.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def student_list (request):
    
    t = loader.get_template('student_list.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def teacher_list (request):
    
    t = loader.get_template('teacher_list.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def staff_list (request):
    
    t = loader.get_template('staff_list.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def class_timetable (request):
    t = loader.get_template('class_timetable.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def fees_system (request):
    t = loader.get_template('fees_system.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def tution_fee (request):
    t = loader.get_template('tution_fee.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def attendance_taken (request):
    t = loader.get_template('attendance_taken.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def attendance_view (request):
    t=loader.get_template('attendance_view.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def library (request):
    t=loader.get_template('library.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def office_page (request):
    t = loader.get_template('office_page.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def admin_page (request):
    t = loader.get_template('admin_page.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def admin_base_details (request):
    t = loader.get_template('base_details.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def datatable_adminpage (request):
    t = loader.get_template('datatable_adminpage.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))

def fupload(request):
    if request.method == 'POST' :
           if 'mfile' in request.FILES:
                  myfile = request.FILES['myfile']
                  fs = FileSystemStorage()
                  filename = fs.save(myfile.name, myfile)

# <!----- cource ---------------------------------------------------------->

def course (request):
    cat=[{'cat':'finance','des':'Finance'},
     {'cat':'design','des':'Design Courses'},
    {'cat':'web','des':'Web DEsign'},
    {'cat':'photo','des':'Image Editing'}]

    cs=[{'id':1,'cat':'finance','name':'Finance One','price':10},
    {'id':2,'cat':'design','name':'Design One','price':12},
    {'id':3,'cat':'web','name':'Web One','price':12},
    {'id':4,'cat':'photo','name':'Photo Gal One','price':15},
    {'id':5,'cat':'finance','name':'Finance Two','price':17},
    {'id':6,'cat':'design','name':'image Design','price':15},
    {'id':7,'cat':'web','name':'Web Design','price':18},
    {'id':7,'cat':'photo','name':'Photoshop Design','price':18}]
    t=loader.get_template('courses.html')
    return HttpResponse(t.render({'clist':cat,'cdata':cs,"usr":checkuuser(request)}))

def login(request):
    stat=''
    d = loader.get_template("login.html")
    if request.method == "POST":
        print(request.POST)
 
        email = request.POST['uname']
        pwd= request.POST['pwd']
        sql = f"SELECT * FROM logintab WHERE email='{email}' AND pwd='{pwd}' LIMIT 1"
        user,err=db.getdata(sql,True)
        if user:
            print(user)
            print("Successfully Login")
            request.session['luser']={'email':email,'name':user['email']}

            return HttpResponseRedirect("/",request)
        else:
            stat="Invalid Login.."
            if err:
                stat+="error ..in signing in..!"
            else:
                stat+="..user or password does not exists..!"


    return HttpResponse(d.render({},request))

def admin_login(request):
    stat=''
    d = loader.get_template("admin_login.html")
    if request.method == "POST":
        print(request.POST)
        ad_uname = request.POST['ad_uname']
        ad_pwd= request.POST['ad_pwd']
        sql = f"SELECT * FROM tbl_admin_signup WHERE adm_username='{ad_uname}' AND adm_pwd='{ad_pwd}' LIMIT 1"
        user,err=db.getdata(sql,True)
        if user:
            print(user)
            print("Successfully Login")
            # request.session['luser']={'adm_username':ad_uname,'adm_name':user['adm_email']}
            # request.session['luser']={'ad_uname':ad_uname,'name':user['adm_username']}
            return HttpResponseRedirect("/admin_page/",request)
        else: 
            stat="Invalid Login.."
            if err:
                stat+="error ..in signing in..!"
            else:
                stat+="..user /password  does not exists..!"

    return HttpResponse(d.render({},request))

def office_login(request):
    stat=''
    d = loader.get_template("office_login.html")
    if request.method == "POST":
        print(request.POST)
        email = request.POST['uname']
        pwd= request.POST['pwd']
        # image= request.POST['image']
        sql = f"SELECT * FROM office_login WHERE email='{email}' AND pwd='{pwd}' LIMIT 1"
        user,err=db.getdata(sql,True)
        if user:
            print(user)
            print("Successfully Login")
            request.session['luser']={'email':email,'name':user['email']}

            return HttpResponseRedirect("/office_page/",request)

        else:
            stat="Invalid Login.."
            if err:
                stat+="error ..in signing in..!"
            else:
                stat+="..user /password  does not exists..!"


    return HttpResponse(d.render({},request))


def checkuuser(request):
    luser = ''
    if request.session.has_key('luser'):
        luser=request.session['luser']
    return luser

def logout(request):
    if request.session.has_key('luser'):
        del request.session['luser']
    return HttpResponseRedirect('/', request)
def signup(request):
    stat=''
    d={}
    t = loader.get_template("signup.html")
    if request.method == "POST":
        print(request.POST)
        email = request.POST['uname']
        pwd= request.POST['pwd']
        d={'email':email}
        rval,err=db.getdata(f"select * from logintab where email='{email}' LIMIT 1",True)
        if rval:
            stat="This user already exists..hi you've already registered with us..!"

        else:
            sql = f"INSERT INTO logintab(email,pwd)VALUES('{email}','{pwd}')"
            rval,err=db.updatedata(sql)
            if rval:
                return HttpResponseRedirect("/login/",request)
            else:
                stat="Unable to signup..!.."
                if err:
                    stat+='error occured..!'
                else:
                    stat+=" ..make sure you have provided proper values..!"     

    return HttpResponse(t.render({'msg':stat,'data':d}, request))

def admin_signup(request):
    stat=''
    d={}
    t = loader.get_template("admin_signup.html")
    if request.method == "POST":
        print(request.POST)
        ad_id = request.POST['ad_id']
        ad_name = request.POST['ad_name']
        ad_email = request.POST['ad_email']
        ad_phone = request.POST['ad_phone']
        ad_uname = request.POST['ad_uname']
        ad_pwd= request.POST['ad_pwd']
        ad_con_pwd = request.POST['ad_conf_pwd']
        d={'email':ad_email}
        rval,err=db.getdata(f"select * from admin_login where email='{ad_email}' LIMIT 1",True)
        if rval:
            stat="This user already exists..hi you've already registered with us..!"

        else:
            sql = f"INSERT INTO tbl_admin_signup(adm_id,adm_name,adm_mobnum,adm_email,adm_username,adm_pwd)VALUES('{ad_id}','{ad_name}','{ad_phone}','{ad_email}','{ad_uname}','{ad_pwd}')"
            rval,err=db.updatedata(sql)
            if rval:
                return HttpResponseRedirect("/admin_login/",request)
            else:
                stat="Unable to signup..!.."
                if err:
                    stat+='error occured..!'
                elif ad_pwd != ad_con_pwd:
                    raise ValueError("password and confirm_password does not match")
                else:
                    stat+=" ..make sure you have provided proper values..!"

    return HttpResponse(t.render({'msg':stat,'data':d}, request))

def office_signup(request):
    stat=''
    d={}
    t = loader.get_template("office_signup.html")
    if request.method == "POST":
        print(request.POST)
        email = request.POST['uname']
        pwd= request.POST['pwd']
        d={'email':email}
        rval,err=db.getdata(f"select * from office_login where email='{email}' LIMIT 1",True)
        if rval:
            stat="This user already exists..hi you've already registered with us..!"

        else:
            sql = f"INSERT INTO office_login(email,pwd)VALUES('{email}','{pwd}')"
            rval,err=db.updatedata(sql)
            if rval:
                return HttpResponseRedirect("/office_login/",request)
            else:
                stat="Unable to signup..!.."
                if err:
                    stat+='error occured..!'
                else:
                    stat+=" ..make sure you have provided proper values..!"

    return HttpResponse(t.render({'msg':stat,'data':d}, request))


def student_reg (request):
    # cs=[{'cid':1,'name':'BSc Botony'},{'cid':2,'name':'BSc Zoology'},
    # {'cid':3,'name':'BA English'}]
    t=loader.get_template('student_reg.html') 
    stat=''
    cs,err=db.getdata('SELECT * FROM cource_cat')
    if not cs:
        stat="unable to retrieve course data..!.."
        if err:
            stat+="error occured..!"
    if request.method=='POST':

        sql=f"INSERT INTO student_reg(fname,lname,dob,emailid,mobile,gender,address,city,\
        pincode,state,country,hobbies,qualification,applied,class_x_board,class_x_pr,class_x_year,\
        class_xii_board,class_xii_pr,class_xii_year,grad_board,grad_pr,grad_year,mast_board,mast_pr,mast_year)\
        VALUES('fname','lname','dob','emailid','mobile','gender','address','city','pincode','state','country',\
        'hobbies','qualification','applied','class_x_board','class_x_pr','class_x_year',\
        'class_xii_board','class_xii_pr','class_xii_year','grad_board,grad_pr','grad_year','mast_board','mast_pr','mast_year')"
        rval,err=db.updatedata(sql,True)#true newly inserted identity column value
        if not rval:
            stat="unable to register ..!.."
            if err:
                stat+="error occured..!"
        else:
            pass
            #insert into exam passed,coursemark etc with rval as foreign key value

    return HttpResponse(t.render({'msg':stat,'cl':cs,"usr":checkuuser(request)}))
    return HttpResponseRedirect("/office_page/",request)

def teacher_reg (request):
    t = loader.get_template('teacher_reg.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))
    return HttpResponseRedirect("/office_page/",request)

def staff_reg (request):
    t = loader.get_template('staff_reg.html')
    return HttpResponse(t.render({"usr":checkuuser(request)}))
    return HttpResponseRedirect("/office_page/",request)
