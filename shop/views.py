from django.shortcuts import render
from .models import Medicine, Category  # MANA SHU YERGA Category NI QO'SHING

def index(request):
    categories = Category.objects.all() # Hamma kategoriyalarni olamiz
    cat_id = request.GET.get('category') # Tanlangan kategoriyani olamiz
    query = request.GET.get('q')

    if query:
        items = Medicine.objects.filter(name__icontains=query)
    elif cat_id:
        items = Medicine.objects.filter(category_id=cat_id)
    else:
        items = Medicine.objects.all()

    return render(request, 'index.html', {'items': items, 'categories': categories})

def detail(request, pk):
    medicine = Medicine.objects.get(pk=pk)
    return render(request, 'detail.html', {'medicine': medicine})