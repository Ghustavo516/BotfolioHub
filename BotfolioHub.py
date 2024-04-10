import telebot

CHAVE_API = "<insert your API Token here>"
bot = telebot.TeleBot(CHAVE_API)

# Opcoes de contato
@bot.message_handler(commands=["Linkedin"])
def linkedin(mensagem):
    bot.reply_to(mensagem, "<insert your linkedin here>")
   
@bot.message_handler(commands=["WhatsApp"])
def whatsapp(mensagem):
    bot.send_contact(mensagem.chat.id, phone_number="<insert your phone number here>", first_name="<insert your first name here>")
    
@bot.message_handler(commands=["Email"])
def email(mensagem):
    bot.reply_to(mensagem, "<insert your email here>") 
    
# Opcoes do menu
@bot.message_handler(commands=["opcao1"])
def opcao(mensagem):
    bot.reply_to(mensagem, "<insert your resume url here>")
     
@bot.message_handler(commands=["opcao2"])
def opcao(mensagem):
    bot.send_photo(mensagem.chat.id, photo='https://beecrowd.io/wp-content/uploads/2022/08/Beecrowd-Agosto-6-02-larger.png', caption="Meu GitHub: \n <insert your GitHub url here>")
    
@bot.message_handler(commands=["opcao3"])
def opcao(mensagem):
    bot.send_photo(mensagem.chat.id, photo='https://i.pinimg.com/736x/fb/07/cd/fb07cd9fd5fa37f9be69c23e73d46d70.jpg', caption="Meu portifolio: \n <insert your portifolio url here>")
    
    
@bot.message_handler(commands=["opcao4"])
def opcao(mensagem):
    texto = """
    Escolha  uma opção para continuar (Clique no item):
    /Linkedin
    /WhatsApp
    /Email
    """
    bot.reply_to(mensagem, "Que legal!, Como voce prefere entrar em contato ?")
    bot.send_message(mensagem.chat.id, texto)
    

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Olá!")
    texto = """
    Escolha  uma opção para continuar (Clique no item):
    /opcao1 Baixar Curriculo
    /opcao2 Acessar o Github
    /opcao3 Ver portifolio
    /opcao4 Entrar em contato
    """
    bot.send_message(mensagem.chat.id, texto)
    
while True:    
    bot.polling()
