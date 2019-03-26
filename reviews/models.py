from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    review = models.ForeignKey('feedback', on_delete=models.CASCADE, null=True, default = "NA")
    def __str__(self):
        return self.title

class feedback(models.Model):
    SCORE_CHOICES = zip(range(6), range(6) )    
    user = models.CharField(max_length=50, null= True, default='anonymous user')
    item = models.ForeignKey(product, on_delete=models.SET_NULL, null= True)
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, blank=False)

    def __str__(self):
        return 'Rating(Item ='+ str(self.item)+', Stars ='+ str(self.rating)+')'
    