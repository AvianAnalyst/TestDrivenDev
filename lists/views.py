from django.shortcuts import redirect, render
from lists.models import Item


# Create your views here.
# TODO: Adjust model so that items are associated with different lists
# TODO: Support unique URLs for each list
# TODO: Add URLS for adding a new item to an existing list via POST
def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
