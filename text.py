from dingtalkchatbot.chatbot import DingtalkChatbot,ActionCard,CardItem
def talktext(wehook,secret,body):
    xiaoding = DingtalkChatbot(wehook, secret=secret)
    xiaoding.send_text(msg=body, is_at_all=False)
def talklink(wehook,secret,titel,text,Url,photo_URL):
    xiaoding = DingtalkChatbot(wehook,secret=secret)
    xiaoding.send_link(titel=titel,text=text,message_url==Url,pic_url=photo_URL)
def cin():
