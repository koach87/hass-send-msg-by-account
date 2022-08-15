@service
async def open_door(api_id = None, api_hash = None, chat_id = None, msg = None):
    from telethon.sync import TelegramClient

    log.info('start sending msg to open door')
    
    async with TelegramClient('name', api_id, api_hash) as client:
        await client.send_message(chat_id, msg)