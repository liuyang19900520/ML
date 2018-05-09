import itchat,time,re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match =re.search('年',msg['Text']).span()
    if match:
        itchat.send(('我也祝您新年快乐'),msg['FromUserName'])

itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()