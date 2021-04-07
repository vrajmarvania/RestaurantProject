from datetime import date, datetime, timedelta

from MySQLdb.constants.FIELD_TYPE import NULL
from django.db.models import Count
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from pyasn1.type.univ import Null
from reportlab.pdfgen import canvas

from Restaurant.models import Ordert,User_Register,Admin_Register, RestaurantData, Food, Product, Ordert,Restaurantl

def User_login(request):
    RD = RestaurantData.objects.all()
    params = {'RestaurantData': RD}


    return render(request, 'User_login.html',params)

def User_register(request):
    return render(request, 'User_register.html')


def User_register(request):
    return render(request, 'User_register.html')


def User_registerform(request):
    if request.method == "POST":
        User_NameF = request.POST.get('FirstName', '')
        User_NameL = request.POST.get('LastName', '')
        User_Email = request.POST.get('InputEmail', '')
        User_Password = request.POST.get('InputPassword', '')
        User_PasswordC = request.POST.get('RepeatPassword', '')
        register = User_Register(User_NameF=User_NameF, User_NameL=User_NameL, User_Email=User_Email, User_Password=User_Password, User_PasswordC=User_PasswordC)
        register.save()

    return render(request, 'User_login.html')


def a(request):
    RD = Ordert.objects.all()
    params = {'RestaurantData': RD}
    return render(request, 'allorder.html',params)


def loginc(request):
    if request.method == "POST":
        User_Email = request.POST.get('InputEmail', '')
        User_Password = request.POST.get('InputPassword', '')
        Rcode = request.POST.get('code')
        Rname = request.POST.get('name')
        print(Rname)
        print(Rcode)
        register = User_Register.objects.filter(User_Email=User_Email, User_Password=User_Password)
        RC = RestaurantData.objects.filter(ucode=Rcode, RestaurantName=Rname)
        print(RC)
        if len(register )>0 and len(RC)>0:
            return redirect('http://127.0.0.1:8000/NewOrder/'+Rname)
        else:
            return render(request, '404.html')
    return redirect('http://127.0.0.1:8000/index')


def logout(request):
    return render(request, 'logout.html')


def forgotp(request):
    return render(request, 'forgot-password.html')


def Restorent(request, i):
    i = RestaurantData.objects.filter(RestaurantId=i)

    for I in i:
        if I != '':
            R = I.RestaurantName

        # for day
    today = str(date.today())
    Data = Ordert.objects.filter(ODate=today, RestaurantName=R)

    temp = 0.00
    if Data != '':
        for j in Data:
            if j.TPrice != '':
                temp = temp + float(j.TPrice)
    # print(temp)

    # Month
    today = date.today()
    month = today.month
    Data = Ordert.objects.filter(ODate__month=month, RestaurantName=R)
    Ms = 0.00
    for k in Data:
        if k.TPrice != '':
            Ms = Ms + float(k.TPrice)
            # print(i.TPrice)

    # for weeek

    one_week_ago = datetime.today() - timedelta(days=7)
    O = Ordert.objects.filter(RestaurantName=R, ODate__gte=one_week_ago)
    # Data = Ordert.objects.filter(ODate=today, RestaurantName=R)
    ans = 0.00
    for l in O:
        if l.TPrice != '':
            ans = ans + float(l.TPrice)
    # print(ans)

    params = {'i': i, 'T': temp, 'ans': ans, 'Ms': Ms}

    return render(request, 'Restorent.html', params)




def UData(request):
    i='lol'
    Data = Ordert.objects.filter(RestaurantName=i)
    params = {'Data': Data}
    return render(request, 'UData.html', params)

def Order(request):
    RD = RestaurantData.objects.all()
    params = {'RestaurantData': RD}

    return render(request, 'Order.html', params)

def up(request):
    ID = request.POST.get('ID')
    RN = request.POST.get('RN')
    OD = request.POST.get('OD')
    TP = request.POST.get('TP')
    print(ID)
    print(RN)
    print(OD)
    print(TP)

    return render(request, 'UData.html')


def NewOrder(request, i):
    j = Food.objects.filter(RestaurantId=i)
    Ro = Ordert.objects.filter(RestaurantName=i)
    params = {'Foods': j, 'Restorent': i,'Ro':Ro}

    return render(request, 'NewOrder.html', params)






def UpdateF(request):
    Name = request.POST.get('Name', '')
    FoodName = request.POST.get('FoodName', '')
    FoodPrice = request.POST.get('FoodPrice', '')
    RestaurantId = request.POST.get('RestaurantName', '')
    Food.objects.filter(FoodName=Name).update(FoodName=FoodName, FoodPrice=FoodPrice, RestaurantId=RestaurantId)
    return redirect('http://127.0.0.1:8000/AddFood')


def UpdateR(request):
    Name = request.POST.get('Name', '')
    RestaurantName = request.POST.get('RestaurantName', '')
    RestaurantAddress = request.POST.get('RestaurantAddress', '')
    t = RestaurantData.objects.get(RestaurantName=Name)

    t.RestaurantName = RestaurantName
    t.RestaurantAddress = RestaurantAddress
    t.save()
    return redirect('http://127.0.0.1:8000/AddRestaurant')


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def RestorentDetails(request):
    RD = RestaurantData.objects.all()

    # For Month data

    today = date.today()
    month = today.month
    Data = Ordert.objects.filter(ODate__month=month)
    Ms = 0.00
    for i in Data:
        if i.TPrice != '':
            Ms = Ms + float(i.TPrice)
            # print(i.TPrice)

    # for Day data

    today = str(date.today())
    Data = Ordert.objects.filter(ODate=today)
    temp = 0.00
    if Data != '':
        for i in Data:
            if i.TPrice != '':
                temp = temp + float(i.TPrice)

    # for year data
    one_week_ago = datetime.today() - timedelta(days=7)
    O = Ordert.objects.filter(ODate__gte=one_week_ago)

    ans = 0.00
    for i in O:
        if i.TPrice != '':
            ans = ans + float(i.TPrice)

    # top dish

    a = Product.objects.values_list('ProductName').annotate(count=Count('ProductName')).order_by('count')
    courses = a
    print(a[1][0])
    # print(a.ProductName.ProductName)
    params = {'RestaurantData': RD, 'Ds': temp, 'Ms': Ms, 'a': a, 'Ys': ans}

    return render(request, 'RestorentDetails.html', params)

# RestorentDetails

def Norder(request, i):
    if request.method == "POST":
        x = 0

        data = []
        j = Food.objects.filter(RestaurantId=i)
        for m in j:
            name = m.FoodName + "Name"
            price = m.FoodName + "price"
            qty = m.FoodName + "qty"
            qp = m.FoodName + "QP"
            Name = request.POST.get(name, '')
            Price = request.POST.get(price, '')
            Qty = request.POST.get(qty, '')
            QP = request.POST.get(qp, '')

            today = date.today()
            Tpric = request.POST.get('Total_Amount', '')
            if Qty != '':
                p = Product(ProductName=Name, ProductQty=Qty, ProductPrice=Price, QP=QP)
                p.save()

                data.append({'ProductName': Name, 'ProductQty': Qty, 'ProductPrice': Price, 'QP': QP})

                if x == 0:
                    o = Ordert(TPrice=Tpric, RestaurantName=i)

                    o.save()
                    x = 1
                if x != 0:
                    o.Allproduct.add(p)

        params = {'Data': data, 'Tprice': Tpric, 'Date': today, 'Name': i}
        print(params)
    return render(request, 'Invoice.html', params)

