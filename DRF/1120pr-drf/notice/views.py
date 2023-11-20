from rest_framework.viewsets import ModelViewSet
from .models import NoticePost
from .serializers import NoticePostSerializer
from .permissions import IsAuthorOrReadOnly

class NoticePostViewSet(ModelViewSet):
    queryset = NoticePost.objects.all()
    serializer_class = NoticePostSerializer
    permission_classes = [IsAuthorOrReadOnly]