import discord, os 
from dotenv import load_dotenv
import comms
import eco
from discord.ext import commands


load_dotenv ()
token = os.getenv("dt")


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name = 'hola')
async def hola(message):
    await message.channel.send(f'¡Hola, {message.author.name}! ¿Cómo puedo ayudarte hoy?')

@bot.command(name = 'adios')
async def bye(ctx):
    await ctx.channel.send(f'¡ADIOS {ctx.author.name}!')

@bot.command()
async def lista(ctx):
    await ctx.send(f'son: $hola, $adios, $pasw, $flip, $memes, $ja, $NYE, $meme $eco (1-6). quieres agregar otro(que no sea complicado)?')

@bot.command()
async def ja(ctx, count_ja = 5):
    await ctx.send("ja" * count_ja)

#Una referencia a Undertale
@bot.command(name = 'NYE')
async def ny(ctx, count_ny = 5):
    await ctx.send("IT'S ME THE GREAT PAPYRUS NYE " + "HEHEHEHE" * count_ny)

@bot.command(name = 'pasw')
async def psw(ctx, Largo: int = 20):
    pasw = comms.psw(Largo)
    await ctx.send(f"la contra es: {pasw}")

@bot.command(name='flip')
async def coin(ctx):
    stack = comms.flip_coin()
    await ctx.send(f"🪙la moneda es: {stack}")

@bot.command(name = "memes")
async def imgs(ctx):
    picture = comms.memes()
    await ctx.send(file = picture)

@bot.command(name = "eco")
async def Ecologia(ctx, opc:int):
    if opc == 1:
        await ctx.send(embed=eco.etiqueta_ambiente())
    elif opc == 2:
        await ctx.send(embed=eco.etiqueta_ambiente2())
    elif opc == 3:
        await ctx.send(embed=eco.etiqueta_ambiente3())
    elif opc == 4:
        await ctx.send(embed=eco.etiqueta_ambiente4())
    elif opc == 5:
        await ctx.send(embed=eco.etiqueta_ambiente5())
    elif opc == 6:
        await ctx.send(embed=eco.etiqueta_ambiente6()) 
    else:
        await ctx.send("no existe esa opción")    

#Pon aqui el dt del .env o el token de tu bot
bot.run("")