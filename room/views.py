from asyncio.windows_events import NULL
from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    r = requests.get('https://sheet.best/api/sheets/54c0bb23-8546-44bc-8591-9087e227d346')
    books = r.json()
    droplet_list = []
    x = len(books)
    for i in range(x):
        droplet_list.append(books[i])
    return render(request,'room/index.html',{'books':droplet_list})
 
def friends(request):
    gvnstr = request.POST.get('gvn')
    if request.POST.get('block') != NULL:
      block = request.POST.get('block')
    gvnstr = str(gvnstr)
    r = requests.get('https://sheet.best/api/sheets/54c0bb23-8546-44bc-8591-9087e227d346')
    books = r.json()
    droplet_list = []
    x = len(books)
    for i in range(x):
        droplet_list.append(books[i])
    newdrop = droplet_list
    return render(request,'room/roommate.html',{'books':droplet_list,'gvnstr':gvnstr,'block':block,'book':newdrop})