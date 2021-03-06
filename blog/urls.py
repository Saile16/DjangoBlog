from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# esto te llevara a los viewst post donde tenemos definido unas views y eso mostrara
# recordar qwue tambien tenemos que cambiar las urls de mysite
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 127.0.0.1:8000/post/new-->local
    path('post/new/', views.post_new, name="post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    #
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name="comment_remove"),
    path('comment/<int:pk>/approve/',
         views.comment_approve, name='comment_approve'),
    path('signup/', views.signup, name='signup')

]
