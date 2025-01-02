"""
Telegram Sender Script
======================
This script sends URLs from a JSON file to a specified Telegram group,
with a configurable delay between each send.

Dependencies:
    - asyncio
    - telethon

Usage:
    - Update 'api_id', 'api_hash', 'group_name', 'group_id', and 'json_file_path'.
    - Execute this script using an asyncio-compatible environment, e.g.:
      `python -m asyncio your_script.py`
    - The user may be prompted for phone/bot token credentials when run the first time.
"""

import asyncio
import json
from telethon import TelegramClient

# Replace these with your own values
API_ID = ""
API_HASH = ""
GROUP_NAME = ''        # The name of the group
GROUP_ID = ...         # The ID of the group
JSON_FILE_PATH = 'post_urls.json'
SESSION_NAME = 'session_name'

# Delay (in seconds) between sending URLs
SEND_DELAY_SECONDS = 120

async def send_urls(api_id: str = API_ID,
                    api_hash: str = API_HASH,
                    session_name: str = SESSION_NAME,
                    group_name: str = GROUP_NAME,
                    group_id: int = GROUP_ID,
                    json_file_path: str = JSON_FILE_PATH,
                    send_delay_seconds: int = SEND_DELAY_SECONDS) -> None:
    """
    Send URLs from a JSON file to a given Telegram group with a delay between messages.
    
    :param api_id: Your Telegram API ID.
    :param api_hash: Your Telegram API hash.
    :param session_name: A name for the local session file.
    :param group_name: The name of the target group.
    :param group_id: The ID of the target group.
    :param json_file_path: The path to the JSON file containing URLs.
    :param send_delay_seconds: The number of seconds to wait between sending URLs.
    """
    # Initialize and start the client
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    # Fetch all dialogs (conversations)
    dialogs = await client.get_dialogs()

    # Attempt to find the specified group by name or ID
    group = None
    for dialog in dialogs:
        if dialog.is_group and (dialog.name == group_name or dialog.entity.id == group_id):
            group = dialog.entity
            print(f"Found group '{group_name}' with ID {group.id}")
            break

    # If we don't find the group, exit
    if group is None:
        print(f"Could not find group with title '{group_name}' or ID '{group_id}'")
        await client.disconnect()
        return

    # Read the URLs from the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as f:
        urls = json.load(f)

    # Iterate over URLs and send each one to the group
    for url in urls:
        print(f"Sending URL to group '{group_name}': {url}")
        await client.send_message(group, url)
        print(f"URL sent: {url}")

        # Wait before sending the next URL
        print(f"Waiting for {send_delay_seconds} seconds...")
        await asyncio.sleep(send_delay_seconds)

    print("All URLs processed. Disconnecting client.")
    await client.disconnect()

if __name__ == "__main__":
    # Run the main sending coroutine
    asyncio.run(send_urls())
