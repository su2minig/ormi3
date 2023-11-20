from rest_framework.serializers import ModelSerializer
from .models import NoticePost

class NoticePostSerializer(ModelSerializer):
    class Meta:
        model = NoticePost
        fields = [
            'id',
            'Notice_author',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]