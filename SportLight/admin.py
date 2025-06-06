from django.contrib import admin

from .models import *


# Register your models here.
class SwRegistretion(admin.ModelAdmin):
    list_display = ['NAME','DOB','EMAIL','PHONE','PASSWORD','ROLE','STATUS','ADDRESS','GENDER','DP']
    list_per_page = 3
    search_fields = ['NAME','EMAIL']
    list_filter = ['STATUS']
admin.site.register(Registretion, SwRegistretion)

class SwCATEGORY(admin.ModelAdmin):
    list_display = ['CAT_NAME']
admin.site.register(CATEGORY, SwCATEGORY)

class SwEVENT(admin.ModelAdmin):
    list_display = ['SELLER_ID','CATEGORY_ID','E_NAME','E_IMAGE','E_DATE','E_TIME','E_URL','E_PRICE','E_DESCRIPTION']
admin.site.register(EVENT, SwEVENT)

class SwFEEDBACK(admin.ModelAdmin):
    list_display = ['EMAIL_ID','RATING','COMMENT']
admin.site.register(FEEDBACK, SwFEEDBACK)

@admin.register(BOOKING)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'EVENT_ID', 'Registretion_ID', 'BOOKING_DATE', 'TOTAL_AMOUNT', 'STATUS')
    list_filter = ('STATUS', 'BOOKING_DATE')
    search_fields = ('EVENT_ID__E_NAME', 'Registretion_ID__NAME')

@admin.register(PAYMENT)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('PAYMENT_ID', 'BOOKING_ID', 'AMOUNT', 'PAYMENT_STATUS', 'PAYMENT_DATE')
    list_filter = ('PAYMENT_STATUS', 'PAYMENT_DATE')
    search_fields = ('PAYMENT_ID', 'ORDER_ID', 'BOOKING_ID__id')

class SwCONTACT(admin.ModelAdmin):
    list_display = ['NAME','EMAIL','SUBJECT','PHONE','MESSAGES']
admin.site.register(CONTACT, SwCONTACT)

class SwCARD(admin.ModelAdmin):
    list_display = ['Registretion_ID','NAME','CVV','EXPDATE','ACCOUNT_NO']
admin.site.register(CARDDETAILS, SwCARD)