from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'content',
			'email',
			'draft'
		]



class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer