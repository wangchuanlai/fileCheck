from django.shortcuts import HttpResponse
from django.views import View
import json
import os


# Create your views here.


class checkFile(View):  # 获取文件尺寸
    def post(self, request):
        fileName = request.POST.get("filePath")
        if not fileName:
            return HttpResponse(json.dumps({
                "code": 400,
                "msg": "未传入 参数"
            }, ensure_ascii=False))

        fileName = "/" + fileName
        if os.path.exists(fileName):
            fileSize = os.path.getsize(fileName)
            return HttpResponse(json.dumps({
                "code": 200,
                "countSize": fileSize
            }))
        else:
            return HttpResponse(json.dumps({
                "code": 400,
                "msg": "文件不存在"
            }, ensure_ascii=False))


class latestVersion(View):  # 获取最新时间的 文件名称
    def post(self, request):
        filePath = "/Users/nimawocao/Desktop/ios/"
        fileName = request.POST.get("fileName")
        if not fileName:
            return HttpResponse(json.dumps({
                "code": 400,
                "msg": "未传入 参数",
                "message": "false"
            }, ensure_ascii=False))

        fileList = {}
        for name in os.listdir(filePath):
            if fileName.split("/")[len(fileName.split("/"))-1] in name:
                fileList[int(os.path.getmtime(filePath + name))] = name

        if fileList:
            return HttpResponse(json.dumps({
                "code": 200,
                "msg": "成功获取文件属性",
                "md5Code": os.path.getsize(filePath + fileList[max(fileList)]),
                "fileName": fileList[max(fileList)],
                "message": "true"
            }, ensure_ascii=False))
        else:
            return HttpResponse(json.dumps({
                "code": 400,
                "msg": "文件不存在",
                "message": "false"
            }, ensure_ascii=False))
