from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from .models import Item
from .models import Comment
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

	if request.method =="POST":
		userinput = request.POST.get('userinput')
	elif request.GET.get('userinput'):
		userinput = request.GET.get('userinput')
	else:
		userinput = None
	items = Item.objects.all()
	if userinput is not None:
		items = Item.objects.filter(
		Q(titleline__contains = userinput) |
		Q(body__contains = userinput)
		)
	items = Paginator(items, 25)
	page_number = request.GET.get('page')
	page_obj = items.get_page(page_number)
	template = loader.get_template('apple/index.html')
	if userinput is not None:
		context = {
		'items': page_obj,
		'userinput': userinput
		}
	else:
		context = {
		'items': page_obj
		}

	return HttpResponse(template.render(context,request))

@login_required
def new(request):
	if request.method == 'POST':
		i = ItemForm(request.POST, request.FILES)
		if i.is_valid():
			item = i.save(commit=False)
			item.author = request.user
			item.save()
			return HttpResponseRedirect('/apple/')

	else:
		i = ItemForm()
		return render(request, 'apple/new.html',{'itemform':i})

def detail(request, item_id):
	if request.method == 'POST':
		item = Item.objects.get(pk=item_id)
		comment = Comment(item_id = item, user_id=request.user, text= request.POST.get('comment'))
		comment.save()
	else:
		try:
			item = Item.objects.get(pk=item_id)
			item.hit = item.hit +1
			item.save()
		except Item.DoesNotExist:
			raise Http404("Item does not exist")
	return render(request, 'apple/detail.html', {'item': item,'comments':Comment.objects.filter(item_id=item_id)})

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

def comment_delete(request, item_id, comment_id):
	if request.method == 'POST':
		comment= Comment.objects.get(pk=comment_id)
		comment.delete()
		item= Item.objects.get(pk=item_id)
		return render(request, 'apple/detail.html', {'item': item,'comments':Comment.objects.filter(item_id=item_id)})
	raise Http404("Error")
