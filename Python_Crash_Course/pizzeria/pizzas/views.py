from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """显示所有的pizza"""

    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """显示特定的pizza"""

    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
