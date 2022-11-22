from dingtalkchatbot.chatbot import DingtalkChatbot,ActionCard,CardItem
def talktext(webhook,secret,body):
    xiaoding = DingtalkChatbot(webhook, secret=secret)
    xiaoding.send_text(msg=body, is_at_all=False)