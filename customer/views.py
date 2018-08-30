# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View,FormView
from customer.forms import CustomerForm,UserForm

from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test

class HomeView(View):
	template_name='index.html'
	def get(self,request):
		return render(request,self.template_name)
		

class AboutView(View):
	template_name='about.html'
	def get(self,request):
		return render(request,self.template_name)

class ProductView(View):
	template_name='products.html'
	def get(self,request):
		return render(request,self.template_name)


class ProcessView(View):
	template_name='process.html'
	def get(self,request):
		return render(request,self.template_name)

class GalleryView(View):
	template_name='gallery.html'
	def get(self,request):
		return render(request,self.template_name)	

class ContactView(View):
	template_name='contact.html'
	def get(self,request):
		return render(request,self.template_name)


class RegisterCustomer(FormView):
	template_name = 'sign.html'
	form_class = UserForm
	model = User

	def get(self,request,*args, **kwargs):
	    self.object = None
	    form_class = self.get_form_class()
	    user_form = self.get_form(form_class)
	    cust_form = CustomerForm()
	    return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))


	def post(self,request,*args,**kwargs):
	    self.object = None
	    form_class = self.get_form_class()
	    user_form = self.get_form(form_class)
	    cust_form = CustomerForm(self.request.POST,self.request.FILES)
	    if (user_form.is_valid() and cust_form.is_valid()):
	        return self.form_valid(user_form, cust_form)
	    else:
	        return self.form_invalid(user_form, cust_form)

	def get_success_url(self, **kwargs):
	    return r('success')

	def form_valid(self, user_form, cust_form):
	    self.object = user_form.save()
	    self.object.is_staff=True
	    self.object.save()
	    cust_obj= cust_form.save(commit=False)
	    cust_obj.usr_data = self.object
	    cust_obj.save()
	    return redirect('/login/')

	def form_invalid(self, user_form, cust_form):
	    return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))

def login(request):
    form =AuthenticationForm()
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return redirect("/adminhome/")# or your url name
        if request.user.is_staff:
            return redirect("/home/")# or your url name


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            if request.user.is_superuser:
                return redirect("/adminhome/")# or your url name
            if request.user.is_staff:
                return redirect("/home/")# or your url name

        else:
            messages.error(request, 'Error wrong username/password')
    context = {}
    context['form']=form

    return render(request, 'login.html', context)

@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
    context = {}
    return render(request, 'index.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
    context = {}
    return render(request, 'newhome.html', context)