from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def help(request):
    return render(request,'help.html')
def func1(request,sname):
    res=(sname==sname[::-1])
    d={'result':res}
    return render(request,'palindrome.html',d)
def func2(request,name1):
    res=(name1%2==0)
    v={'result':res}
    return render(request,'evenodd.html',v)
    
    