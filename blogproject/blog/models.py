from django.db import models
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='blog/',blank=True,null=True)  #업로드할 파일 지정
    writer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def summary(self):
        if len(self.body)>70:
            return self.body[:70]+'...'
        else:
            return self.body

