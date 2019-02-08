from django.contrib import admin
from .models import Category, myblog, Author
# Register your models here.


admin.site.register(Category)
admin.site.register(myblog)
admin.site.register(Author)