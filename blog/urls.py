from django.urls import path
from . import views

# esto te llevara a los viewst post donde tenemos definido unas views y eso mostrara
# recordar qwue tambien tenemos que cambiar las urls de mysite
urlpatterns = [
    path('', views.post_list, name='post_list')
]
