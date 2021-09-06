from django.contrib import admin

# Register your models here.
from app1.models import Blog, Register, Contact
admin.site.register(Blog)
admin.site.register(Register)
admin.site.register(Contact)

