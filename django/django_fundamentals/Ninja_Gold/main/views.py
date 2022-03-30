from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random

def index(request):
  # del request.session['user_log']
  # del request.session['user_money']
  if 'ninja_money' in request.session:
    print('ninja_money =')
    request.session['ninja_money'] 
    pass
  else:
    request.session['ninja_money'] = 0
    request.session['ninja_log'] = []
  return render(request,"index.html")

def process_money(request):
  if request.POST['form'] == 'farm':
    random_number = random.randint(10,20)
    request.session['ninja_log'].append(f'Earned {random_number} golds from the Farm! ({strftime("%Y/%m/%d")} - {strftime("%I:%M %p", localtime())})')
    request.session['ninja_money'] += random_number
  
  elif request.POST['form'] == 'cave':
    random_number = random.randint(5,10)
    request.session['ninja_log'].append(f'Earned {random_number} golds from the Cave! ({strftime("%Y/%m/%d")} - {strftime("%I:%M %p", localtime())})')
    request.session['ninja_money'] += random_number
    
  elif request.POST['form'] == 'house':
    random_number = random.randint(2,5)
    request.session['ninja_log'].append(f'Earned {random_number} golds from the Cave! ({strftime("%Y/%m/%d")} - {strftime("%I:%M %p", localtime())})')
    request.session['ninja_money'] += random_number
  
  else:
    random_number = random.randint(-50,50)
    request.session['ninja_money'] += random_number
    if random_number >= 0:
      request.session['ninja_log'].append(f'Earned {random_number} golds from the Casino! ({strftime("%Y/%m/%d")} - {strftime("%I:%M %p", localtime())})')
    else:
      request.session['ninja_log'].append(f'Lost {random_number * -1} golds from the Casino! ({strftime("%Y/%m/%d")} - {strftime("%I:%M %p", localtime())})')
  return redirect('/')
