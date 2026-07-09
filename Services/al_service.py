import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")

def generate_task_plan(task_name: str, available_hours: float) -> dict:
    prompt = f"""
انت مساعد ذكي بيساعد المستخدمين في تخطيط مهامهم.

المهمة: {task_name}
عدد الساعات المتاحة يوميًا: {available_hours}

المطلوب منك:
1. تقدير عدد الأيام اللي محتاجها المستخدم عشان يخلص المهمة دي بالظبط بناءً على الساعات المتاحة.
2. حدد هل التقسيم المناسب يومي ولا شهري (لو المهمة كبيرة جدًا اعمله تقسيم شهري، لو صغيرة اعمله تقسيم يومي).
3. اعمل خطة مقسمة (breakdown) كل نقطة فيها تكون خطوة واضحة أو مرحلة معينة من المهمة.
4. اديله 3 لـ 5 نصايح عملية تساعده يخلص المهمة بكفاءة.

مهم جدًا: رد بصيغة JSON فقط وبدون أي نص إضافي أو markdown، بالشكل ده بالظبط:

{{
  "estimated_days": <رقم>,
  "breakdown_type": "daily" أو "monthly",
  "plan": ["...", "...", "..."],
  "tips": ["...", "...", "..."]
}}
"""

    response = model.generate_content(prompt)
    raw_text = response.text.strip()

    # تنظيف أي markdown fences لو اتبعتت غصب
    if raw_text.startswith("`"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.replace("json", "", 1).strip()

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        raise ValueError("الرد من الـ AI مش JSON صالح: " + raw_text)

    return data