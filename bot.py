import os
import db
import nextcord

from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord import SlashOption, Embed

load_dotenv()

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.slash_command(name="quote", description="quote a person")
async def quote(interaction: nextcord.Interaction,
                quote: str = SlashOption(description="quote string"),
                person: str = SlashOption(description="the person beeing quoted"),
                year: str = SlashOption(description="the year the person said the quote")):
    db.add_quote_to_db(quote.lower(), person.lower(), year)
    await interaction.send(f"{interaction.user} added: ```\"{quote}\" - {person}, {year}```")


@bot.slash_command(name="get_quotes", description="Get the quotes from a specific person")
async def get_quotes(interaction: nextcord.Interaction, person: str = SlashOption(description="the person to get quotes from"),):
    embed = nextcord.Embed(title=f"{person}", description=f"this is all quotes form {person}", color=0x000ff)
    text = ""
    for (quote, person, year) in db.get_quotes_from_person(person):
        text = f"{text}```\"{quote}\", {year}```"
    embed.add_field(name=f"The quotes", value=text, inline=False)
    await interaction.send(embed=embed)


bot.run(os.getenv("TOKEN"))
