from django.shortcuts import render

def index(request):

	return render(request, 'wall2_app/index.html')
