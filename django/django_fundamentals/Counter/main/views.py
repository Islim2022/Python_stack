from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'key_name' in request.session:
        request.session['key_name'] += 1
    else:
        request.session['key_name'] = 0
    return render(request, "index.html")

def reset(request):
    del request.session['key_name']
    return redirect("/")

def addtwo(request):
    if 'key_name' in request.session:
        request.session['key_name'] += 1
    else:
        request.session['key_name'] = 1
    return redirect('/')