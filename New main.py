import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send("Guess a number between 1 and 10.")

@bot.command()
async def answer(ctx, n):
    if n == random.randint(1, 10):
        await ctx.send('Nice guessing!!!')
    else:
        await ctx.send('Nahhh...., You wrong!!!')

@bot.command()
async def coins(ctx):
    await ctx.send("Guess a side coins between tails or heads.")
@bot.command()
async def coinside(ctx, ans):
    side = ["tails","head"]
    m = (random.choice(side))
    if ans == m:
        await ctx.send('Nice guessing!!!')
        await ctx.send('the coins side is', m)
    else:
        await ctx.send('Nahhh...., You wrong!!!')
        await ctx.send('the true coins side is', m)

@bot.command()
async def meme(ctx):
    images = os.listdir('images')
    with open('images/'+random.choice(images), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def Joke_Gelap(ctx):
    await ctx.send("Negara apa yang gampang kalah dalam permainan catur??")
    
@bot.command()
async def Jawab(ctx, jawab):
    if jawab == 'UK':
        await ctx.send("Selamat Kamu Benar!!!")
        await ctx.send("Karena ratunya mati awokawok")
    else:
        await ctx.send("Salah Nyet!!!....")
        await ctx.send("Yang bener UK!!!....")
        await ctx.send("Karena ratunya mati :)")
@bot.command()
async def waktu_sampah_terurai(ctx):
    await ctx.send("Sampah Jenis Apa yang Kamu Ingin Tanyakan??")
    await ctx.send("Jenis sampah yang sudah terdaftar:")
    await ctx.send("1. Organik basah, dengan command = $jenis_sampah Organik Basah")
    await ctx.send("2. Sisa makanan, dengan command = $jenis_sampah Sisa Makanan")
    await ctx.send("3. Plastik, dengan command = $jenis_sampah Plastik")
    await ctx.send("Jenis sampah lain akan menyusul........")
@bot.command()
async def jenis_sampah(ctx, jawaban):
    if jawaban == 'Organik Basah':
        await ctx.send("Untuk sampah jenis organik basah")
        await ctx.send("Biasanya memakan waktu sekitar sekitar seminggu tergantuh jenisnya :)")
    if jawaban == 'Sisa Makanan':
        await ctx.send("Untuk sampah jenis sisa makanan")
        await ctx.send("Biasanya memakan waktu sekitar 1 bulan untuk terurai")
    if jawaban == 'Plastik':
        await ctx.send("Plastik jenis apa??")
        await ctx.send("Jenis sampah plastik yang sudah terdaftar:")
        await ctx.send("Botol plastik, dengan command = $plastik Botol")
        await ctx.send("Sterofom, dengan command = $plastik Sterofom")
        await ctx.send("Jenis samapah plastik lain akan menyusul.......")
        
    else:
        await ctx.send("Sampah ketagori ini belum terdaftar....")

@bot.command()
async def plastik(ctx, pls):
    if pls == 'Botol':
        await ctx.send("Untuk ketagori sampah ini termasuk sampah yang sulit terurai!!")
        await ctx.send("Waktu yang dibutuhkan bahkan hingga 450 tahun")
    if pls == 'Sterofom':
        await ctx.send("Untuk ketagori sampah ini termasuk sampah yang sangat sulit terurai!!!")
        await ctx.send("Untuk sampah plastik sterofom, tidak dapat terurai secara alami")
        await ctx.send("Dan dapat terurai dalam waktu sekitar 500 tahun!!")
        await ctx.send("Dan dalam proses penguraiannya, sampah ini menghasilkan racun yang berbahaya!!!!")
    else:
        await ctx.send("Sampah ketagori ini belum terdaftar....")

bot.run("Rahasia Dong")
