import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Você entrou como {bot.user}")


@bot.command()
async def lixo(ctx, lixo: str):
    lixo = lixo.lower().strip()

    await ctx.send(f"O tipo de lixo que você digitou é: {lixo}")

    if lixo == "papel":
        await ctx.send("A lata de lixo correta para papel é a azul.")

    elif lixo in ("plastico", "plástico"):
        await ctx.send("A lata de lixo correta para plástico é a amarela.")

    elif lixo == "vidro":
        await ctx.send("A lata de lixo correta para vidro é a verde.")

    elif lixo == "metal":
        await ctx.send("A lata de lixo correta para metal é a vermelha.")

    elif lixo in ("organico", "orgânico"):
        await ctx.send("A lata de lixo correta para orgânico é a marrom.")

    elif lixo in ("eletronico", "eletrônico"):
        await ctx.send("A lata de lixo correta para eletrônico é a cinza.")

    elif lixo in ("pilha", "bateria"):
        await ctx.send("A lata de lixo correta para pilhas e baterias é a preta.")

    else:
        await ctx.send(
            "Não reconheci esse tipo de lixo. "
            "Tente: papel, plástico, vidro, metal, orgânico, eletrônico, pilha ou bateria."
        )


bot.run("YOUR_BOT_TOKEN")