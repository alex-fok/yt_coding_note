from django.db import models

# Create your models here.
class Video(models.Model):
    def fileStruct_default():
        root = {"id": "/", "type": "root", "parent": "", "subDirs": []}
        return {"0": {
            "/": root
        }}
    videoId = models.CharField(max_length=20)
    fileStruct = models.JSONField(default=fileStruct_default)

class CodeFile(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    fileId = models.CharField(max_length=50)
    content = models.TextField()
