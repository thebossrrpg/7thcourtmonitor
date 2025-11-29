import telebot
import os

# Coloque aqui o token que o BotFather te deu
TOKEN = '8218809414:AAFDn5ydA0sM9Y2oOUvUrxGj-kuvOA-Yk8M'

bot = telebot.TeleBot(TOKEN)

# Responde ao comando /re (qualquer pessoa no grupo ou privado)
@bot.message_handler(commands=['re'])
def enviar_notificacao(message):
    resposta = "Uma nova resposta foi enviada em 7th Court Roleplay."
    bot.reply_to(message, resposta)

# Mensagem de start (opcional, só pra testar)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot ativo! Use /re no grupo para enviar a notificação manualmente.")

print("Bot rodando...")
bot.infinity_polling()
