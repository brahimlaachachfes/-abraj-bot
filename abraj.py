import os, random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")



abraj = {
    "الحمل": ["نهارك فيه حماس", "طاقة كبيرة"],
    "الثور": ["نهار ديال الفلوس", "مفاجأة زوينة"],
    "الجوزاء": ["أفكار بزاف", "تواصل مع ناس جدد"],
    "السرطان": ["العائلة أولا", "نهار حنان"],
    "الاسد": ["بان ووري خدمتك", "الأنظار عليك"],
    "العذراء": ["نظم وقتك", "رد بالك للتفاصيل"],
    "الميزان": ["توازن هو الحل", "قرار مهم"],
    "العقرب": ["خدم فصمت", "الصبر هو قوتك"],
    "القوس": ["سفر وأفكار جديدة", "مغامرة"],
    "الجدي": ["الخدمة هي المفتاح", "غادي توصل"],
    "الدلو": ["فكرة جديدة جاية", "خليك مبدع"],
    "الحوت": ["خليك مع راسك", "خيالك واسع"]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌟 مرحبا بيك\nكتب برجك: الحمل، الثور، الجوزاء، السرطان، الاسد، العذراء، الميزان، العقرب، القوس، الجدي، الدلو، الحوت")

async def borj_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()
    for name in abraj:
        if name in msg:
            await update.message.reply_text(f"🔮 برج {name} اليوم:\n{random.choice(abraj[name])}")
            return
    await update.message.reply_text("كتب برجك: الحمل...")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, borj_handler))
app.run_polling()
