from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from myapp.forms import InputForm
from myapp.forms import LogForm
from myapp.models import Menu


def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)


# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info
#
#     response = HttpResponse()
#     response.headers['Age'] = 20
#
#     msg = f"""<br>
#                 <br>Path: {path}
#                 <br>Address: {address}
#                 <br>Scheme: {scheme}
#                 <br>Method: {method},
#                 <br>User agent: {user_agent}
#                 <br>Path_info: {path_info}
#                 <br>Response: {response.headers}"""
#     return HttpResponseNotFound(msg, content_type='text/html', charset='utf-8')


def display_date(request):
    data_joined = datetime.today().year
    return HttpResponse(data_joined)


# def menu(request):
#     mew_menu = {'mains': [
#         {'name': "falafel", 'price': "12"},
#         {'name': "shawarma", 'price': "15"},
#         {'name': "gyro", 'price': "10"},
#         {'name': "hummus", 'price': "5"},
#     ]}
#     return render(request, "menu.html", mew_menu)
def home(request):
    return render(request, "index.html")


# def about(request):
#     about_content = {
#         'about': "Base in Chicago, Illinois, Little Lemon is a family owned Mediterranean restaurant, focused on traditional recipes "
#                  " served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12-15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with "
#                  " moderate prices, making it a popular place for a meal any time of the day."}
#     return render(request, "partials/../templates/about.html", about_content)
def about(request):
    return render(request, "about.html")


def menu(request):
    return render(request, "menu.html")


def menu_by_id(request):
    new_menu = Menu.objects.all()
    new_menu_dict = {'menu1': new_menu}  # create dictionary
    return render(request, 'menu_cards.html', new_menu_dict)


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", main_data)
