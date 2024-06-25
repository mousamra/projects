import random

hellow = ["hi","is anyone there?","hello","good day","hello there"]
bye = ["i text you later","see you later","bye","goodbye","i am leaving","have a Good day"]
howare =["how are you","whats up","how you doing"]
name =["whats your name","what is your name","do you have any name","what should i call you","your good name"]
menu =["i want to buy something","what is on the menu","what do you reccommend?","how can i help you"]
hours =["when are you guys open","what are your hours","hours of operation","time","you are free"]
feelings =["i am feeling low", "i am not feeling good","feeling lonely","i have no one to talk"]
share =["i want to share something", " please don't get me wrong","can i express my felling to you","no one is there for me"]
print("***********************************************\n")

while True:
    a = input('User said -')

    if a.lower() in hellow:
        botans = ["Hello !","hi","hi what'sup","welcome","haii after a long time"]
        print('Bot said -'+random.choice(botans)+'\n')

    elif a.lower() in  bye:
        botans = ["sad to see you go: bye","miss you","text when you are free","take care","Goodbye","Have a nice day",]
        print('Bot said -'+random.choice(botans)+'\n')

    elif a.lower()  in howare:
        botans =["I am fine ,thanks","Happy","I am good","as always fit and fine"]
        print('Bot said -'+random.choice(botans)+'\n')

    elif a.lower()  in name:
        botans =["My name is alexa","You can call me buddy"," buddy at your service","I am here for you","How can i help you"]
        print('Bot said -'+random.choice(botans)+'\n')
    
    elif a.lower()  in menu:
        botans =["what do you want to buy","what are you in the mood for","please tell you options you listed to buys, so that i can help you out"]
        print('Bot said -'+random.choice(botans)+'\n')

    elif a.lower()  in hours:
        botans =["We are open 24/7","Available for your service anytime","yes free for you anytime"]
        print('Bot said -'+random.choice(botans)+'\n')

    elif a.lower()  in feelings:
        botans =["What happen","Oh no , I' am sorry to hear that you are not felling good","yes free for you anytime"]
        print('Bot said -'+random.choice(botans)+'\n')

    elif a.lower()  in share:
        botans =["you can share ", "feel free","express dont hesitate","i am there for you"]
        print('Bot said -'+random.choice(botans)+'\n')
        

    else:
        print('Bot said -Sorry What ?''\n')
        


        