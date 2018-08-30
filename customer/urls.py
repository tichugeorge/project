from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from customer import views
from customer.views import HomeView,AboutView,ProductView,ProcessView,GalleryView,RegisterCustomer,ContactView

urlpatterns = [
	url(r'^home/', HomeView.as_view(),name='hm_vw'),
	url(r'^about/', AboutView.as_view(),name='abt_vw'),
	url(r'^products/', ProductView.as_view(),name='pdt_vw'),
	url(r'^process/', ProcessView.as_view(),name='pro_vw'),
	url(r'^gallery/', GalleryView.as_view(),name='glry_vw'),
	url(r'^contact/', ContactView.as_view(),name='contct_vw'),
	url(r'^register/$', RegisterCustomer.as_view(), name='cust_reg'),
	url(r'^login/$', views.login, name='login'),


]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)