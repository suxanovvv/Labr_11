#12. а) Дан текстовий файл f. Переписати у файл g тільки ті рядки вихідного
#файлу, що містять більше тридцяти символів.

g=open('12.1.text_.txt', 'w') #Відкриваємо документ для запису даних, у яких більше\
#30 символів.

with open('12.1.text.txt', 'r') as f: #Далі відкриваємо файл f (в якому вже записана\
#інформація) та зчитуємо її.
    lines=f.readlines()
    for i in lines:
        if len(i)>30:
           g.write(i) #Записуємо у файл g, якщо у рядку більше, ніж 30 символів.
        
g=open('12.1.text_.txt', 'r')

#Ітераційно виведемо рядок на екран користувача (для більшої зрозумілості).
fd=g.readlines()
for i in fd:
    print('Текст, що містить більше 30 літер: ', i)

