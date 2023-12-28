from django.contrib import admin
from .models import *

# Register your models here.

# username  = Library
# password = library

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name')}

# class BookAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('book_name')}

admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Issuebook)


