# -*- encoding: utf-8 -*-

import urllib2
import requests
import json

class sendMessageforText:

    def get_token(self,corpid,corpsecret):

        baseurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(corpid,corpsecret)
        request = urllib2.Request(baseurl)
        response = urllib2.urlopen(request)
        ret = response.read().strip()
        dd = eval(ret)
        if dd["errmsg"] == "ok":
            return dd["access_token"]
        else:
            #print "Get token failed errcode="+dd["errcode"]
            return False

    def get_media_id(self,path,token):
        img_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=image".format(token)
        files = {'image':open(path, 'rb')}
        r = requests.post(img_url, files=files)
        re = r.json()
        if re["errmsg"] == "ok":
            return re["media_id"]
        else:
            #print "get media id faile errcode="+re["errcode"]
            return False


    def send_msg(self, token,text,user,aid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+token
        payload = {
            "touser": user,
            "msgtype": "text",
            "agentid": aid,
            "text": {
                "content": text
            },
            # 表示是否是保密消息, 0表示否, 1表示是,默认 0
            "safe": "0"
        }
        ret = requests.post(url, data=json.dumps(payload, ensure_ascii=False))
        remsg = ret.json()
        if remsg["errmsg"] == "ok":
            print "send text message success text="+str(text)
        else:
            print "send text message failed errcode="+str(remsg["errcode"])

    def send_image(self, token, media_id, user, aid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + token
        payload = {
            "touser": user,
            "msgtype": "image",
            "agentid": aid,
            # 表示是否是保密消息, 0表示否, 1表示是,默认 0
            "image":{
                "media_id":media_id
            },
            "safe": "0"
        }
        ret = requests.post(url, data=json.dumps(payload, ensure_ascii=False))
        remsg = ret.json()
        print remsg
        if remsg["errmsg"] == "ok":
            print "send image message success media_id="+media_id
        else:
            print "send image message failed media_id="+media_id

# text = sendMessageforText()
# token = text.get_token(mid, msecret)
#
# token = text.get_token(mid, msecret)
# text.send_msg(token, "自动发送图片",touser, agentid)
# medid = text.get_media_id(r"/root/tmp/8.png", token)
# # print medid
# text.send_image(token, medid, touser, agentid)

# ret = text.send_msg(token)
# if ret["errmsg"] == "ok":
#     print "send message success errcode="+str(ret["errcode"])
# else:
#     print "send message failed errcode="+str(ret["errcode"])


