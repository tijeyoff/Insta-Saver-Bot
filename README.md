# ⚡ Insta-Saver Bot

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,5,30&height=180&section=header&text=Insta-Saver%20Bot&fontSize=50&fontAlignY=38&desc=High-Speed%20Telegram%20Media%20Extraction%20Engine&descAlignY=62&descSize=18&theme=tokyonight" width="100%" />

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![pyTelegramBotAPI](https://img.shields.io/badge/pyTelegramBotAPI-4.15+-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/eternnoir/pyTelegramBotAPI)
[![Instaloader](https://img.shields.io/badge/Instaloader-4.10+-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instaloader.github.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  A lightweight, high-performance Telegram bot engineered to extract and deliver Instagram Reels, Videos, and IGTV media with automatic storage management and low memory footprint.
</p>

</div>

---

## ✨ Features

- 🚀 **Instant Processing**: Automatic URL parsing and shortcode resolution.
- 📦 **Automated Cleanup**: Temporary video files and folders are automatically wiped after dispatch, preventing disk leaks.
- 🔐 **Environment Configuration**: Safe credential management via `.env` files.
- 🛡️ **Robust Error Handling**: Graceful fallback and user alerts for private posts or invalid links.
- ⚡ **Zero Bloat**: Downloads strictly the required video payload without unnecessary metadata or comments.

---

## 🛠️ Tech Stack & Requirements

- **Python**: 3.10 or higher
- **pyTelegramBotAPI**: Async / Polling Telegram client
- **instaloader**: Optimized Instagram media extraction engine
- **python-dotenv**: Environment variable loader

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/tijeyoff/Insta-Saver-Bot.git
cd Insta-Saver-Bot
```

### 2. Setup Virtual Environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file from the provided template:
```bash
cp .env.example .env
```
Open `.env` and insert your Telegram bot token obtained from [@BotFather](https://t.me/BotFather):
```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ
```

### 5. Run the Bot
```bash
python bot.py
```

---

## 📂 Project Architecture

```plaintext
Insta-Saver-Bot/
├── bot.py             # Main bot engine & event handlers
├── requirements.txt   # Project dependencies
├── .env.example       # Environment template
├── .gitignore         # Git ignore rules for safety
└── README.md          # Comprehensive documentation
```

---

## 👨‍💻 Author & Credits

Engineered by **[TIJEY](https://github.com/tijeyoff)** / **TIJEY Studio**  
- Telegram: [@tijey_12057](https://t.me/tijey_12057)  
- Instagram: [@tijey_official_](https://instagram.com/tijey_official_)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
