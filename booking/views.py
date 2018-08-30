# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse,render_to_response
from django.views.generic import CreateView,View
from django.contrib.auth.models import User

from booking.forms import ProductsForm,BookingForm
from booking.models import NewProducts,BookingProduct

# Create your views here.

# class PdtCreateView(CreateView):
# 	template_name='prod_new.html'
# 	form_class=ProductsForm
# 	success_url='success'

class PdtCreateView(View):
    template_name = 'prod_new.html'
    form_class =ProductsForm
    def get(self,request):
    	if request.user.is_superuser:
	        if request.user.is_superuser:
	            form  = self.form_class()
	            context={
	                'form':form
	            }
	            return render(request,self.template_name,context)
	        else:
	            return redirect('/login/')

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            print('Valid !')
            form.save()
            context = {
                'form':form,
                'success':"saved successfully"
            }
            return redirect('/listss/')

        else:
            print('Invalid !')
            context = {
                'form':form
            }
            return render(request,self.template_name,context)

class HomeAdminView(View):
	template_name='newhome.html'
	def get(self,request):
		if request.user.is_superuser:
			return render(request,self.template_name)	

class ListPdt(View):
	template_name = 'pdt_lst.html'
	def get(self,request):
		if request.user.is_superuser:
			data = NewProducts.objects.all()
			context={
				'data' :data
			}
			return render(request,self.template_name,context)

class EditPdtz(View):
	template_name = 'edit.html'
	form_class = ProductsForm

	def get(self,request,pk):
		if request.user.is_superuser:
		
			pdt_id = pk

			pdt_obj = NewProducts.objects.get(id=pdt_id)
			
		
			
			form = ProductsForm(
				initial={
				'Name':pdt_obj.Name,
				'quantity':pdt_obj.quantity,
				'price':pdt_obj.price,
				'picture':pdt_obj.picture,

				}
			)
			context = {
				'form': form
			}
			return render(request,self.template_name,context)

	def post(self,request,pk):
		pdt_id = pk
		form = ProductsForm(request.POST,request.FILES)
		buy_pdt = NewProducts.objects.get(id=pdt_id)
		print(buy_pdt)
		if form.is_valid():
			print "valid"
			buy_pdt.Name = str(request.POST.get('Name'))
			buy_pdt.quantity =str(request.POST.get('quantity'))
			buy_pdt.price = str(request.POST.get('price'))
			buy_pdt.picture= request.FILES.get('picture')
			buy_pdt.save()
			
			context = {
			'form': form
			}
			return redirect('/home/')
		else:
			print "not cvalid",form.errors
			context = {
			'form':form
			}
			return render(request,self.template_name,context)	

class BookPdtz(View):
	template_name = 'product1.html'
	def get(self,request):
		if request.user.is_staff:
			data = NewProducts.objects.all()
			context={
				'data' :data
			}
			return render(request,self.template_name,context)

class Order(View):
	template_name = 'buk.html'
	form_class = ProductsForm

	def get(self,request,pk):
		if request.user.is_staff:
			event_id = pk
			event_obj = NewProducts.objects.get(id=event_id)
			form = ProductsForm()
			context = {
				
				'Name':event_obj.Name,
				'quantity':event_obj.quantity,
				'price':event_obj.price,
				
			
			}
			return render(request,self.template_name,context)


		

		def post(self, request,pk):
			event_id=pk
			form = ProductsForm(request.POST)
			model=NewProducts
			print(request)
			event_obj = NewProducts.objects.get(id=event_id)

			# if form.is_valid():
			print("eeee")
			log_user=request.user
			s_booked_by = User.objects.get(username=log_user)
			s_pdt_types = str(request.POST.get('pdt_types'))
			sobj = BookingProduct.objects.create(booked_by=s_booked_by,pdt_types=event_obj.Name,quantity=event_obj.quantity,price=event_obj.price)
			sobj.save()
			# context = {
			# 	'form':form,
			# 	'success':"saved successfully"
			# }
			return redirect('/books/')

		