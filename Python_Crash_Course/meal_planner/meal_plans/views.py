from django.shortcuts import render

def index(request):
    """主页"""
    return render(request, 'meal_plans/index.html')
