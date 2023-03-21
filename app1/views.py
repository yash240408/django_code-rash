from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'api_test_add.html')
@csrf_exempt
def add(request):
    if request.method == 'POST':
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        params = {"f_name": f_name, "l_name": l_name,
                  "email": email, "password": password}
        post_url = requests.post(
            'http://coderashapi.mywebcommunity.org/data_add.php', data=params)
        response = post_url.json()
        context={"message":response['message']}
    return render(request,'api_test_add.html', context)
@csrf_exempt
def fetch(request):
    post_url = requests.get(
        'http://coderashapi.mywebcommunity.org/data_fetch.php')
    response = post_url.json()
    context={"message":response["message"],"data":response['data']}
    return render(request,'api_test_fetch.html', context)
