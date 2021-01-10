from django.shortcuts import render

#from .models import Users  # in order to see this class on server


# Create your views here.


def index(request):
    #all_users = Users.objects.all()  # return all users
    #return render(request, 'books/index.html', {'title': 'Home page1', 'all_users': all_users})  # home page
    return render(request, 'books/index.html')

def books(request):
    return render(request, 'books/books.html') # /books

def history(request):
    return render(request, 'books/history.html') # /history
