import logging
import Mensajes as msj
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


logging.basicConfig(level=logging.INFO, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

def start(update, context):
    user_name = update.message.chat.first_name
    logger.info(f"El usuario {user_name}, ha iniciado el BOT.")
    update.message.reply_text(f'¡Hola {user_name}, un gusto tenerte por acá!')
    logger.info("Bot iniciado.")


def saludar(query):
    logger.info('El usuario ha llamado la función `saludar()`')
    user_name = query.message.chat.first_name
    query.message.reply_text(f'¡Hola {user_name}, un gusto tenerte por acá!')
    logger.info("Saludo enviado.")


def secuencia_info(query):
    user_name = query.message.chat.first_name
    logger.info(f'El usuario {user_name} ha solicitado inforamción del comando `secuencia()`.')

    query.message.reply_text(msj.secuencia_message, parse_mode='MarkdownV2')


def secuencia(update, context):
    logger.info("Se enviará una secuencia:")
    text = update.message.text
    text = text.replace("/secuencia", "").strip()
    datos = text.split(";")
    if text == "":
        update.message.reply_text(msj.secuencia_message, parse_mode='MarkdownV2')
    elif len(datos) == 2:
        try:
            lista = eval(datos[0])
            filtro = int(datos[1])
            update.message.reply_text("Los elementos filtrados de la lista son:")
            for i in [j for j in lista if j % filtro == 0]:
                update.message.reply_text(i)
        except:
            update.message.reply_text("Los parámetros no son válidos, por favor intente nuevamente.")
    else:
        update.message.reply_text("La cantidad parámetros no corresponden, por favor intente nuevamente.")


def send_image(query):
    name = query.message.chat.first_name
    logger.info(f'El usuario {name} ha solicitado una imagen.')

    chat_id = query.message.chat_id
    img = open('img/prueba.png', 'rb')
    query.message.reply_text('Cargando imagen...')
    query.bot.sendPhoto(chat_id=chat_id, photo=img, timeout=120)



def help_menu(update, context):
    query = update.callback_query
    query.answer()
    callback = query.data
    if callback == 'a1':
        saludar(query)
    elif callback == 'a2':
        secuencia_info(query) 
    else:
        send_image(query)


def ayuda(update, context):
    logger.info("El usuario ha solicitado el menu de ayuda.")
    options = [
        [InlineKeyboardButton("Start", callback_data='a1')],
        [InlineKeyboardButton("Secuencia", callback_data='a2')],
        [InlineKeyboardButton("Imagen", callback_data='a3')]
    ]

    reply_markup = InlineKeyboardMarkup(options)
    update.message.reply_text("A continuación se listan las funciones del bot: ", reply_markup=reply_markup)
    logger.info('Se ha desplegado el menú de ayuda.')
