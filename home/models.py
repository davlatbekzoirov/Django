from django.db import models

class Add_jobs(models.Model):
    link = models.CharField(max_length=350)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Add jobs'
    
    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Image_job(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
class AdminMessage(models.Model):
    message = models.CharField(max_length=1000000000)

    class Meta:
        verbose_name_plural = "Message"
