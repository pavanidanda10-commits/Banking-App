from django.db import models

# Create your models here.

class UserAccount(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=30,primary_key= True)
    password = models.CharField(max_length=30,)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_accounts"
       

    def __str__(self):
        return self.email