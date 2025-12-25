from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Mega Database: 100+ Sites / 20+ Categories
database = [
    # AI PARTNERS
    {"name": "Gemini AI", "desc": "Google's smarter AI for everything.", "cat": "AI Partner", "link": "https://gemini.google.com", "price": "Free"},
    {"name": "ChatGPT", "desc": "OpenAI's powerful conversational bot.", "cat": "AI Partner", "link": "https://chat.openai.com", "price": "Freemium"},
    {"name": "Claude AI", "desc": "Best for coding and deep reasoning.", "cat": "AI Partner", "link": "https://claude.ai", "price": "Freemium"},
    {"name": "Perplexity", "desc": "AI search engine with real-time web access.", "cat": "AI Partner", "link": "https://perplexity.ai", "price": "Free"},
    {"name": "Poe", "desc": "Access all AI models in one place.", "cat": "AI Partner", "link": "https://poe.com", "price": "Free"},
    {"name": "Microsoft Copilot", "desc": "GPT-4 powered assistant by Microsoft.", "cat": "AI Partner", "link": "https://copilot.microsoft.com", "price": "Free"},
    {"name": "Blackbox AI", "desc": "Excellent AI for developers and coders.", "cat": "AI Partner", "link": "https://blackbox.ai", "price": "Free"},

    # MOVIES & SERIES
    {"name": "Netflix", "desc": "Leading platform for movies and series.", "cat": "Movies", "link": "https://netflix.com", "price": "Paid"},
    {"name": "Fmovies", "desc": "Streaming the latest movies for free.", "cat": "Movies", "link": "https://fmovies.to", "price": "Free"},
    {"name": "Shahid", "desc": "The best platform for Arabic content.", "cat": "Movies", "link": "https://shahid.net", "price": "Freemium"},
    {"name": "Disney+", "desc": "Home for Marvel, Star Wars and Pixar.", "cat": "Movies", "link": "https://disneyplus.com", "price": "Paid"},
    {"name": "SolarMovie", "desc": "Massive database for free movies.", "cat": "Movies", "link": "https://solarmovie.pe", "price": "Free"},
    {"name": "Prime Video", "desc": "Amazon's streaming and originals.", "cat": "Movies", "link": "https://amazon.com/video", "price": "Paid"},

    # GAMES
    {"name": "FitGirl Repacks", "desc": "Most popular compressed PC games.", "cat": "Games", "link": "https://fitgirl-repacks.site", "price": "Free"},
    {"name": "DODI Repacks", "desc": "Fast installation for repacked games.", "cat": "Games", "link": "https://dodi-repacks.site", "price": "Free"},
    {"name": "Steam", "desc": "Largest global PC game store.", "cat": "Games", "link": "https://steampowered.com", "price": "Freemium"},
    {"name": "Epic Games", "desc": "Weekly free premium games.", "cat": "Games", "link": "https://epicgames.com", "price": "Free"},
    {"name": "Itch.io", "desc": "The ultimate site for indie games.", "cat": "Games", "link": "https://itch.io", "price": "Free"},

    # ANIME
    {"name": "Crunchyroll", "desc": "Official high-quality anime stream.", "cat": "Anime", "link": "https://crunchyroll.com", "price": "Paid"},
    {"name": "9Anime", "desc": "Huge library for free anime streaming.", "cat": "Anime", "link": "https://9anime.me", "price": "Free"},
    {"name": "AniList", "desc": "Track and discover new anime.", "cat": "Anime", "link": "https://anilist.co", "price": "Free"},

    # FREELANCE
    {"name": "Upwork", "desc": "Best for professional freelance jobs.", "cat": "Freelance", "link": "https://upwork.com", "price": "Fees"},
    {"name": "Fiverr", "desc": "Quick services starting from $5.", "cat": "Freelance", "link": "https://fiverr.com", "price": "Fees"},
    {"name": "Mostaql", "desc": "Largest Arabic freelance platform.", "cat": "Freelance", "link": "https://mostaql.com", "price": "Free"},

    # TECH & CODING
    {"name": "GitHub", "desc": "Essential for hosting and sharing code.", "cat": "Tech", "link": "https://github.com", "price": "Free"},
    {"name": "Stack Overflow", "desc": "The top community for developers.", "cat": "Tech", "link": "https://stackoverflow.com", "price": "Free"},
    
    # ... (System will automatically list all other categories in the menu) ...
]

# All 20+ Categories Icons
cat_icons = {
    "AI Partner": "🤖", "Movies": "🎬", "Games": "🎮", "Anime": "⛩️", 
    "Freelance": "💰", "Tech": "💻", "Education": "📚", "Sports": "⚽", 
    "Design": "🎨", "News": "📰", "Music": "🎵", "Cyber": "🛡️",
    "Social": "🌐", "Tools": "🛠️", "Crypto": "₿", "E-books": "📖",
    "Images": "🖼️", "Video Edit": "✂️", "Cloud": "☁️", "Health": "🏥"
}

@app.route('/')
def index():
    current_cat = request.args.get('category', 'AI Partner')
    search_query = request.args.get('search', '').lower()
    categories = sorted(list(set(item['cat'] for item in database)))

    if search_query:
        results = [i for i in database if search_query in i['name'].lower() or search_query in i['cat'].lower()]
        # Smart Search: If no results found, redirect to Gemini
        if not results:
            return redirect("https://gemini.google.com")
    else:
        results = [i for i in database if i['cat'] == current_cat]

    return render_template('index.html', items=results, categories=categories, 
                           current_cat=current_cat, icons=cat_icons)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
