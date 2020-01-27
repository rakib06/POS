from django.shortcuts import render, redirect, get_object_or_404
from .models import Chair, Sofa, Bed
from .forms import ProductForm

def index(request):
    return render(request, 'index.html')


def display(product, request):
    items = product.objects.all()
    product_list = list(str(product))
    p_s = ''
    for item in product_list[23:-2]:
        p_s += item
    context = {
        'items': items,
        'headline': str(p_s)
        }

    return render(request, 'index.html', context=context)


def display_chair(request):
    return display(Chair, request)


def display_sofa(request):
    return display(Sofa, request)


def display_bed(request):
    return display(Bed, request)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
        return render(request, 'add_new.html', {'form': form})


def edit_product(request, pk):
    item = get_object_or_404(Chair, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item )
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def edit_chair(request, pk):
    return edit_product(request,pk)


def delete_product(request, pk):
    Chair.objects.filter(id=pk).delete()
    items = Chair.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def delete_chair(request, pk):
    return delete_product(request, pk)

