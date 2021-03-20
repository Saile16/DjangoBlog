from django.urls import path
from . import views

# esto te llevara a los viewst post donde tenemos definido unas views y eso mostrara
# recordar qwue tambien tenemos que cambiar las urls de mysite
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 127.0.0.1:8000/post/new-->local
    path('post/new/', views.post_new, name="post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name="post_edit")
]
