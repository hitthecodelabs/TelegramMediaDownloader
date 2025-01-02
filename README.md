# Telegram URL Sender & Media Downloader

A collection of two scripts that enable you to:
1. Send URLs from a JSON file to a Telegram group at a specified interval.
2. Listen in a Telegram group for media sent by a specific bot user and automatically download those media files (and their captions) to local storage.

## Table of Contents

- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [API Credentials](#api-credentials)
- [Usage](#usage)
  - [Sender Script](#sender-script)
  - [Downloader Script](#downloader-script)
- [Project Structure](#project-structure)
- [Security Disclaimer](#security-disclaimer)
- [License](#license)

---

## Requirements

- Python 3.7+  
- [Telethon](https://github.com/LonamiWebs/Telethon)  

---

## Getting Started

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hitthecodelabs/TelegramMediaDownloader.git
   cd TelegramMediaDownloader
   ```

2. **Install dependencies (preferably inside a virtual environment)**:
   ```bash
   pip install -r requirements.txt
   ```

   If you don’t already have `requirements.txt`, create one with:
   ```text
   telethon
   ```

   Or simply install Telethon directly:
   ```bash
   pip install telethon
   ```

---

### API Credentials

You must have a Telegram API ID and API Hash.

1. Sign in at [my.telegram.org](https://my.telegram.org).
2. Go to **API development tools**.
3. Copy the `api_id` and `api_hash` and place them in the scripts.

---

## Usage

### Sender Script

**File**: `telegram_sender.py`

This script reads from a JSON file containing URLs (e.g., `post_urls.json`) and sends them one by one to a specified Telegram group with a configurable delay between each send.

**Update the following variables in the script**:

- `API_ID`
- `API_HASH`
- `GROUP_NAME`
- `GROUP_ID`
- `JSON_FILE_PATH`
- `SEND_DELAY_SECONDS` (optional, default is 120 seconds)

**Run the script**:
```bash
python telegram_sender.py
```

On the first run, you’ll be prompted to enter your phone number and the code you receive from Telegram. A session file (e.g., `session_name_001.session`) will be created for subsequent runs.

---

### Downloader Script

**File**: `telegram_downloader.py`

This script listens to a specified Telegram group for messages from a particular bot user. If the message contains media, it downloads the media and the accompanying caption (if any) to local storage.

**Update the following variables in the script**:

- `API_ID`
- `API_HASH`
- `GROUP_NAME`
- `BOT_USERNAME`

**Run the script**:
```bash
python telegram_downloader.py
```

Again, you may be asked for your phone number and verification code the first time you run this script. You can stop listening at any time by pressing `Ctrl + C`.

---

## Project Structure

Below is an example structure for your repository:

```
telegram-url-sender-media-downloader/
├─ downloads/                 # Downloaded media files (auto-created by script)
├─ post_urls.json             # Example JSON file with URLs
├─ telegram_sender.py         # Script to send URLs to a Telegram group
├─ telegram_downloader.py     # Script to download media from a Telegram group
├─ requirements.txt           # Required Python packages (i.e., Telethon)
└─ README.md                  # Project documentation
```

---

## Security Disclaimer

- Never share your `api_id` and `api_hash` publicly. Treat them as sensitive credentials.
- Do not commit your session files (`.session`) to version control.
- Ensure you comply with Telegram’s Terms of Service while using these scripts.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this code as permitted by the license.

---

Happy Coding! If you find this useful, consider giving it a star on GitHub.
