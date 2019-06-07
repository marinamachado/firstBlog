from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#link para outro modelo
    title = models.CharField(max_length=200)#texto com tamanho limitado
    text = models.TextField()#texto com tamanho ilimitado
    createdDate = models.DateTimeField(#data e hora
            default=timezone.now)
    publishedDate = models.DateTimeField(
            blank=True, null=True)

    def publicacao(self): #metodo
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title