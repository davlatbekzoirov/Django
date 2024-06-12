from django.db import models

class Add_jobs(models.Model):
    title = models.CharField(max_length=350)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


    class Meta:
        verbose_name_plural = 'Add jobs'
    
    def __str__(self):
        return self.name
    
class Popular_course(models.Model):
    image = models.ImageField(upload_to='images/')
    students = models.CharField(max_length=350)
    time = models.CharField(max_length=350)
    title = models.CharField(max_length=350)
    price = models.CharField(max_length=350)

    class Meta:
        verbose_name_plural = 'Popular Course'
    
    def __str__(self):
        return self.title

class Teacher(models.Model):
    image = models.ImageField(upload_to='images/')
    link_skype = models.CharField(max_length=350)
    link_facebook = models.CharField(max_length=350)
    link_linkedin = models.CharField(max_length=350)
    name = models.CharField(max_length=350)
    profession = models.CharField(max_length=350)

    class Meta:
        verbose_name_plural = 'Teacher'
    
    def __str__(self):
        return self.name