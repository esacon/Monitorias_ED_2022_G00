import os
import dotenv
import Bot as bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


# Cargaremos las variables de entorno a nuestro entorno de ejecución.
dotenv.load_dotenv()
TOKEN = os.environ.get('TOKEN') # Recuperamos el valor del TOKEN.


def main():
    # Establecemos una conexión entre nuestro programa y el bot.
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher # Despachador de solicitudes.

    # Estableces los comandos de ejecución del bot.
    dp.add_handler(CommandHandler("start", bot.start))
    dp.add_handler(CommandHandler("ayuda", bot.ayuda))
    dp.add_handler(CommandHandler("secuencia", bot.secuencia))
    
    # Respuesta a los Callbacks del bot.
    dp.add_handler(CallbackQueryHandler(bot.help_menu, pattern='a1'))
    dp.add_handler(CallbackQueryHandler(bot.help_menu, pattern='a2'))
    dp.add_handler(CallbackQueryHandler(bot.help_menu, pattern='a3'))

    # Iniciar el bot.
    updater.start_polling()
    # Mantener el bot ejecutándose hasta que ocurra una interrupción.
    updater.idle()



if __name__ == '__main__':
    main()
