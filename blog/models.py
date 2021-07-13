from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='blog/',blank=True,null=True)  #업로드할 파일 지정
    writer=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
