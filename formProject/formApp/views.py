from django.shortcuts import render
from django.http import HttpResponseRedirect
from  formApp import form
from django.core.mail import send_mail
from formApp.models import Practice,Products
from django.contrib.auth.decorators import login_required
from formApp.signupform import SignUpForm
def studentinputview(request):
    form1=form.Student()
    if(request.method=='POST'):
        form1=form.Student(request.POST)
        if(form1.is_valid()):
            name=form1.cleaned_data['name']
            email=form1.cleaned_data['email']
            roll=form1.cleaned_data['roll']
            branch=form1.cleaned_data['branch']
            college=form1.cleaned_data['college']
            mydata=Practice.objects.get_or_create(name=name,roll=roll,branch=branch,college=college)
            send_mail('Registration Successfull','Hey Thanks for Registering to our website our team will get in touch with you','laymansagro@gmail.com',[email],fail_silently=False)
            return render(request,'formApp/thanks.html',{'name':name})

    mydict={'forms':form1}
    return render(request,'formApp/form.html',context=mydict)
def home(request):
    return render(request,'formApp/home.html')
@login_required
def contact(request):
    return render(request,'formApp/contact.html')
def logout(request):
    return render(request,'formApp/logout.html')
def signupview(request):
    form=SignUpForm()
    if(request.method=='POST'):
        form=SignUpForm(request.POST)
        if(form.is_valid()):
            email=form.cleaned_data['email']
            print(email)
            user=form.save()
            user.set_password(user.password)
            user.save()
            send_mail('Registration Successfull','Hey Thanks for Registering to our website our team will get in touch with you','laymansagro@gmail.com',[email],fail_silently=False)
            return HttpResponseRedirect('/accounts/login')
    return render(request,'formApp/signup.html',{'form':form})


def productsview(request):
    product_details=Products.objects.all()
    return render(request,'formApp/products.html',{'product_details':product_details})
