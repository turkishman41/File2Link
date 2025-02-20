# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["⚡️ Başlat","📚 Yardım","🔑 Giriş","DC"],
                ["TakipEt🚶","ms 📡","Durum 📊","Qurucu 😎"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["⚡️ Başlat","📚 Yardım","DC"],
                ["TakipEt🚶","ms 📡","Durum 📊","Qurucu 😎"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('⚡️ Başlat')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Yeni Üye:** \n\n____ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Botu Başlatdı !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__Botu Kullanma Yetkiniz Alındı , Kurucuyla İletişime Geçin __\n\n  ****",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/d08afd7aa60eccadaef92.jpg",
                caption="<i> Botu Kullana Bilmeniz İçin Kanala abone olmanız Gerekir🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Abone Olun 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>Bir Şey Düz Değil</i> <b> <a href='https://t.me/iLqar_turksoy'> Kurucuya Bildirin </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/d08afd7aa60eccadaef92.jpg",
        caption =f'Esenlikler , Sayğılar {m.from_user.mention(style="md")}!,\n Bu Dosya / Videolarınızdan Bağlantı  Oluşturan Botdur . \nBota herhangi bir dosya/Video gönderin, Direk İndirme  ve Akış Bağlantılarını alın. ;)',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('📚 Yardım')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i> Botu Kullanma Hakkınız Alındımış , Kötüye Kullanmaydın </i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/d08afd7aa60eccadaef92.jpg",
                Caption="** Botu Kullana Bilmeziniz için Kanala Abone olmanız Gerekir. ** __ Katıl ve kullan!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 KATILIN", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Bir şeyler düz değil , Qurucuya Bildirin__ [Qurucu](https://t.me/ilqar_turksoy).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Bota herhangi bir dosya / video gönderin, size akış bağlantısı ve Direk İndirme bağlantısı verecek.</b> \n Birde Bot Kanalları destekliyor, Botu Kanalınıza ekleyin ve herhangi bir medya dosyasını gönderin ve mucizeyi görün✨
""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ Qurucu", url="https://t.me/iLqar_TurkSoy")],
                [InlineKeyboardButton("💥 Film / Dizi", url="https://t.me/TuranMovies")]
            ]
        )
    )
