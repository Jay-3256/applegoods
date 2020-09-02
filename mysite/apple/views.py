from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Item
from .forms import *

# Create your views here.
def index(request):
	items = Item.objects.all()
	template = loader.get_template('apple/index.html')
	context = {
		'items': items
	}
	return HttpResponse(template.render(context,request))

def new(request):
	if request.method == 'POST':
		i = ItemForm(request.POST, request.FILES)
		if i.is_valid():
			i.save()
			return HttpResponseRedirect('/apple/')
	else:
		i = ItemForm()
		return render(request, 'apple/new.html',{'itemform':i})

def detail(request, item_id):
	try:
		item = Item.objects.get(pk=item_id)
	except Item.DoesNotExist:
		raise Http404("Item does not exist")
	return render(request, 'apple/detail.html', {'item': item})

def edit(request, item_id):
	if request.method == 'POST':
		item= Item.objects.get(pk=item_id)
		i = ItemForm(request.POST, request.FILES, instance=item)
		if i.is_valid():
			i.save()
			return HttpResponseRedirect('/apple/')
		else:
			raise Http404("Item does not exist")

	else:
		try:
			item = Item.objects.get(pk=item_id)
			i = ItemForm(instance=item)
		except Item.DoesNotExist:
			raise Http404("Item does not exist")
		return render(request, 'apple/edit.html', {'itemform':i, 'item':item})

def delete(request, item_id):
	if request.method == 'POST':
		item= Item.objects.get(pk=item_id)
		item.delete()
		return HttpResponseRedirect('/apple/')
