from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	list_display_links = ["title"]
	list_filter = ["timestamp", "updated"]
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)

