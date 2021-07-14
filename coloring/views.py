from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, "coloring/demo.html")

def interaction(request):
    return render(request, "coloring/new_interaction.html")

def blank(request):
    return render(request, "coloring/blank.html")