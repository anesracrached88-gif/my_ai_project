from flask import Flask, render_template, request
import os

app = Flask(__name__)

# قاعدة البيانات الكاملة مع الروابط الأصلية
database = [
    # --- AI PARTNER ---
    {"name": "Gemini AI", "desc": "Google's smart assistant for coding & life.", "cat": "AI Partner", "link": "https://gemini.google.com", "price": "Free"},
    {"name": "ChatGPT", "desc": "OpenAI's powerful text model.", "cat": "AI Partner", "link": "https://chat.openai.com", "price": "Freemium"},
    {"name": "Claude AI", "desc": "Advanced reasoning and coding assistant.", "cat": "AI Partner", "link": "https://claude.ai", "price": "Freemium"},
    {"name": "Perplexity", "desc": "AI search engine with citations.", "cat": "AI Partner", "link": "https://perplexity.ai", "price": "Free"},
    {"name": "Poe", "desc": "Multi-model AI platform.", "cat": "AI Partner", "link": "https://poe.com", "price": "Free"},

    # --- MOVIES & SERIES ---
    {"name": "Netflix", "desc": "Global movies and originals.", "cat": "Movies", "link": "https://netflix.com", "price": "Paid"},
    {"name": "Fmovies", "desc": "Watch latest movies for free.", "cat": "Movies", "link": "https://fmovies.to", "price": "Free"},
    {"name": "Disney+", "desc": "Marvel, Star Wars, Pixar.", "cat": "Movies", "link": "https://disneyplus.com", "price": "Paid"},
    {"name": "Shahid", "desc": "Top Arabic content and originals.", "cat": "Movies", "link": "https://shahid.mbc.net", "price": "Freemium"},
    {"name": "SolarMovie", "desc": "Huge free movie database.", "cat": "Movies", "link": "https://solarmovie.pe", "price": "Free"},

    # --- GAMES ---
    {"name": "FitGirl Popular", "desc": "Popular compressed PC games.", "cat": "Games", "link": "https://fitgirl-repacks.site", "price": "Free"},
    {"name": "Steam", "desc": "Biggest PC gaming store.", "cat": "Games", "link": "https://steampowered.com", "price": "Freemium"},
    {"name": "Epic Games", "desc": "Weekly free premium games.", "cat": "Games", "link": "https://epicgames.com", "price": "Freemium"},
    {"name": "DODI Repacks", "desc": "Alternative compressed games.", "cat": "Games", "link": "https://dodi-repacks.site", "price": "Free"},
    
    # --- FREELANCE & MONEY ---
    {"name": "Upwork", "desc": "World's top freelance marketplace.", "cat": "Freelance", "link": "https://upwork.com", "price": "Free"},
    {"name": "Fiverr", "desc": "Micro-services for $5+.", "cat": "Freelance", "link": "https://fiverr.com", "price": "Free"}
]

# الأيقونات
cat_icons = {
    "AI Partner": "🤖", "Movies": "🎬", "Games": "🎮", 
    "Freelance": "💰", "Design": "🎨", "Education": "📚",
    "Cybersecurity": "🛡️", "Sports": "⚽", "Anime": "⛩️"
}

@app.route('/')
def index():
    current_cat = request.args.get('category', 'Movies')
    search_query = request.args.get('search', '').lower()
    
    # استخراج التصنيفات الفريدة
    categories = sorted(list(set(item['cat'] for item in database)))

    # تصفية النتائج
    if search_query:
        results = [i for i in database if search_query in i['name'].lower() or search_query in i['cat'].lower()]
    else:
        results = [i for i in database if i['cat'] == current_cat]

    return render_template('index.html', items=results, categories=categories, 
                           current_cat=current_cat, icons=cat_icons)

if __name__ == '__main__':
    # إعدادات التشغيل لـ Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

