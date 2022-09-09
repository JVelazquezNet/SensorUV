import tipsfull
import serial
import time
import telepot
import random
from telepot.loop import MessageLoop
from datetime import date
from datetime import datetime

# Today
today = date.today()
# Fecha actual
now = datetime.now()
#print(today)
#print(now)
#print(now.hour)



def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)

    print("\nDatos del mesaje recibido --", now)
    print("Tipo de contenido:",content_type, "\nTipo de chat:" , chat_type, "\nId de chat:", chat_id)
    print("Nombre:", msg['from']['first_name'], msg['from']['last_name'])
    print("Mensaje recibido: ", msg['text'])
    cadena1 = ''
    cadena2 = ''

    cad_recibida = msg['text'].lower()

    if content_type == 'text' and cad_recibida == '/start':
        bot.sendMessage(chat_id, '🌞 Bienvenido(a) al boot para consultar el indice ultravioleta de la ciudad de '
                                 'Zacatecas, México 🇲🇽, utiliza el comando /ayuda para recibir ayuda ℹ en '
                                 'cualquier momento, utiliza el comando /uv para recibir el indice ultravioleta 🚦 '
                                 'en tiempo real.')

    elif content_type == 'text' and cad_recibida == '/ayuda':
        bot.sendMessage(chat_id, 'Este bot reconoce los siguientes comandos: \n'
                        '/start  Muestra el mensaje de bienvenida \n'
                        '/ayuda  Muestra este menú de ayuda \n'
                        '/uv     Muestra el indice ultravioleta de la ciudad de Zacatecas en tiempo real \n'
                        '/tip   Muestra un tip aleatorio ')

    elif content_type == 'text' and cad_recibida == '/tip':
        tip = random.choice(tipsfull.my_tips)
        bot.sendMessage(chat_id, tip)
        bot.sendMessage(chat_id, tipsfull.source1)
        print("Respuesta: ", 'Tip o información')
        
    elif content_type == 'text' and cad_recibida == '/info':
        info = random.choice(tipsfull.my_info)
        bot.sendMessage(chat_id, info)
        bot.sendMessage(chat_id, tipsfull.source1)
        print("Respuesta: ", 'Tip o información')    

    elif content_type == 'text' and cad_recibida == '/uv':
        if int(format(now.hour)) >= 8 and int(format(now.hour)) <= 20:
            if cad_recibida == '/uv':
                #serial_arduino = serial.Serial("COM5", 9600)
                serial_arduino = serial.Serial("/dev/ttyUSB0", 9600)
                bot.sendMessage(chat_id, 'Consultando el índice UV')

                time.sleep(1)
                recibido = serial_arduino.readline().decode('ascii')
                string_list = recibido.split()
                try:
                    cadena1 = string_list[0]
                    cadena2 = string_list[1]
                   
                except ValueError:
                    bot.sendMessage(chat_id, "Error recuperando los valores intente de nuevo por favor")

                if cadena1 == '1':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 1⃣")
                    bot.sendMessage(chat_id, '🟩BAJO🟩  '
                                             '\nLo que significa bajo peligro para la mayoria de las personas.'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖'
                                    )
                elif cadena1 == '2':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 2⃣")
                    bot.sendMessage(chat_id, '🟩BAJO🟩  '
                                             '\nLo que significa bajo peligro para la mayoria de las personas.'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖'
                                    )
                elif cadena1 == '3':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 3⃣")
                    bot.sendMessage(chat_id, '🟨MODERADO🟨  '
                                             '\nLo que significa peligro moderado, mantente en la sombra al medio dia.'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴'
                                    )
                elif cadena1 == '4':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 4⃣")
                    bot.sendMessage(chat_id, '🟨MODERADO🟨  '
                                             '\nLo que significa peligro moderado, mantente en la sombra al medio dia.'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴'
                                    )
                elif cadena1 == '5':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 5⃣")
                    bot.sendMessage(chat_id, '🟨MODERADO🟨  '
                                             '\nLo que significa peligro moderado, mantente en la sombra al medio dia.'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴'
                                    )
                elif cadena1 == '6':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 6⃣")
                    bot.sendMessage(chat_id, '🟧ALTO🟧  '
                                             '\nLo que significa peligro alto, evita la exposicion prolongada al sol..'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴 \n'
                                             '👉Gorra o sombrero 🧢 👒'
                                    )
                elif cadena1 == '7':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 7⃣")
                    bot.sendMessage(chat_id, '🟧ALTO🟧  '
                                             '\nLo que significa peligro alto, evita la exposicion prolongada al sol..'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴 \n'
                                             '👉Gorra o sombrero 🧢 👒'
                                    )
                elif cadena1 == '8':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 8⃣")
                    bot.sendMessage(chat_id, '🟥MUY ALTO🟥  '
                                             '\nLo que significa peligro ⚠ muy alto ⚠, evita cualquier exposición '
                                             'al sol, busca la sombra en tus actividades al aire libre'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴 \n'
                                             '👉Gorra o sombrero 🧢 👒'
                                    )
                elif cadena1 == '9':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 9⃣")
                    bot.sendMessage(chat_id, '🟥MUY ALTO🟥  '
                                             '\nLo que significa peligro ⚠ muy alto ⚠, evita cualquier exposición '
                                             'al sol, busca la sombra en tus actividades al aire libre'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴 \n'
                                             '👉Gorra o sombrero 🧢 👒'
                                    )
                elif cadena1 == '10':
                    bot.sendMessage(chat_id, "🚦 El indice ultravioleta es: 🔟")
                    bot.sendMessage(chat_id, '🟥MUY ALTO🟥  '
                                             '\nLo que significa peligro ⚠ muy alto ⚠, evita cualquier exposición '
                                             'al sol, busca la sombra en tus actividades al aire libre'
                                             '\nSe recomienda usar:\n'
                                             '👉Lentes de sol. 😎  \n'
                                             '👉Ropa adecuada para cubrir la mayor parte de su cuerpo. 👕 👖 \n'
                                             '👉Protector solar (Bloqueador solar)🧴 \n'
                                             '👉Gorra o sombrero 🧢 👒'
                                    )

                bot.sendMessage(chat_id, "☀ La radiacion solar es de:  " + cadena2 + " mW/cm^2  ☀")
                print("Valores recibidos {}".format(recibido))
                serial_arduino.close()
        else:
            print("Respuesta: En estos momentos no se puede consultar la radiación UV")
            bot.sendMessage(chat_id, "🤨 En estos momentos no se puede consultar la radiación UV proveniente del sol ☀, intentalo mañana...")
    else: bot.sendMessage(chat_id, "🤨 No se reconoce el comando 🤷‍♂️")


# TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot('5365708729:AAHwL1z3TogLVGwh9bLajwBEwVuLh-t2VNs')
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
