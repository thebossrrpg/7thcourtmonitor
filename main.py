import telebot
import os

# Coloque aqui o token que o BotFather te deu
TOKEN = '8218809414:AAFDn5ydA0sM9Y2oOUvUrxGj-kuvOA-Yk8M'

bot = telebot.TeleBot(TOKEN)

# Responde ao comando /re (qualquer pessoa no grupo ou privado)
@bot.message_handler(commands=['re'])
def enviar_notificacao(message):
    texto = "Uma nova resposta foi enviada em 7th Court Roleplay."

    # Envia a notificação
    bot_reply = bot.reply_to(message, texto)

    # Apaga o comando que a pessoa digitou (/re ou /re@nome_do_bot)
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass  # se já foi apagado ou não tiver permissão, ignora

# === AQUI VOCÊ ESCOLHE QUANTO TEMPO A NOTIFICAÇÃO FICA VISÍVEL ===
    tempo_em_segundos = 86400  # 86400 segundos = 24 horas
    # Exemplos que você pode usar trocando o número acima:
    # 10    → 10 segundos
    # 30    → 30 segundos  
    # 60    → 1 minuto
    # 300   → 5 minutos
    # 3600  → 1 hora
    # 86400 → 24 horas (1 dia)

    # Apaga a própria mensagem do bot depois do tempo escolhido
    def apagar_depois():
        threading._start_new_thread(lambda: (
            __import__('time').sleep(tempo_em_segundos),
            bot.delete_message(message.chat.id, bot_reply.message_id)
        )[1])()

    apagar_depois()

# Mensagem de start (opcional, só pra testar)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot ativo! Use /re no grupo para enviar a notificação manualmente.")

print("Bot rodando 24/7 - comando /re some automaticamente")
bot.infinity_polling()
