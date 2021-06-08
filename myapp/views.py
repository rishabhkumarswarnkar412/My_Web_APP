from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Get_quote, Design, Feedback

# Create your views here.
def index(request):
    dsins=Design.objects.all()
    return render(request,'index.html',{'dsins':dsins})
    #return HttpResponse('This is HomePage')
def get_quote(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')

        get_quote=Get_quote(name='name', email='email', phone='phone', desc='desc', date=datetime.today())
        get_quote.save()
    return render(request, 'get_quote.html')
    # return HttpResponse('This is Contact page')

def about(request):
    return render(request, 'About.html')
    #return HttpResponse('This is About page')

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse('This is Service page')

def feedback(request):
    if request.method== 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        feedback= request.POST.get('feedback')

        feedback=Feedback(name='name', email='email',feedback='feedback', date=datetime.today())
        feedback.save()
    return render(request, 'feedback.html')
