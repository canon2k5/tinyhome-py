#!/usr/bin/env python3
import configparser
import sys

CSS = '''
* { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg: #f5f7fa;
    --card-bg: #ffffff;
    --card-border: rgba(0, 0, 0, 0.08);
    --text: #1a1a2e;
    --text-muted: #64748b;
    --accent: #3b82f6;
    --accent-secondary: #8b5cf6;
    --shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
    --card-hover: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
}

[data-theme="dark"] {
    --bg: #0f172a;
    --card-bg: #1e293b;
    --card-border: rgba(148, 163, 184, 0.1);
    --text: #f1f5f9;
    --text-muted: #94a3b8;
    --accent: #60a5fa;
    --accent-secondary: #a78bfa;
    --shadow: 0 4px 6px -1px rgba(0,0,0,0.4);
    --card-hover: 0 20px 25px -5px rgba(0,0,0,0.4);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    transition: background 0.3s, color 0.3s;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--text-muted);
}

h1 {
    font-size: 1.75rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.theme-toggle {
    background: var(--card-bg);
    border: none;
    padding: 0.75rem;
    border-radius: 50%;
    cursor: pointer;
    box-shadow: var(--shadow);
    transition: transform 0.2s, box-shadow 0.2s;
    color: var(--text);
    font-size: 1.25rem;
}

.theme-toggle:hover {
    transform: scale(1.1);
    box-shadow: var(--card-hover);
}

section {
    margin-bottom: 2rem;
}

h2 {
    font-size: 1rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-muted);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

h2 i { color: var(--accent); }

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
}

.card {
    position: relative;
    background: var(--card-bg);
    padding: 1.25rem;
    border-radius: 16px;
    text-decoration: none;
    color: var(--text);
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    z-index: 1;
}

.card::before {
    content: '';
    position: absolute;
    inset: -2px;
    border-radius: 18px;
    background: linear-gradient(135deg, var(--accent), var(--accent-secondary), var(--accent));
    background-size: 200% 200%;
    opacity: 0;
    z-index: -1;
    transition: opacity 0.3s ease, background-position 0.5s ease;
}

.card::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 16px;
    background: var(--card-bg);
    z-index: -1;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 40px -10px var(--accent);
}

.card:hover::before {
    opacity: 1;
    animation: gradient-shift 2s ease infinite;
}

@keyframes gradient-shift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.card i, .card span {
    position: relative;
    z-index: 1;
}

.card i {
    font-size: 1.25rem;
    color: var(--accent);
}

.card span {
    font-weight: 500;
}

@media (max-width: 600px) {
    .cards { grid-template-columns: 1fr; }
    h1 { font-size: 1.4rem; }
}
'''

JS = '''
function toggleTheme() {
    const html = document.documentElement;
    const current = html.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateIcon(next);
}

function updateIcon(theme) {
    const btn = document.querySelector('.theme-toggle i');
    btn.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
}

(function() {
    const saved = localStorage.getItem('theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', saved);
    document.addEventListener('DOMContentLoaded', () => updateIcon(saved));
})();
'''

def get_icon_class(icon_value):
    parts = icon_value.split()
    if len(parts) == 2:
        return f'{parts[0]} fa-{parts[1]}'
    return f'fas fa-{parts[0]}'

def parse_config(configfile):
    config = configparser.ConfigParser()
    config.read(configfile)
    
    title = config.get('settings', 'title', fallback='Dashboard')
    
    sections = []
    for section_name in config.sections():
        if section_name == 'settings':
            continue
        
        section_icon = config.get(section_name, 'icon', fallback='folder')
        items = []
        
        for key, value in config.items(section_name):
            if key == 'icon':
                continue
            parts = [p.strip() for p in value.split(',', 1)]
            icon = parts[0] if parts else 'link'
            url = parts[1] if len(parts) > 1 else '#'
            items.append({'name': key, 'icon': icon, 'url': url})
        
        items.sort(key=lambda x: x['name'].lower())
        sections.append({'name': section_name, 'icon': section_icon, 'items': items})
    
    return title, sections

def main():
    configfile = sys.argv[1] if len(sys.argv) > 1 else 'config.ini'
    title, sections = parse_config(configfile)

    print(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
    <style>{CSS}</style>
    <script>{JS}</script>
</head>
<body>
<div class="container">
<header>
    <h1>{title}</h1>
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme">
        <i class="fas fa-moon"></i>
    </button>
</header>''')

    for section in sections:
        print(f'''<section>
<h2><i class="{get_icon_class(section['icon'])}"></i>{section['name']}</h2>
<div class="cards">''')
        for item in section['items']:
            print(f'<a class="card" href="{item["url"]}"><i class="{get_icon_class(item["icon"])}"></i><span>{item["name"]}</span></a>')
        print('</div></section>')

    print('''</div>
</body>
</html>''')

if __name__ == '__main__':
    main()
