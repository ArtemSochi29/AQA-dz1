# Както получить от пользователя оценку
rate_as_str=input("Оцените работу оператора от 1-5:") # str
rate=int(rate_as_str) # int

# Проверить что оценка от 1-5
if (rate < 1):
    rate = 1
if(rate > 5):
    rate = 5


# В зависимости от оценки предложить дать обратную связь
feedback=''
if rate==1:
     feedback = input("Расскажите, что нам улучшить?")
elif rate==2:
     feedback = input("Расскажите, что вас смутило?")
elif rate==3:
     feedback = input("Расскажите, что вас смутило?")
elif rate==4:
    feedback = input("Расскажите, почему не 5?")
else:
    feedback = input("Засскажите, за что похвалить оператора?")


print(feedback)
