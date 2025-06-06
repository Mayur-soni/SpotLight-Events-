from django.db import models
from django.utils.safestring import mark_safe
# from unicodedata import category


# Create your models here.

class Registretion(models.Model):
    NAME= models.CharField(max_length=30)
    DOB= models.DateField()
    EMAIL= models.EmailField()
    PHONE= models.BigIntegerField()
    PASSWORD= models.CharField(max_length=30)
    ROLE= models.CharField(max_length=30)
    STATUS= models.CharField(max_length=30)
    ADDRESS= models.TextField()
    GENDER= models.CharField(max_length=30)
    DP= models.ImageField(upload_to='document', null=True)

    def __str__(self):
        return self.NAME

    def udp(self):
        return mark_safe('<img src={} width="100">'.format(self.DP.url))



class CATEGORY(models.Model):
    CAT_NAME= models.CharField(max_length=30)

    def __str__(self):
        return self.CAT_NAME


class EVENT(models.Model):
    SELLER_ID= models.ForeignKey(Registretion, on_delete=models.CASCADE, null=True)
    CATEGORY_ID= models.ForeignKey(CATEGORY, on_delete=models.CASCADE)
    E_NAME= models.CharField(max_length=30)
    E_IMAGE= models.ImageField(upload_to='event_images')
    E_DATE= models.DateField()
    E_TIME= models.TimeField()
    E_URL= models.URLField(null=True)
    E_PRICE= models.IntegerField()
    E_DESCRIPTION= models.TextField()

    def __str__(self):
        return self.E_NAME

    def event_images(self):
        return mark_safe('<img src={} width="100">'.format(self.E_IMAGE.url))

class FEEDBACK(models.Model):
    EMAIL_ID= models.EmailField()
    RATING= models.CharField(max_length=30)
    COMMENT= models.TextField()


class BOOKING(models.Model):
    EVENT_ID = models.ForeignKey(EVENT, on_delete=models.CASCADE)
    Registretion_ID = models.ForeignKey(Registretion, on_delete=models.CASCADE)
    BOOKING_DATE = models.DateTimeField(auto_now_add=True, null=True)
    TOTAL_AMOUNT = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]
    STATUS = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Booking #{self.id} - {self.EVENT_ID.E_NAME}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class PAYMENT(models.Model):
    BOOKING_ID = models.ForeignKey(BOOKING, on_delete=models.CASCADE)
    PAYMENT_ID = models.CharField(max_length=100, unique=True)  # Razorpay payment ID
    AMOUNT = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded'),
    ]
    PAYMENT_STATUS = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    PAYMENT_DATE = models.DateTimeField(auto_now_add=True)
    SIGNATURE = models.CharField(max_length=200, blank=True, null=True)  # For verification

    def __str__(self):
        return f"Payment {self.PAYMENT_ID} - {self.PAYMENT_STATUS}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

class CONTACT(models.Model):
    NAME= models.CharField(max_length=30)
    EMAIL= models.EmailField()
    SUBJECT= models.CharField(max_length=30)
    PHONE= models.BigIntegerField()
    MESSAGES= models.TextField()

class CARDDETAILS(models.Model):
    Registretion_ID= models.ForeignKey(Registretion, on_delete=models.CASCADE)
    NAME= models.CharField(max_length=30)
    CVV= models.IntegerField()
    EXPDATE= models.DateField()
    ACCOUNT_NO= models.BigIntegerField()


