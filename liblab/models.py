from django.utils import timezone
from django.db import models


# Create your models here.
class User(models.Model):
    f_name = models.CharField("First Name", max_length=30)
    l_name = models.CharField("Last Name", max_length=30)
    email = models.CharField("Email", max_length=100)
    CHOICES = (('F', 'Female',), ('M', 'Male',))
    gender = models.CharField("Gender", max_length=2, choices=CHOICES)
    postalcode = models.CharField("Postal Code", max_length=7, default="N9B 3P4")

class Libuser(User):
    PROVINCE_CHOICES = (
        ('AB', 'Alberta'),
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
    )
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, default='Windsor')
    province = models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    phone = models.IntegerField(null=True)

class Libitem(models.Model):
    TYPE_CHOICES = (
        ('Book', 'Book'),
        ('DVD','DVD'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=100)
    itemtype = models.CharField(max_length=6, choices=TYPE_CHOICES, default='Book')
    checked_out=models.BooleanField(default=False)
    user=models.ForeignKey(Libuser, default=None, null=True)
    duedate=models.DateField(default=None, null=True)
    last_chkout = models.DateField(default=None, null=True)
    date_acquired = models.DateField(default=timezone.now)
    pubyr = models.IntegerField()
    CharField = models.IntegerField(default=0)

class Book(Libitem):
    CATEGORY_CHOICES = (
        (1, 'Fiction'),
        (2, 'Biography'),
        (3, 'Self Help'),
        (4, 'Education'),
        (5, 'Children'),
        (6, 'Teen'),
        (7, 'Other'),
    )
    author = models.CharField(max_length=100, blank=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)

    def __str__(self):
        return self.title + ' by ' + self.author


