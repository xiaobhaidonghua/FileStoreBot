![FileStoreBot Banner](start.jpg)

# 🌟 Give it a star. 🌟

# FileStoreBot
🎯 **A Telegram Bot to Store and Share Files with a Single Link**  
🧑‍💻 Developed by [@Prime_Hritu](https://t.me/Prime_Hritu)  
📢 Stay updated via our [Developer Channel](https://t.me/Private_Bots)  

---

## 🌟 Features
✅ Store files securely in Telegram  
✅ Get unique shareable links for each file  
✅ Generate QR codes for easy sharing  
✅ List and delete your stored files  
✅ Simple configuration and deployment  
✅ Admin broadcast and statistics panel  

---

## ⚙️ Configuration Variables

Set these environment variables to configure your bot (see [`config.py`](config.py)):

| Variable             | Description                                                        |
|----------------------|--------------------------------------------------------------------|
| `BOT_TOKEN`          | Bot Token from [@BotFather](https://t.me/BotFather)                |
| `API_ID`             | API ID from [my.telegram.org](https://my.telegram.org/apps)        |
| `API_HASH`           | API Hash from [my.telegram.org](https://my.telegram.org/apps)      |
| `MONGO_URI`          | MongoDB connection URI                                             |
| `DATABASE_NAME`      | Name of the MongoDB database (default: "FileDrawerBot")            |
| `STORAGE_CHANNEL_ID` | Telegram channel ID for storing files                              |
| `ADMIN_USER_IDS`     | Comma-separated list of admin user IDs                             |

---

## 🚀 Deployment

### 🐧 Ubuntu Deployment

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
git clone https://github.com/Private-Bots-Official/FileStoreBot
cd FileStoreBot
pip3 install -r requirements.txt
cp .env-example .env  # Edit .env with your variables
python3 main.py
```

### ☁️ One-Click Deployment

> **Coming soon:** Deploy to Heroku, Koyeb, or Render with one click!

---

## 📦 Usage

- **/start** – Show welcome message or retrieve a file by UUID  
- **/list** – List your stored files  
- **/delete `<FILE_UUID>`** – Delete a file you own  
- **/help** – Show help message  
- **Send any file** – Store it and get a shareable link & QR code  
- **Admins:**  
  - **/stats** – Show bot statistics  
  - **/broad** – Broadcast a message to all users

---

## 📞 Contact

[![@Prime_Hritu](https://stylish-social-buttons.vercel.app/?social=telegram&text=Prime_Hritu)](https://t.me/Prime_Hritu)  
[![@Private_Bots](https://stylish-social-buttons.vercel.app/?social=telegram&text=Private_Bots)](https://t.me/Private_Bots)

---

## 📚 Libraries Used

See [`requirements.txt`](requirements.txt) for all dependencies.

---

## 🔖 License

This project is licensed under the MIT License.

---