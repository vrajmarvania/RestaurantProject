from datetime import date, datetime, timedelta

from MySQLdb.constants.FIELD_TYPE import NULL
from django.db.models import Count, Sum
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from pyasn1.type.univ import Null
from reportlab.pdfgen import canvas

from .models import Admin_Register, RestaurantData, Food, Product, Ordert


def index(request):
    RD = RestaurantData.objects.all()

    # For Month data

    today = date.today()
    month = today.month
    Data = Ordert.objects.filter(ODate__month=month)
    Ms = 0.00
    for i in Data:
        if i.TPrice != '':
            Ms = Ms + float(i.TPrice)

    # for Day data

    today = str(date.today())
    Data = Ordert.objects.filter(ODate=today)
    ds = 0.00
    for i in Data:
        if i.TPrice != '':
            ds = ds + float(i.TPrice)

    # for year data
    one_week_ago = datetime.today() - timedelta(days=7)
    O = Ordert.objects.filter(ODate__gte=one_week_ago)

    ans = 0.00
    for i in O:
        if i.TPrice != '':
            ans = ans + float(i.TPrice)

    # top dish

    a = Product.objects.values_list('ProductName').annotate(count=Count('ProductName')).order_by('count')
    a = a.reverse()
    Ro = Ordert.objects.all()



    #
    labels = []
    data = []
    a = Product.objects.values_list('ProductName').annotate(count=Count('ProductName')).order_by('count')
    a = a.reverse()
    for i in a:
        labels.append(i[0])
        data.append(i[1])



    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

    labels2 = []
    data2 = []

    Data = RestaurantData.objects.all()
    for a in Data:
        labels2.append(a.RestaurantName)



    for R in labels2:
        Data = Ordert.objects.filter(RestaurantName=R)
        temp = 0.00
        if Data != '':
            for j in Data:
                if j.TPrice != '':
                    temp = temp + float(j.TPrice)
        data2.append(temp)





    params = {'ro':Ro,'RestaurantData': RD, 'Ds': ds, 'Ms': Ms, 'a': a, 'Ys': ans,'data':data,'labels':labels,'labels1': labels2,'data1': data2}
    return render(request, 'index.html',params,)


def register(request):
    return render(request, 'register.html')


def registerform(request):
    if request.method == "POST":
        Admin_NameF = request.POST.get('FirstName', '')
        Admin_NameL = request.POST.get('LastName', '')
        Admin_Email = request.POST.get('InputEmail', '')
        Admin_Password = request.POST.get('InputPassword', '')
        Admin_PasswordC = request.POST.get('RepeatPassword', '')
        register = Admin_Register(Admin_NameF=Admin_NameF, Admin_NameL=Admin_NameL, Admin_Email=Admin_Email, Admin_Password=Admin_Password, Admin_PasswordC=Admin_PasswordC)
        register.save()

    return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def loginc(request):
    if request.method == "POST":
        Admin_Email = request.POST.get('InputEmail', '')
        Admin_Password = request.POST.get('InputPassword', '')
        register = Admin_Register.objects.filter(Admin_Email=Admin_Email, Admin_Password=Admin_Password)
        if len(register) > 0:
            return redirect('http://127.0.0.1:8000/a/index')
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

    # Month
    today = date.today()
    month = today.month
    Data = Ordert.objects.filter(ODate__month=month, RestaurantName=R)
    Ms = 0.00
    for k in Data:
        if k.TPrice != '':
            Ms = Ms + float(k.TPrice)


    # for weeek

    one_week_ago = datetime.today() - timedelta(days=7)
    O = Ordert.objects.filter(RestaurantName=R, ODate__gte=one_week_ago)
    # Data = Ordert.objects.filter(ODate=today, RestaurantName=R)
    ans = 0.00
    for l in O:
        if l.TPrice != '':
            ans = ans + float(l.TPrice)





 # for Restorent dishis data
    hd=[]
    labels = []
    data = []
    a=Food.objects.filter(RestaurantId=R)
    for z in a:
      hd.append(z.FoodName)
    c= Product.objects.values_list('ProductName').annotate(count=Count('ProductName')).order_by('count')
    for a in range(len(c)):
        for m in range(len(hd)):
            if(c[a][0]==hd[m]):
               labels.append(c[a][0])
               data.append(c[a][1])

    l2 = []
    d1 = []
    c = Ordert.objects.filter(RestaurantName=R).values_list('ODate', ).annotate(Sum('TPrice'))
    for c1 in c:
        l2.append(str(c1[0]))
        d1.append(c1[1])


    Data = Ordert.objects.filter(RestaurantName=R)


    params = {'i': i, 'T': temp, 'ans': ans, 'Ms': Ms,'da':data,'la':labels,'la1':l2,'da1':d1,'Data':Data}

    return render(request, 'Restorent.html', params)


def AddRestaurant(request):
    if request.method == "POST":
        RestaurantName = request.POST.get('RestaurantName')
        RestaurantAddress = request.POST.get('RestaurantAddress')
        RestaurantCode = request.POST.get('RestaurantCode')
        restaurantData = RestaurantData(RestaurantAddress=RestaurantAddress, RestaurantName=RestaurantName,ucode=RestaurantCode)
        restaurantData.save()
        return render(request, 'index.html')
    Data = RestaurantData.objects.all()
    params = {'Data': Data}
    return render(request, 'AddRestaurant.html', params)


def AddFood(request):
    if request.method == "POST":
        FoodName = request.POST.get('FoodName', '')
        FoodPrice = request.POST.get('FoodPrice', '')
        RestaurantId = request.POST.get('RestaurantName', '')
        i = Food.objects.filter(FoodName=FoodName)
        food = Food(FoodPrice=FoodPrice, RestaurantId=RestaurantId, FoodName=FoodName)
        if len(i) < 1:
            food.save()
            return render(request, 'index.html')
        else:
            return render(request, 'AddFood.html')

    Data = Food.objects.all()
    params = {'Data': Data}
    return render(request, 'AddFood.html', params)


def Order(request):
    RD = RestaurantData.objects.all()
    params = {'RestaurantData': RD}

    return render(request, 'Order.html', params)


def NewOrder(request, i):
    j = Food.objects.filter(RestaurantId=i)
    Ro = Ordert.objects.all(RestaurantName=i)
    params = {'Foods': j, 'Restorent': i,'Ro':Ro}

    return render(request, 'NewOrder.html', params)


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
    return render(request, 'Invoice.html', params)


def DeleteF(request, i):
    Food.objects.get(FoodId=i).delete()
    return render(request, 'AddFood.html')


def DeleteR(request, i):
    RestaurantData.objects.get(RestaurantId=i).delete()
    return render(request, 'AddRestaurant.html')


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

    params = {'RestaurantData': RD, 'Ds': temp, 'Ms': Ms, 'a': a, 'Ys': ans}

    return render(request, 'RestorentDetails.html', params)

# RestorentDetails


def test(request):
    l2=[]
    d1= []
    c = Ordert.objects.filter(RestaurantName='lol').values_list('ODate',).annotate(Sum('TPrice'))
    for c1 in c:
      l2.append(str(c1[0]))
      d1.append(c1[1])







    return render(request, 'test.html', {
        'labels': l2,
        'data': d1,
    })

