5# Amir travel Europe — Flask

موقع أولي جاهز للتشغيل لشركة "أمير للسفر والسياحة" باستخدام Flask.

## المتطلبات
- Python 3.10+

## التثبيت والتشغيل محلياً
1. إنشاء بيئة افتراضية وتفعيلها.
2. تثبيت الاعتمادات.
3. تشغيل التطبيق.

### أوامر Powershell
```
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
python app.py
```

## بنية المشروع
- صفحات: الرئيسية، الرحلات (مع تصفية)، السائق العربي، من نحن، التواصل، المدونة، التقييمات.
- تم تفعيل قاعدة بيانات SQLite تلقائيًا عند التشغيل الأول.

## تخصيص
- عدِّل القوالب في مجلد `templates/`.
- أضف صورك إلى `static/img/`.
- لإضافة رحلات وتقييمات ومقالات لاحقاً يمكن بناء لوحة إدارة بسيطة أو استخدام سكريبتات إدخال.

## النشر على Render
تم تجهيز ملف `render.yaml` في جذر المستودع لدعم النشر على Render ضمن هيكل monorepo (المجلد `amir_travel`).

خطوات سريعة:

1) اربط مستودع GitHub/Bitbucket مع Render.
2) اختر "New +" ثم "Blueprint" وحدد المستودع الذي يحتوي على الملف `render.yaml`.
3) سيقوم Render بإنشاء خدمة ويب باسم `amir-travel-europe` تلقائياً.
4) في حالة الحاجة لتعديل البيئة:
	- SECRET_KEY: تم توليده تلقائياً.
	- DATABASE_URL: افتراضياً `sqlite:///database.db`. للإنتاج يُفضّل إضافة PostgreSQL وربط متغيّر `DATABASE_URL` بقيمة اتصال Postgres.
5) انشر وسيبدأ التشغيل باستخدام الأمر:
	- `gunicorn "app:create_app()" --bind 0.0.0.0:$PORT`

ملاحظات:
- تم تثبيت الاعتمادات من `requirements.txt` داخل المجلد `amir_travel` تلقائياً عبر `rootDir` في `render.yaml`.
- إذا غيّرت اسم الدالة أو موقع ملف التطبيق، عدّل `startCommand` وفقاً لذلك.
