from django import forms

from booking.models import  NewProducts,BookingProduct

class ProductsForm(forms.ModelForm):
	class Meta:
		model = NewProducts
		exclude=('created_date',)

class BookingForm(forms.ModelForm):
	class Meta:
		model = BookingProduct
		exclude=('created_date',)	





		
# class OrderForm(forms.Form):
# 	def __init__(self,*args,**kwargs):
# 		super(OrderForm,self).__init__(*args, **kwargs)

# 	event_type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)	
# 	event_name= forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}),required=True)		
# 	pic= forms.ImageField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
# 	rate= forms.IntegerField(widget=forms.TextInput(attrs={ 'class': 'form-control'}),required=True)
# 	event_date= forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}),required=True)
# 	