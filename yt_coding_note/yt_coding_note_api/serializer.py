from rest_framework.serializers import ModelSerializer
from .models import Video, CodeFile

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = [ 'videoId', 'fileStruct' ]

class CodeFileSerializer(ModelSerializer):
    class Meta:
        model = CodeFile
        fields = [ 'id', 'fileId', 'content' ]
