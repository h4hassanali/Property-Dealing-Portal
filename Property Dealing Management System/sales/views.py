from django.contrib.auth.models import User
from django.shortcuts import render
# from django.templatetags import static
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages, auth
# from django.core.files import File
import psycopg2
# Create your views here.
def index(request):
    return render(request,'index.html')

def add_prop(request):
    return render(request,'add_prop.html')
    return HttpResponse("Add Prop")
def home_delete(request):
    delete = request.POST.get('delete')
    if len(delete) != 0:
        return redirect('/del_rec')
def home_search(request):
    search = request.POST.get('search')
    if len(search) != 0:
        return redirect('/search_property')
def home_add(request):
    add = request.POST.get('add')
    if len(add) != 0:
        return redirect('/add_prop')

def add_new(request):
    p_no = request.POST.get('p_no')
    s_treet = str(request.POST.get('street'))
    c_ity = request.POST.get('city')
    p_ostcode = request.POST.get('postcode')
    t_ype = request.POST.get('type')
    r_ooms = request.POST.get('rooms')
    r_ent = request.POST.get('rent')
    o_no = request.POST.get('o_num')

    conn = psycopg2.connect(database="dreamhomeproperty", user="postgres", password="hassan", host="127.0.0.1",port="5432")
    cur = conn.cursor()
    cur.execute("""INSERT INTO dreamhome_schema.property_for_rent (property_n,street,city,postcode,typee,rooms,rent,owner_number) \
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""",(p_no,s_treet,c_ity,p_ostcode,t_ype,r_ooms,r_ent,o_no))
    conn.commit()
    conn.close()
    return HttpResponse("Data Saved into table of database")

def search_property_for_rent(request):
    return render(request,'search_property.html')
def search_result(request):
    pr_num = int(request.POST.get('pr_no'))
    conn = psycopg2.connect(database="dreamhomeproperty", user="postgres", password="hassan", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    cur.execute(f''' SELECT * FROM dreamhome_schema.property_for_rent WHERE property_n={pr_num}''')
    rows = cur.fetchall()
    result = []
    for t in rows: #list of tuples into single list
        for x in t:
            result.append(x)
    cur.close()
    if len(result) == 0:
        return HttpResponse("<h1>NO RECORD FOUND </h1>")
    else:
        p_n = result[0]
        street = result[1]
        city = result[2]
        postcode = result[3]
        typee = result[4]
        rooms = result[5]
        rent = result[6]
        o_n = result[7]
        return render(request, 'searched.html', {
            'p_n': p_n,
            'street': street,
            'city': city,
            'postcode': postcode,
            'type': typee,
            'rooms': rooms,
            'rent': rent,
            'o_n': o_n
        })

def del_record(request):

    return render(request,'del.html')

def del_confirm(request):
    pr_num = int(request.POST.get('pr_no'))
    conn = psycopg2.connect(database="dreamhomeproperty", user="postgres", password="hassan", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    cur.execute(f''' DELETE FROM dreamhome_schema.property_for_rent WHERE property_n={pr_num}''')
    conn.commit()
    cur.close()
    return render(request,'del_confirm.html')
def login(request):
    if request.method == 'POST':
        u_name = str(request.POST.get('username'))
        pas = str(request.POST.get('password'))
        user = authenticate(username=u_name,password=pas)
        u1 = "admin"
        u2 = 'user'
        if user is not None:
            auth.login(request,user)
            if u1 in u_name:
                return redirect('/index')
            elif u2 in u_name:
                return redirect('/search_owner_prop')

        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        e_mail = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password, email=e_mail)
        user.save()
        return HttpResponse("User created")
    else:
        return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def search_owner_prop(request):
    if request.method == 'POST':
        o_no = request.POST.get('owner_num')
        conn = psycopg2.connect(database="dreamhomeproperty", user="postgres", password="hassan", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute(f''' SELECT property_for_rent.property_n,private_owner.fname,property_for_rent.street,property_for_rent.rooms,property_for_rent.typee FROM dreamhome_schema.property_for_rent 
INNER JOIN dreamhome_schema.private_owner
ON property_for_rent.owner_number={o_no} AND private_owner.owner_no={o_no}''')
        rows = cur.fetchall()
        conn.close()
        if len(rows) != 0:
            return render(request, 'owner_with_prop.html', {'data': rows})
        else:
            return HttpResponse("No Record Found")
    else:
        return render(request, 'search_owner_prop.html')





