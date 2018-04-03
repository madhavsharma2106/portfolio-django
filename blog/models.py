from django.db import models

#Create a blog model
#  Title
#  Pub date
#  body
#  image


#Add a blog app to root app settings

#create a migration

#migrate

#add to the app admin

class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')