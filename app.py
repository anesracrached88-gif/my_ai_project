from flask import Flask, render_template, request
import os

app = Flask(__name__)

# قاعدة البيانات الشاملة
database = [
    # ذكاء اصطناعي
    {"name": "Gemini AI", "desc": "مساعد جوجل الذكي للبرمجة والبحث.", "cat": "AI Partner", "link": "https://gemini.google.com", "price": "Free"},
    {"name": "ChatGPT", "desc": "نموذج لغوي قوي من OpenAI.", "cat": "AI Partner", "link": "https://chat.openai.com", "price": "Freemium"},
    {"name": "Claude AI", "desc": "منافس قوي في التحليل والبرمجة.", "cat": "AI Partner", "link": "https://claude.ai", "price": "Freemium"},
    # أفلام
    {"name": "Netflix", "desc": "أضخم منصة للأفلام والمسلسلات.", "cat": "Movies", "link": "https://netflix.com", "price": "Paid"},
    {"name": "Fmovies", "desc": "مشاهدة أحدث الأفلام مجاناً.", "cat": "Movies", "link": "https://fmovies.to", "price": "Free"},
    {"name": "Shahid", "desc": "أكبر منصة للمحتوى العربي.", "cat": "Movies", "link": "https://shahid.mbc.net", "price": "Freemium"},
    # ألعاب
    {"name": "FitGirl Repacks", "desc": "أشهر موقع للألعاب المضغوطة.", "cat": "Games", "link": "https://fitgirl-repacks.site", "price": "Free"},
    {"name": "Steam", "desc": "متجر الألعاب الأكبر عالمياً.", "cat": "Games", "link": "https://steampowered.com", "price": "Freemium"},
    # عمل حر
    {"name": "Upwork", "desc": "أكبر منصة للعمل الحر عالمياً.", "cat": "Freelance", "link": "https://upwork.com", "price": "Free"},
    {"name": "Fiverr", "desc": "بيع وشراء الخدمات المصغرة.", "cat": "Freelance", "link": "https://fiverr.com", "price": "Free"}
]

cat_icons = {
    "AI Partner": "🤖", "Movies": "🎬", "Games": "🎮", "Freelance": "💰"
}

@app.route('/')
def index():
    current_cat = request.args.get('category', 'AI Partner')
    search_query = request.args.get('search', '').lower()
    categories = sorted(list(set(item['cat'] for item in database)))

    if search_query:
        results = [i for i in database if search_query in i['name'].lower() or search_query in i['cat'].lower()]
    else:
        results = [i for i in database if i['cat'] == current_cat]

    return render_template('index.html', items=results, categories=categories, 
                           current_cat=current_cat, icons=cat_icons)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
