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

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title