from django.contrib import admin
# estamos importando la clase Posts para poder mostrarlo en el admin
from .models import Post
# Register your models here.Esto nos muestra el ventana,pestaña post para utilizarla
# en el admin
admin.site.register(Post)
