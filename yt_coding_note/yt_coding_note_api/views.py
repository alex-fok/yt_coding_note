from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .models import Video, CodeFile
from .serializer import VideoSerializer, CodeFileSerializer
# Create your views here.

@api_view(['GET'])
def getVideo(request: Request):
    try:
        info = Video.objects.get(videoId=request.query_params.get('videoId'))
    except Video.DoesNotExist:
        return HttpResponse(status=404)

    serializer = VideoSerializer(info)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def getFile(request: Request):
    try:
        info = CodeFile.objects.get(id=request.query_params.get('id'))
    except CodeFile.DoesNotExist:
        return HttpResponse(status=404)

    serializer = CodeFileSerializer(info)
    return JsonResponse(serializer.data)
