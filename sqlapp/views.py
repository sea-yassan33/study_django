from django.shortcuts import render

def index(request):
	params = {
		'title': 'Hell Django',
	}
	return render(request, 'index.html', params)