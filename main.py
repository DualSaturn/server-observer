import discord
from markov_generator import MarkovGenerator

client = discord.Client()

@client.event
async def on_message(message):
    server_name = message.server.name
    if 'server-observer, what do you see' in message.content.lower().strip(): #ignores the message if it has the activation message
        with open('{}.txt'.format(server_name), 'r') as chat_log:
            text = chat_log.read()
            markgen = MarkovGenerator(text)
            await client.send_message(message.channel, markgen.create_markov_chain_text(100))
    elif message.author.bot is False: #ignores messages from bots
        with open('{}.txt'.format(server_name), 'a') as chat_log:
            chat_log.write('{}\n'.format(message.content))

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

client.run('insert_token_here')
