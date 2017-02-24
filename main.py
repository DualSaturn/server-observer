import discord
from markov_generator import MarkovGenerator

client = discord.Client()

@client.event
async def on_message(message):
    if 'server-observer, what do you see' in message.content.lower():
        chat_log_text = ''
        async for msg in client.logs_from(message.channel, limit = 500):
            if not msg.author.bot and 'server-observer, what do you see' not in msg.content.lower(): #ignores bots and messages with the activation phrase
                chat_log_text += '{}\n'.format(msg.content)
        markgen = MarkovGenerator(chat_log_text)
        await client.send_message(message.channel, markgen.create_markov_chain_text(100))

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

client.run('insert_token_here')
