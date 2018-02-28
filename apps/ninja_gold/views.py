from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
		request.session['activities'] = []

	context = {
		"gold": request.session["gold"],
		"activities": request.session['activities']
	}
	return render(request, "ninja_gold/index.html", context)

def process(request):
	time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p") 
	building = request.POST['building']
	
	if request.POST['building'] == 'farm':
		gold = random.randrange(10,20+1)
		request.session['activities'].append({'activity':"You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

	elif request.POST['building'] == 'cave':
		gold = random.randrange(5,10+1)
		request.session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

	elif request.POST['building'] == 'house':
		gold = random.randrange(2,5+1)
		request.session['activities'].append({'activity': "You entered a {} and earned {} golds".format(building, gold), 'class':'win', 'date':time})

	elif request.POST['building'] == 'casino':
		gold = random.randrange(-50,50+1)
	
	if gold < 0:
		request.session['activities'].append({'activity': "You entered a {} and lost {} golds".format(building, gold), 'class': 'loss', 'date':time})
	else:
		request.session['gold'] += gold
	return redirect('/')

def reset(request):
	del request.session["gold"]
	return redirect ('/')

