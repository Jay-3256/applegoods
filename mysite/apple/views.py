from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Item
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	if request.method == 'POST':
		userinput = request.POST.get('userinput', None)
		items = Item.objects.filter(
		Q(titleline__contains = userinput) |
		Q(body__contains = userinput)
		)
		items = Paginator(items, 1)
		page_number = request.GET.get('page')
		page_obj =	items.get_page(page_number)
		template = loader.get_template('apple/index.html')
		context = {
			'items': page_obj
		}
		return HttpResponse(template.render(context,request))
	else:
		items = Item.objects.all()
		items = Paginator(items, 1)
		page_number = request.GET.get('page')
		page_obj =	items.get_page(page_number)
		template = loader.get_template('apple/index.html')
		context = {
			'items': page_obj
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
		item.hit = item.hit +1
		item.save()
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
