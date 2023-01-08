from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_input = models.TextField( verbose_name="User Input", null=True)
    ai_response = models.TextField( verbose_name="User Input", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f'{self.user_input}'
    
    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'
