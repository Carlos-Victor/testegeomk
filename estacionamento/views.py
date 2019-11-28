from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    consulta = list(requests.get("http://localhost:8163/api/").json())
    return render(request,'index.html', {'consulta': consulta})