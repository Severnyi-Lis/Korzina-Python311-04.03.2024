#Спросить человека маршрут ("как пройти в библиотеку"). 
#Получить ответ в виде строки. Сохранить в переменную. Вывести первое слово ответа на экран
way=input("Как пройти в библиотеку? ")
l=str(way.split()[0])
print (l)
