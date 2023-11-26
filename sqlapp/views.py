from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm

def index(request):
	msg = 'データ一覧'
	data = []

	if(request.method == 'POST'):
		obj = Customer()
		form = CustomerForm(request.POST, instance=obj)
		form.save()
		msg = 'データを登録しました'
	
	data = Customer.objects.all()

	params = {
		'title': 'Hell Django',
		'message': msg,
		'form': CustomerForm(),
		'data' : data,
	}
	return render(request, 'index.html', params)