import asyncio
import edge_tts
import os

TEXT = "Welcome back to our daily tech insights. Today we are exploring automated video creation using code."
VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "public/audio.mp3"

async def generate_audio():
    os.makedirs("public", exist_ok=True)
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print("✅ تم توليد الملف الصوتي بنجاح داخل مجلد public!")

if __name__ == "__main__":
    asyncio.run(generate_audio())
