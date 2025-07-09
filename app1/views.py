from django.shortcuts import render

# Create your views here.
def django_templating_lang(request):
    context = {"app" : "app1"}
    return render(request , 'app1/template.html' , context=context)