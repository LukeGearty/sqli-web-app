from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # query = f"SELECT * FROM vulnerable_user WHERE username = '{username}' AND password = '{password}'"

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM vulnerable_user WHERE username = %s AND password = %s", [username,password]
            )
            row = cursor.fetchone()
        
        if row:
            return HttpResponse(f"Logged in as : {row[1]}")
        else:
            return HttpResponse("Login failed.")
    
    return render(request, 'login.html')


def search_users(request):
    search = request.GET.get('q', '')

    query = f"SELECT username, email FROM vulnerable_user WHERE username LIKE '%{search}'"

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    return render(request, 'results.html', {'rows': rows, 'query': query})