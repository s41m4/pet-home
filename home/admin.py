from django.contrib import admin
from .models import Post
from .models import Pet
from .models import Profile

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Pet)