from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
import json

from forms import *
from models import UserReg,User

def signuppage(request):
    registration_form = RegistrationForm()
    profile_form = ProfileForm()
    
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        print registration_form    
        
        if registration_form.is_valid() and profile_form.is_valid():
            user = registration_form.save()
            user.set_password(user.password) 
            user.save()
            prof = profile_form.save(commit = False)
            prof.user = user            

            if 'profileimage' in request.FILES:
                prof.profileimage = request.FILES['profileimage']
            prof.save()  
    
    return render(request, 'signup.html', {'reg_form' : registration_form , 'pro_form' : profile_form })            
        

#@login_required(login_url='/profile/')  
def loginpage(request):
   
   
    login_obj = LoginForm()
    if request.method == 'POST':
    	user_name = request.POST['username']
        pass_word = request.POST['password']
        user = authenticate(username = user_name, password = pass_word)
       
        
        if user:
            if user.is_active:    
                login(request, user)
                return HttpResponseRedirect('/profile/')
            return HttpResponse("no user")
        else:
            return HttpResponseRedirect('/error_page/')
    return render(request,'login.html', {'login_form' : login_obj})        
                     

def profilepage(request):
    
    image_obj = UserReg.objects.get(user = request.user)
    return render(request, 'profile.html', {'user' : request.user, 'pro_obj' : image_obj })    

def loggedout(request):
    return render(request, 'login.html')            
    
def editpage(request):
    
    if request.method == 'GET':
        reg_obj = UpdateForm(instance = request.user)
        obj = UserReg.objects.get(user = request.user)
        pro_obj = ProfileForm(instance = obj)
        return render (request, 'editpage.html', {'reg_obj' : reg_obj, 'pro_obj' : pro_obj, 'obj': obj})
    
    else:
        reg_obj = UpdateForm(request.POST, instance = request.user)
        obj = UserReg.objects.get(user = request.user)        
        pro_obj = ProfileForm(request.POST, request.FILES, instance = obj)
        print reg_obj

        if reg_obj.is_valid():
            user = reg_obj.save()
            if pro_obj.is_valid():
                profile_obj = pro_obj.save(commit = False)
                profile_obj.user = request.user
                profile_obj.save() 
                return render (request, 'profile.html', {'reg_obj' : reg_obj, 'pro_obj' : profile_obj,})          
            else:
                return render (request, 'login.html')    
        else:
            return render (request, 'login.html')     
            
def errorpage(request):
    return render(request,'errorpage.html') 
    
def superpage(request):
    context = UserReg.objects.all()
   
    return render(request,'superpage.html', {'users' : context})
    
def searchbox(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        context = UserReg.objects.all()
        for term in search_query:
            context = context.filter(Q(user__username__istartswith = term))
                   
        if context:
            return render(request,'search_page.html', {'results' : context, 'ltrsearch' : search_query })       
        else:
            return HttpResponse('sorry no user found')


def delete(request):
    if request.method == 'GET':
        delete_user = request.GET.get('delete_box',None)
        print delete_user
        try:
            context = UserReg.objects.get(user__username__iexact=delete_user)
            print context
            context.delete()
        except:
            return HttpResponse('ooompiii')       
    return render(request,'deleted.html')    

def searchauto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        results=[]
        context = UserReg.objects.filter(user__username__istartswith=q)
        print context;
        for name in context:
            name_json = {}
            name_json['name'] = name.user.username
            results.append(name_json)
        print results    
        data = json.dumps(results)
        print data
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
        
       
    
    
    
    
      
    
              
            
        
    
    

        
    
    

         



    

    
        
        
        
        
    


