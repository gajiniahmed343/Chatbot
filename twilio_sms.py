from twilio.rest import Client
import temp

client=Client(temp.account_sid,temp.auth_token)
def twilio(self,n):
    if self.msg[0:5] == "unity":
        message=client.messages.create(
            body=str(n),
            from_=temp.twilio_num,
            to=temp.target_num
        )
    else:pass
def twilio1(n):
        message = client.messages.create(
            body=str(n),
            from_=temp.twilio_num,
            to=temp.target_num
        )
