#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20170112 import ImageSyncScanRequest
import json
import uuid
import datetime

# Porn-detection function.
# event: the input image url.
# context: the function context provided by FunctionCompute service.
def handler(event, context):
    # Your account access key id/secret are stored in context.credentials
    # Replace the "your_access_key_id" and "your_access_key_secret"
    clt = client.AcsClient("your_access_key_id", "your_access_key_secret", 'cn-shanghai')
    region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
    request = ImageSyncScanRequest.ImageSyncScanRequest()
    request.set_accept_format('JSON')

    # set tasks and scenes for porn detection
    img_url = event.decode("utf-8")
    task = {"dataId": str(uuid.uuid1()),
             "url":img_url,
             "time":datetime.datetime.now().microsecond
            }
    request.set_content(bytearray(json.dumps({"tasks": [task], "scenes": ["porn"]}), "utf-8"))
    response = clt.do_action(request)
    return response
