"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from SportLight import views
from myproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login', views.login),
    path('verify', views.verifyuser),
    path('Registretion', views.Registre),
    path('insert', views.insertregister),
    path('artist-event-form', views.artist_event_form),
    path('manage-event', views.manageevent),
    path('events/', views.event_list),
    path('events', views.events),
    path('addevent', views.addevent),
    path('insertevent', views.insertevent),
    path('bookinghistory', views.bookinghistory),
    path('contact', views.contact),
    path('insertcontact', views.insertcontact),
    path('single/<int:eid>', views.singleevent),
    path('single/<int:eid>', views.singleevent),
    path('delete/<int:eid>', views.delete),
    path('editevent/<int:eid>', views.editevent),
    path('update', views.update),
    path('logout', views.logout),
    path('services', views.services),
    path('about', views.about),
    path('ecomm', views.ecomm),
    path('eror', views.eror),
    path('book-event/<int:event_id>', views.bookEvent, name='initiate_payment'),
    path('initiate_payment', views.initiate_payment, name='initiate_payment'),
    path('payment-success', views.paymentsuccess, name='payment_success'),
    path('payment-fail', views.paymentfail, name='payment_failed'),
    path("verify_payment", views.verify_payment)
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

