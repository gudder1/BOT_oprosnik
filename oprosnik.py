import telebot
import config

client = telebot.TeleBot(config.conf['token'])

#a == 0
@client.message_handler(content_types = ['text'])
def get_text(message):
  if message.text.lower() == 'привіт' or message.text.lower() == "хай" or message.text.lower() == "привіт" or message.text.lower() == "ку" or  message.text.lower() == "здоров":
    client.send_message(message.chat.id, 'Привіт! Почнемо роботу?')
  elif message.text.lower() == 'що ти можеш?' or message.text.lower() == "розкажи про себе" or message.text.lower() == "що ти можеш":
    client.send_message(message.chat.id, 'Я можу:Розповісти наскільки ти конфліктна людина')
  elif message.text.lower() == "почнемо" or message.text.lower() == "розпочнемо" or message.text.lower() == "старт" or message.text.lower() == "починаєм":
    client.send_message(message.chat.id,'Починаєм')
    client.send_message(message.chat.id,' У громадському транспорті почалась суперечка. Ваша реакція?')
    client.send_message(message.chat.id,'1) не приймаю участі;')
    client.send_message(message.chat.id,'2) коротко висловлююся на захист сторони, яку вважаю правою')
    client.send_message(message.chat.id,'3) активно втручаюся.')
    client.send_message(message.chat.id,'Зробіть ваш вибір:')
  elif message.text.lower() == "Запитання 2" :
    client.send_message(message.chat.id,'Чи виступаєте на зборах із критикою?')
    client.send_message(message.chat.id,'1) ні;')
    client.send_message(message.chat.id,'2) тільки якщо маю для цього вагомі підстави;')
    client.send_message(message.chat.id,'3) критикую з будь-якого приводу.')
    client.send_message(message.chat.id,'Зробіть ваш вибір')
    if message.text.lower() == '1':
      a = a + 3
    elif message.text.lower() == '2':
      a = a + 2
    elif message.text.lower() == '3':
      a = a + 1    
  elif message.text.lower() == "Запитання 3" :
    client.send_message(message.chat.id,'Чи часто сперечаєтесь з друзями?')
    client.send_message(message.chat.id,'1) тільки якщо ці люди не ображаються;')
    client.send_message(message.chat.id,'2) лише з принципових питань;')
    client.send_message(message.chat.id,'в) суперечки - моя стихія.')
    client.send_message(message.chat.id,'Зробіть ваш вибір:')
    if message.text.lower() == '1':
      a = a + 3
    elif message.text.lower() == '2':
      a = a + 2
    elif message.text.lower() == '3':
      a = a + 1  
  elif message.text.lower() == "Запитання 4":
    client.send_message(message.chat.id,' На обід запропонували недосолену страву. Ваша реакція?')
    client.send_message(message.chat.id,'1) не буду піднімати бучу через дрібниці;')
    client.send_message(message.chat.id,'2) мовчки візьму сільничку;')
    client.send_message(message.chat.id,'3) не втримаюсь від зауважень.')
    client.send_message(message.chat.id,'Зробіть ваш вибір:')
    if message.text.lower() == '1':
      a = a + 3
    elif message.text.lower() == '2':
      a = a + 2
    elif message.text.lower() == '3':
      a = a + 1  
  elif message.text.lower() == "Запитання 5":
    client.send_message(message.chat.id,'Якщо на вулиці, у транспорті Вам наступили на ногу:')
    client.send_message(message.chat.id,'1) з обуренням подивлюсь на кривдника;')
    client.send_message(message.chat.id,'2) сухо зроблю зауваження;')
    client.send_message(message.chat.id,'3) висловлю свої емоції, не обираючи виразів.')
    client.send_message(message.chat.id,'Зробіть ваш вибір:')
    if message.text.lower() == '1':
      a = a + 3
    elif message.text.lower() == '2':
      a = a + 2
    elif message.text.lower() == '3':
      a = a + 1  
  elif message.text.lower() == "Запитання 6":
    client.send_message(message.chat.id,'Якщо хтось із близьких купив річ, що Вам не сподобалася:')
    client.send_message(message.chat.id,'1) промовчу;')
    client.send_message(message.chat.id,'2) обмежуся коротким тактовним зауваженням;')
    client.send_message(message.chat.id,'3) влаштую скандал.')
    client.send_message(message.chat.id,'Зробіть ваш вибір:')
    if message.text.lower() == '1':
      a = a + 3
    elif message.text.lower() == '2':

Ihor Lialiuk (Job), [13.11.2021 13:29]
a = a + 2
    elif message.text.lower() == '3':
      a = a + 1  
  elif message.text.lower() == "Запитання 7":
    client.send_message(message.chat.id,'Не пощастило в лотерею. Як до цього поставитесь?')
    client.send_message(message.chat.id,'1) постараюся залишатись байдужим, але дам собі слово ніколи більше не буду брати участь у лотереї;')
    client.send_message(message.chat.id,'2) не приховуючи досади, поставлюсь до події з гумором, пообіцяю взяти реванш')
    client.send_message(message.chat.id,'3) програш надовго зіпсує настрій.')
    client.send_message(message.chat.id,'Зробіть ваш вибір:')
    if message.text.lower() == '1':
      a = a + 3
    elif message.text.lower() == '2':
      a = a + 2
    elif message.text.lower() == '3':
      a = a + 1  
    client.send_message(message.chat.id,'a')    
     



client.polling(non_stop = True, interval = 0)