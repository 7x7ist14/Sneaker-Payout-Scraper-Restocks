import discord
import main
import datetime
from discord.ext import commands
from config import TOKEN, CHANNEL_NAME, COMMAND_PREFIX

restocks_payout = main.restocks_stock
restocks_url = main.restocks_url
stockx_url = main.stockx_url
hypeboost_url = main.hypeboost_product_url
sneakit_url = main.sneakit_product_url
goat_url = main.product_goat
product_picture = main.restocks_product_img
product_title = main.product_title



if not TOKEN:
    raise ValueError("The Bot-Token was not included in the config.py file")

if not CHANNEL_NAME:
    raise ValueError("The Channel-Name was not included in the config.py file")

if not COMMAND_PREFIX:
    raise ValueError("The Command-Prefix was not included in the config.py file")


bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Scraping! (Payout Restocks)'))
    print("Bot logged in!")


@bot.event
async def on_message(message):
  if message.author == bot.user:
      return
  message_content = message.content.lower()

  if message.channel.name == CHANNEL_NAME:
    if message.content.startswith(COMMAND_PREFIX):
      await message.channel.send("Scraping...")

      if COMMAND_PREFIX in message_content:
        SKU_raw = message_content.replace(COMMAND_PREFIX, '')
        SKU = SKU_raw.replace(" ", "")
        restocks_payout_output = restocks_payout(SKU)
        restocks_url_output = restocks_url(SKU)
        hypeboost_url_output = hypeboost_url(SKU)
        stockx_url_output = stockx_url(SKU)
        sneakit_url_output = sneakit_url(SKU)
        product_picture_output = product_picture(SKU,restocks_url)
        product_title_output = product_title(SKU)
        goat_url_output = goat_url(SKU)

        embed = discord.Embed(
          title=product_title_output,
          url=restocks_url_output,
          color=0x607d8b
        )
        embed.set_author(
          name="Restocks Payout Scraper",
          url="https://twitter.com/jakobaio",
          icon_url= "https://www.reklamation24.de/img/content/marken/original_6710_1.gif"
          )
        embed.set_thumbnail(
          url=product_picture_output
        )
        embed.add_field(
          name="Payout Prices:",
          value=restocks_payout_output
        )
        embed.set_footer(
          text="Developed by Jakob.AIO"
        )
        embed.add_field(
          name="Open Product on:",
          value=f"[[StockX]]({stockx_url_output})      " f"[[Sneakit]]({sneakit_url_output})      " f"[[Restocks]]({restocks_url_output})      " f"[[Hypeboost]]({hypeboost_url_output})      " f"[[GOAT]]({goat_url_output})      ",
          inline=False
        )
        embed.set_footer(
          text=f"Developed by JakobAIO      |      Restocks-Payout      |      {datetime.datetime.now().strftime('%H:%M:%S')}"
        )

        await message.channel.send(embed=embed)
        print('Payout Scraping Successful!')


bot.run(TOKEN)
