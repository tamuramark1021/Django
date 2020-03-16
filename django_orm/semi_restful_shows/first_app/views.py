from django.shortcuts import render, redirect
from .models import TVshow

# Create your views here.
def home(request):
    context={
        'all_tvshow': TVshow.objects.all()
    }
    return render(request, 'home_page.html', context)

def tvshow_new(request):

    return render(request, 'tvshow_new.html')

def add_tvshow(request):
    # some_tvshow=TVshow.objects.get(id=id)
    # if request.POST['title'] and request.POST['network'] and request.POST['release_date'] and request.POST['desc']:
    newShow=TVshow.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
    return redirect(f'/tvshow_info/{newShow.id}')
# may have to add back the network portion of the request.POST['network']
def tvshow_info(request, id):
    context={
        'some_tvshow': TVshow.objects.get(id=id),
    }
    return render(request, 'tvshow_info.html', context)

def edit_tvshow(request, id):
    context={
        # 'some_network': Network.objects.get(id=request.POST['network_id']),
        'some_tvshow' : TVshow.objects.get(id=id),
    }
    return render(request, 'edit_tvshow.html', context)

def change_tvshow(request, id):
    changing_tvshow=TVshow.objects.get(id=id)
    if request.POST['title']:
        changing_tvshow.title=request.POST['title']
        changing_tvshow.save()
    if request.POST['network']:
        changing_tvshow.network=request.POST['network']
        changing_tvshow.save()
    if request.POST['release_date']:
        changing_tvshow.release_date=request.POST['release_date']
        changing_tvshow.save()
    if request.POST['desc']:
        changing_tvshow.desc=request.POST['desc']
        changing_tvshow.save()
    return redirect(f'/tvshow_info/{changing_tvshow.id}')

def delete_tvshow(request, id):
    delete_show=TVshow.objects.get(id=id)
    delete_show.delete()
    return redirect('/')