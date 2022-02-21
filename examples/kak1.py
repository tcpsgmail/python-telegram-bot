
from datetime import datetime
from telethon import TelegramClient, events
 
api_id = 15609062
api_hash = '69e5aa1441115f50690050a3e5b4ea92'
client = TelegramClient('anon', api_id, api_hash)
 
 
def log_userid(userid):
    with open("userid.txt", "a", encoding='utf-8') as f:
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f'\n{userid} {dt}')
 
 
@client.on(events.NewMessage(chats='@kakmehuy'))
async def my_event_handler(event):
    log_userid('@kakmehuy')
    await client.send_message(entity='@huyccc', message=event.message)
 
 
@client.on(events.NewMessage(chats='@huy_kak'))
async def my_event_handler(event):
    log_userid('@huy_kak')
    await client.send_message(entity='@huyccc', message=event.message)
    
    
@client.on(events.NewMessage(chats='@Big_Pumps_Signals'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@Big_Pumps_Signals')
 
 
@client.on(events.NewMessage(chats='@durak_kak'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@durak_kak')
 
 
@client.on(events.NewMessage(chats='@cryptoc'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@cryptoc')
 
 
@client.on(events.NewMessage(chats='@Binance_Pumps_Futures_Signals7'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@Binance_Pumps_Futures_Signals7')
 
 
@client.on(events.NewMessage(chats='@quote'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@quote')
 
 
@client.on(events.NewMessage(chats='@bestmemes'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@bestmemes')
 
 
@client.on(events.NewMessage(chats='@Funny'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@Funny')
 
 
@client.on(events.NewMessage(chats='@durak_kak'))
async def my_event_handler(event):
    await client.send_message(entity='@huyccc', message=event.message)
    log_userid('@durak_kak')
 
 
client.start()
client.run_until_disconnected()
