import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

with open("token.txt","r",encoding="utf-8") as file1:
    token = file1.readline().strip()

with open("kyrs.txt","r+",encoding="utf-8") as file2:
    kyrs = file2.readline().strip()



vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def otpravlaem(id,text):
    vk_session.method("messages.send", {"user_id" : id, "message": text, "random_id" : 0})

def schitaem(sym):
    if sym <= 99:
        return 31
    elif sym>=100 and sym<=199:
        return 61
    elif sym>=200 and sym<999:
        return 1000
    elif sym >= 999 and sym < 1899:
        return 1500
    elif sym >= 1899:
        return 2000



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_chat == False:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg.isdigit() == True:
                sym = int(msg)
                kom = schitaem(sym)
                if kom==1000:
                    kom = 1000
                elif kom = 1500:
                    kom = 1500
                elif kom = 2000:
                    kom = 2000
                else:
                    kom = kom * float(kyrs)
                otpravlaem(id,"Стоимость покупки составит == "+ str(round((float(kyrs) * sym) + kom)) + " рублей(с учётом комиссии) \n"
                                                                                                        "Для заказа писать @goatayodia")
            elif msg[0:17] == "/изменить курс на":
                kyrs = msg[18:22]
                file2 = open("kyrs.txt","r+",encoding="utf-8")
                file2.write(kyrs)
                file2.close()
                otpravlaem(id,"Курс изменён на " + kyrs)
            else:
                otpravlaem(id, "AdievLogisticsBot приветствует тебя &#128075; \n"
                                "Отправьте мне цену в юанях и я рассчитаю стоимость покупки &#128184;")

