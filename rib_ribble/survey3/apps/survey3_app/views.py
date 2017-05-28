from django.shortcuts import render, redirect

def index(request):
	if 'counter' not in request.session:
		request.session['counter'] = 0

	return render(request, "survey3_app/index.html")

def input(request):
	request.session['counter'] += 1

	context = {
		'name': request.POST['name'],
		'location': request.POST['location'],
		'language': request.POST['language'],
		'comment': request.POST['comment']
	}

	return render(request, 'survey3_app/result.html', context)


