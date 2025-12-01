from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class testappVariety(models.Model):
    TEST_TYPE_CHOICE = [
        ('MD', 'Middle'),
        ('WD', 'Window'),
        ('AL', 'Aile'),
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='testapps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=TEST_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.TextField(default='')

    def __str__(self):
        return self.name 
    


#One to Many
class SeatReview(models.Model):
    #fields in the model
    seat = models.ForeignKey(testappVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RATING_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.seat.name}'
    

#Many to Many
class Airplane(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    seat_variety = models.ManyToManyField(testappVariety, related_name='counter')
    
    def __str__(self):
        return self.name
    

#One to One
class seatNumber(models.Model):
    seat = models.OneToOneField(testappVariety, on_delete=models.CASCADE, related_name='certificate')
    seat_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f'Certificate for {self.seat.name}'