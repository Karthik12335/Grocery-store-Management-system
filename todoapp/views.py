
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoapp.models import Product
from django.db.models import Q
from todoapp.forms import Empform,ProductForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def index(request):
    #return HttpResponse("<b>Hello from Index</b>")
    return redirect('/index')





def username(request,username):
    return HttpResponse("User_name is: "+username)


def home(request):
    content={}
    #content['x'] = 'Itvedant Eclass'
    #content['y'] = '100'
    #content['x'] = 100
    #content['y'] = 160
    content['data'] = [10,20,30,40,50,60]
    return render(request,'index.html',content)

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')



'''
return statement returns response object.
Reponse object is created by using
1) HttpResponse() : it is used to craete response object and the object 
                    is returned to client
2) render()

render():

    1.this function can return html file as response 
    render(request,'htmlfile',data)
'''

#Product Management system

def dash_product(request):
    user_id=request.user.id 

    if request.method=="POST":
        #retrive data sent from the form into python variable and and store it in a database
        pname=request.POST['pname']
        desc=request.POST['pdesc']
        price=request.POST['pprice']
        cat=request.POST['cat']
        p1=Product(name=pname,pdesc=desc,price=price,cat=cat,is_deleted="N",uid=user_id)
        p1.save()
        return redirect('/pdashboard')


    else:
        #show empty form
        #rec=Product.objects.all()
        q1=Q(is_deleted='N')
        q2=Q(uid=user_id)
        rec=Product.obj1.filter(q1 & q2)
        #rec=Product.obj1.filter(is_deleted="N",uid=user_id)
        content={}
        content['data']=rec
        
        return render(request,'product_dashboard.html',content)


def delete(request,rid):
    #x=Product.objects.get(id=rid)
    #x.delete()

    #soft delete
    x=Product.obj1.filter(id=rid)
    x.update(is_deleted="Y")
    return redirect('/pdashboard')


def edit(request,rid):
    #str1="Hello from edit function"
    if request.method=='POST':
        uname=request.POST['pname']
        udesc=request.POST['pdesc']
        uprice=request.POST['pprice']
        ucat=request.POST['cat']
        x=Product.obj1.filter(id=rid)
        x.update(name=uname,pdesc=udesc,price=uprice,cat=ucat)
        return redirect('/pdashboard')
    else:

        ret=Product.obj1.get(id=rid)
        content={}
        content['data']=ret
        return render(request,'editproduct.html',content)

'''
def filter_electronic(request):
    q1=Q(cat="E")
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

def filter_grocery(request):
    q1=Q(cat="G")
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

def filter_cloths(request):
    q1=Q(cat="C")
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)
'''

def filter(request,vcat):
    if vcat == "elec":
        f = 'E'
    elif vcat == "groc":
        f = 'G'
    elif vcat == "cloth":
        f = 'C'
    q1=Q(cat=f)
    q2=Q(is_deleted="N")
    rec=Product.obj1.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

def pfilter(request,p):
    if p == ">10000":
        q1=Q(price__gte=10000)
    elif p == "<10000":
        q1=Q(price__lte=10000)
    q2=Q(is_deleted="N")
    rec=Product.obj1.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)


def sort(request,sv):
    if sv=='htol':
        #rec=Product.objects.filter(is_deleted="N").order_by("-price")
        rec=Product.cobj1.sortfilterdesc()
    elif sv=='ltoh':
        #rec=Product.objects.filter(is_deleted="N").order_by("price")
        rec=Product.cobj1.sortfilterasc()
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)



def prange(request):

    if request.method=='POST':
        min=request.POST['from']
        max=request.POST['to']
        #print(min)
        #print(max)
        q1=Q(price__gte=min)
        q2=Q(price__lte=max)
        q3=Q(is_deleted="N")
        rec=Product.obj1.filter(q1 & q2 & q3)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)   


def formapi(request):
    if request.method=='POST':
        return HttpResponse("In the POST section")
    else:
        emf=Empform()
        return render(request,'fromapi.html',{'form':emf})

def modelform(request):
    if request.method=='POST':
        return HttpResponse("In the POST section")
    else:
        mf=ProductForm()
        return render(request,'modelform.html',{'mform':mf})


def register(request):
    if request.method=='POST':
        rdata=RegisterForm(request.POST)
        #print(rdata)
        if rdata.is_valid():
            rdata.save()
            return redirect('/login')
        else:
            return HttpResponse("user not register")
        

    else:

        #rmf=UserCreationForm()
        rmf=RegisterForm()
        return render(request,'register.html',{'rform':rmf})


def user_login(request):

    if request.method=='POST':

        lfm=AuthenticationForm(request=request,data=request.POST)
        if lfm.is_valid():
            uname=lfm.cleaned_data['username']
            upass=lfm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            if u:
                login(request,u) #It start session for that logged in user and store id of that user in the session.
                return redirect('/pdashboard')
        else:

            return HttpResponse('Invalid username or password!')

    else:

        lfm=AuthenticationForm()
        print("In user_login else part")
        return render(request,'login.html',{'lform':lfm})


def setcookie(request):
    r=render(request,'setcookie.html')
    r.set_cookie('name','ITVEDANT')
    r.set_cookie('rno','35')
    return r

def getcookie(request):
    #data=request.COOKIES['name']
    data={}
    data['n']=request.COOKIES['name']
    data['r']=request.COOKIES['rno']

    #return render(request,'getcookie.html',{'d':data})
    return render(request,'getcookie.html',data)




def setsession(request):
    request.session['user']="ITVEDANT"
    return render(request,'setsession.html')

def getsession(request):
    d=request.session['user']
    return render(request,'getsession.html',{'data':d})


def user_logout(request): 

    logout(request) # This function destroys session
    return redirect('/login')