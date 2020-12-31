from django.db import models

# Create your models here.

class Data(models.Model):
    phone_number=models.CharField(max_length=50)
    text_message=models.CharField(max_length=255,blank=True, null=True)

    
    def __str__(self):
          return  self.phone_number




    def serialize(self):
        return {
            "id": self.id,
            "phone_number":self.phone_number,
            "text_message":self.text_message,
       
        }