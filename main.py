import discord
from discord.ext import commands
import random, os
import requests



#Intents son las acciones que el bot puede realizar
intents = discord.Intents.default()
intents.message_content = True

#Iniciando nuestro bot
bot = commands.Bot(command_prefix='$', intents = intents)

#Evento que se despliega al inciar nuestro bot
@bot.event
async def on_ready():
    print(f"has iniciado como {bot.user}")

#Estableciendo el comando llamado meme_pro, para memes de la programacion
@bot.command()
async def meme_pro(ctx):
    imagenes_cargadas = random.choice(os.listdir("Imagenes"))
    with open(f'Imagenes/{imagenes_cargadas}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file = picture)

#Estableciendo el comando llamado meme_ani, para memes de la animales
@bot.command()
async def meme_ani(ctx):
    imagenes_cargadas = random.choice(os.listdir("Ani_memes"))
    with open(f'Ani_memes/{imagenes_cargadas}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file = picture)


#Imagen de pato
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("TOKEN")
