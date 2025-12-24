from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة البيانات المليونية - (Success-Ready Database)
database = [
    # --- AI PARTNER (مهامي) ---
    {"name": "Gemini AI", "desc": "Google's smart assistant for coding & life.", "cat": "AI Partner", "link": "https://gemini.google.com", "price": "Free"},
    {"name": "ChatGPT", "desc": "OpenAI's powerful text model.", "cat": "AI Partner", "link": "https://chat.openai.com", "price": "Freemium"},
    {"name": "Claude AI", "desc": "Advanced reasoning and coding assistant.", "cat": "AI Partner", "link": "https://claude.ai", "price": "Freemium"},
    {"name": "Perplexity", "desc": "AI search engine with citations.", "cat": "AI Partner", "link": "https://perplexity.ai", "price": "Free"},
    {"name": "Poe", "desc": "Multi-model AI platform.", "cat": "AI Partner", "link": "https://poe.com", "price": "Freemium"},

    # --- MOVIES & SERIES (ترفيه) ---
    {"name": "Netflix", "desc": "Global movies and originals.", "cat": "Movies", "link": "https://netflix.com", "price": "Paid"},
    {"name": "Fmovies", "desc": "Watch latest movies for free.", "cat": "Movies", "link": "https://fmovies.to", "price": "Free"},
    {"name": "Disney+", "desc": "Marvel, Star Wars, Pixar.", "cat": "Movies", "link": "https://disneyplus.com", "price": "Paid"},
    {"name": "Shahid", "desc": "Top Arabic content and series.", "cat": "Movies", "link": "https://shahid.net", "price": "Paid"},
    {"name": "SolarMovie", "desc": "Huge free movie database.", "cat": "Movies", "link": "https://solarmovie.to", "price": "Free"},
    {"name": "Prime Video", "desc": "Amazon's streaming service.", "cat": "Movies", "link": "https://amazon.com/video", "price": "Paid"},

    # --- GAMES (تحميل وشراء) ---
    {"name": "FitGirl Popular", "desc": "Popular compressed PC games.", "cat": "Games", "link": "https://fitgirl-repacks.site/popular-repacks/", "price": "Free"},
    {"name": "Steam", "desc": "Biggest PC gaming store.", "cat": "Games", "link": "https://store.steampowered.com", "price": "Paid"},
    {"name": "Epic Games", "desc": "Weekly free premium games.", "cat": "Games", "link": "https://epicgames.com", "price": "Free"},
    {"name": "DODI Repacks", "desc": "Alternative compressed games.", "cat": "Games", "link": "https://dodi-repacks.site", "price": "Free"},
    {"name": "Itch.io", "desc": "Best place for Indie games.", "cat": "Games", "link": "https://itch.io", "price": "Free"},

    # --- ANIME ---
    {"name": "Crunchyroll", "desc": "Official Anime destination.", "cat": "Anime", "link": "https://crunchyroll.com", "price": "Paid"},
    {"name": "9Anime", "desc": "Massive free anime streaming.", "cat": "Anime", "link": "https://9anime.to", "price": "Free"},
    {"name": "GogoAnime", "desc": "Fast anime updates.", "cat": "Anime", "link": "https://gogoanime.pe", "price": "Free"},
    {"name": "AniList", "desc": "Track and discover anime.", "cat": "Anime", "link": "https://anilist.co", "price": "Free"},
    {"name": "Zoro.to", "desc": "Quality free anime streaming.", "cat": "Anime", "link": "https://zoro.to", "price": "Free"},

    # --- FREELANCE & MONEY ---
    {"name": "Upwork", "desc": "World's top freelance market.", "cat": "Freelance", "link": "https://upwork.com", "price": "Paid"},
    {"name": "Fiverr", "desc": "Micro-services for $5+.", "cat": "Freelance", "link": "https://fiverr.com", "price": "Fees"},
    {"name": "Mostaql", "desc": "Arabic professional freelance.", "cat": "Freelance", "link": "https://mostaql.com", "price": "Free"},
    {"name": "Freelancer", "desc": "Competitive project bidding.", "cat": "Freelance", "link": "https://freelancer.com", "price": "Paid"},
    {"name": "Khamsat", "desc": "Arabic micro-services.", "cat": "Freelance", "link": "https://khamsat.com", "price": "Free"},

    # --- DESIGN & EDITING ---
    {"name": "Figma", "desc": "Best UI/UX design tool.", "cat": "Design", "link": "https://figma.com", "price": "Free"},
    {"name": "Canva", "desc": "Design for non-designers.", "cat": "Design", "link": "https://canva.com", "price": "Free"},
    {"name": "Midjourney", "desc": "Pro AI image generation.", "cat": "Design", "link": "https://midjourney.com", "price": "Paid"},
    {"name": "Adobe Firefly", "desc": "AI integrated in Photoshop.", "cat": "Design", "link": "https://adobe.com/firefly", "price": "Paid"},
    {"name": "CapCut", "desc": "Easy AI video editing.", "cat": "Design", "link": "https://capcut.com", "price": "Free"},

    # --- EDUCATION & LANGUAGES ---
    {"name": "Udemy", "desc": "Diverse online courses.", "cat": "Education", "link": "https://udemy.com", "price": "Paid"},
    {"name": "Coursera", "desc": "University certifications.", "cat": "Education", "link": "https://coursera.org", "price": "Freemium"},
    {"name": "Duolingo", "desc": "Language learning fun.", "cat": "Education", "link": "https://duolingo.com", "price": "Free"},
    {"name": "Khan Academy", "desc": "Free world-class learning.", "cat": "Education", "link": "https://khanacademy.org", "price": "Free"},
    {"name": "DeepL", "desc": "Accurate AI translator.", "cat": "Education", "link": "https://deepl.com", "price": "Free"},

    # --- CYBERSECURITY & PRIVACY ---
    {"name": "NordVPN", "desc": "Top online protection.", "cat": "Security", "link": "https://nordvpn.com", "price": "Paid"},
    {"name": "Bitwarden", "desc": "Safe password storage.", "cat": "Security", "link": "https://bitwarden.com", "price": "Free"},
    {"name": "Have I Been Pwned", "desc": "Check for data leaks.", "cat": "Security", "link": "https://haveibeenpwned.com", "price": "Free"},
    {"name": "ProtonMail", "desc": "Encrypted secure email.", "cat": "Security", "link": "https://proton.me", "price": "Free"},
    {"name": "VirusTotal", "desc": "Scan files for viruses.", "cat": "Security", "link": "https://virustotal.com", "price": "Free"},

    # --- SPORTS (بث مباشر ومتابعة) ---
    {"name": "Yalla Shoot", "desc": "Matches & live results.", "cat": "Sports", "link": "https://yalla-shoot.com", "price": "Free"},
    {"name": "BeIN Connect", "desc": "Official live streaming.", "cat": "Sports", "link": "https://connect.bein.com", "price": "Paid"},
    {"name": "FlashScore", "desc": "Fastest live score updates.", "cat": "Sports", "link": "https://flashscore.com", "price": "Free"},
    {"name": "Kooora", "desc": "The Arabic sports source.", "cat": "Sports", "link": "https://kooora.com", "price": "Free"},
    {"name": "LiveSoccerTV", "desc": "Global match schedules.", "cat": "Sports", "link": "https://livesoccertv.com", "price": "Free"}
]

# الأيقونات
cat_icons = {
    "AI Partner": "🤖", "Movies": "🎬", "Games": "🎮", "Anime": "⛩️",
    "Freelance": "💰", "Design": "🎨", "Education": "📚", "Security": "🛡️", "Sports": "⚽"
}

@app.route('/')
def index():
    current_cat = request.args.get('category')
    search_query = request.args.get('search', '').lower()
    categories = sorted(list(set(item['cat'] for item in database)))
    
    if not current_cat: current_cat = "Movies"

    results = []
    if search_query:
        # البحث الذكي: إذا كتب 3 أحرف فأكثر تطابق اسم القسم
        matching_cats = [c for c in categories if len(search_query) >= 3 and search_query in c.lower()]
        if matching_cats:
            results = [i for i in database if i['cat'] in matching_cats]
        else:
            results = [i for i in database if search_query in i['name'].lower() or search_query in i['desc'].lower()]
    else:
        results = [i for i in database if i['cat'] == current_cat]
    
    return render_template('index.html', items=results, categories=categories, current_cat=current_cat, search_query=search_query, icons=cat_icons)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
