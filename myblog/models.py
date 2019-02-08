#from typing import List
from django.db import models
#from django.urls import reverse  # To generate URLS by reversing URL patterns
from datetime import date

# Create your models here.


class Category(models.Model):
    """Model representing a Category """
    name = models.CharField(max_length=200, help_text="Enter a Category (e.g.  etc.)" )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class myblog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    text = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category, help_text="Select a Category")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.title

    def __str__(self):
        return self.text


    def display_category(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([category.name for category in self.category.all()[:3]])
        display_category.short_description = 'Category'


class Author(models.Model):
        """Model representing an author."""
        first_name = models.CharField(max_length=200)
        last_name = models.CharField(max_length=200)
        date_of_birth = models.DateField(null=True, blank=True)

        def __str__(self):
            #return self.first_name,self.last_name
            template = '{0},{1}'
            return template.format(self.first_name, self.last_name)

        #        class Meta:
 #       ordering = ['last_name', 'first_name']


  #  def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
   #      return reverse('myblog-detail', args=[str(self.id)])


  #  def __str__(self):
        """String for representing the Model object."""
   #     return self.first_name

