from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from booking.views import PdtCreateView,ListPdt,EditPdtz,BookPdtz,Order,HomeAdminView

urlpatterns = [
	 url(r'^add/$',PdtCreateView.as_view(),name='add_event'),
	 url(r'^listss/$',ListPdt.as_view(),name='list_event'),
	 url(r'^edits/(?P<pk>[0-9]+)/$',EditPdtz.as_view(),name='edit_products'),
	 url(r'^adminhome/$',HomeAdminView.as_view(),name='Hm_vw'),
	 url(r'^books/$',BookPdtz.as_view(),name='book_event'),
	 url(r'orders/(?P<pk>[0-9]+)/$',Order.as_view(),name='order'),
	 ]


urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
