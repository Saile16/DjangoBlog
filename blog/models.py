from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # este metodo lo usamos en los drafts

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)
# create a string representation
# aqui mostramos en string el titulo del post y lo que queramos

    def __str__(self):
        return self.title
        # return self.title + ' por ' + str(self.author)

# recordar hacer python manage.py makemigrate luego python manage.py migrate
# tambien agregar en admin.py


class Comment(models.Model):
    # on_delete significa si eliminamos un post todoslos comentarios relacionados al post
    # tienen que elminarse
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
    # Post.objects.get(pk=2).comments.all()
