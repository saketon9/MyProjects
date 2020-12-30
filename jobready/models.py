from django.db import models

# Create your models here.


Interview_Category = (
    ('J', 'Java'),
    ('C', 'C'),
    ('PHP', 'PHP'),
    ('Py', 'Pyhton')

)

Company_Name = (
    ('G', 'Google'), ('F', 'Facebook'), ('kh', 'Khoros')
)


class fresherQuestion(models.Model):
    Questions = models.TextField(max_length=2000)
    Answers = models.TextField(max_length=2000)
    Category = models.CharField(choices=Interview_Category, max_length=5, default='NA')


class company_Reviews(models.Model):
    review = models.TextField(max_length=500)
    review_Category = models.CharField(choices=Company_Name, max_length=50, default='Not Available')
