from django.db import models
from django.contrib.auth import get_user_model # here we are importing the user model bc we want to link the user to the thing that they are creating

# Create your models here.
class Thing(models.Model): 
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Thing_name=models.CharField(max_length=64)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Thing_name # this is what will show up in the admin page