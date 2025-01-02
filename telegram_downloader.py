"""
Telegram Download Media Script
==============================
This script listens to a specified Telegram group for new messages coming
from a specific bot user, and downloads media (videos, photos) and captures
captions to a text file.

Dependencies:
    - asyncio
    - telethon

Usage:
    - Update 'api_id', 'api_hash', 'group_name', and 'bot_username'.
    - Execute this script using an asyncio-compatible environment, e.g.:
      `python -m asyncio your_script.py`
    - The user may be prompted for phone/bot token credentials when run the first time.
"""

import os
import asyncio
import datetime
from telethon import TelegramClient, events

# Replace these with your own values
API_ID = ""
API_HASH = ""
GROUP_NAME = ''           # The name of the group you want to listen to
BOT_USERNAME = ''         # The username of the bot (without '@')
SESSION_NAME = 'session_name'

async def download_media(api_id: str = API_ID,
                         api_hash: str = API_HASH,
                         session_name: str = SESSION_NAME,
                         group_name: str = GROUP_NAME,
                         bot_username: str = BOT_USERNAME) -> None:
    """
    Listen for new messages in a specified Telegram group from a specified bot user,
    download any media in those messages, and save captions to a text file.

    :param api_id: Your Telegram API ID.
    :param api_hash: Your Telegram API hash.
    :param session_name: A name for the local session file.
    :param group_name: The name of the target group to listen to.
    :param bot_username: The bot username to filter the messages from.
    """

    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    # Check if we can find the group
    dialogs = await client.get_dialogs()
    group_found = None
    for dialog in dialogs:
        if dialog.is_group and dialog.name == group_name:
            group_found = dialog.entity
            print(f"Found group '{group_name}' with ID {group_found.id}")
            break

    if group_found is None:
        print(f"Could not find group with title '{group_name}'")
        await client.disconnect()
        return

    @client.on(events.NewMessage(chats=group_name, from_users=bot_username))
    async def handler(event):
        """
        Event handler for new messages that come from the specified bot user in the group.
        If the message contains media, download it and save any caption to a text file.
        """
        message = event.message

        if message.media:
            # Format part of the path with date + message.id
            date_str = message.date.strftime("%Y_%m_%d_%H_%M_%S")
            m_id = f"{date_str}_{message.id}"

            # Create a unique download folder for this media
            download_folder = os.path.join('downloads', m_id)
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            # Download media to that folder
            file_path = await client.download_media(message, download_folder)
            print(f"Downloaded media to {file_path}")

            # Save the caption (if any) in a text file alongside the media
            caption = message.text or ''
            if caption:
                # Use the same base filename for the caption
                caption_base = os.path.splitext(os.path.basename(file_path))[0]
                caption_filename = os.path.join(download_folder, f"{caption_base}.txt")

                with open(caption_filename, 'w', encoding='utf-8') as f:
                    f.write(caption)
                print(f"Saved caption to {caption_filename}")
        else:
            print("Message does not contain media.")

    print("Listening for new messages... Press Ctrl+C to stop.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    # Run the main download coroutine
    asyncio.run(download_media())
