# TinyHome

A minimal, modern dashboard generator. Two files, no dependencies, beautiful output.

Inspired by [bderenzo/tinyhome](https://github.com/bderenzo/tinyhome) — a brilliant shell-based static homepage generator. This Python rewrite adds a modern UI, dark mode toggle, and simplified INI configuration while keeping the same spirit of simplicity.

Perfect for homelabs, internal intranets, self-hosted dashboards, or anywhere you need a clean landing page for your links.

![Dark mode](https://img.shields.io/badge/dark%20mode-supported-blue)
![Python 3](https://img.shields.io/badge/python-3.x-green)
![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)

## Features

- **Single Python script** — no frameworks, no build tools
- **INI config file** — cleaner than CSV, easy to read and edit
- **Dark/light mode** — toggle button + respects system preference
- **Auto-sorted sections** — items alphabetized automatically
- **Responsive grid** — works on desktop and mobile
- **Modern UI** — gradient borders, glow effects, smooth animations
- **Font Awesome 6** — full icon library via CDN
- **Zero local assets** — fonts and icons load from CDN

## Quick Start

```bash
# Generate the dashboard
./tinyhome.py > index.html

# Or specify a different config
./tinyhome.py myconfig.ini > index.html
```

Open `index.html` in your browser. That's it.

![darkmode](images/darkmode.jpg)
![lightmode](images/lightmode.jpg)

## Configuration

Edit `config.ini` to customize your dashboard:

```ini
[settings]
title = My Dashboard

[Development]
icon = code
GitHub = fab github, https://github.com
GitLab = fab gitlab, https://gitlab.com
Stack Overflow = fab stack-overflow, https://stackoverflow.com

[Tools]
icon = toolbox
Claude = message, https://claude.ai
Notion = note-sticky, https://notion.so
```

### Config format

```
[Section Name]
icon = section-icon
Link Name = icon-name, https://example.com
```

### Icons

Icons use [Font Awesome 6](https://fontawesome.com/icons). Two types:

| Type | Prefix | Example |
|------|--------|---------|
| Solid (default) | none | `server`, `code`, `toolbox` |
| Brands | `fab` | `fab github`, `fab youtube` |

Browse available icons at [fontawesome.com/icons](https://fontawesome.com/icons)

## Example config.ini

```ini
[settings]
title = My Dashboard

[Search]
icon = magnifying-glass
Google = fab google, https://www.google.com
DuckDuckGo = magnifying-glass, https://duckduckgo.com

[Development]
icon = code
GitHub = fab github, https://github.com
GitLab = fab gitlab, https://gitlab.com
Stack Overflow = fab stack-overflow, https://stackoverflow.com
MDN Web Docs = book, https://developer.mozilla.org

[Tools]
icon = toolbox
ChatGPT = comment-dots, https://chat.openai.com
Claude = message, https://claude.ai
Notion = note-sticky, https://notion.so
Trello = fab trello, https://trello.com

[Social]
icon = users
Reddit = fab reddit, https://reddit.com
Twitter = fab x-twitter, https://twitter.com
LinkedIn = fab linkedin, https://linkedin.com

[Media]
icon = play
YouTube = fab youtube, https://youtube.com
Spotify = fab spotify, https://spotify.com
Twitch = fab twitch, https://twitch.tv
```

## Requirements

- Python 3.x (standard library only)
- Internet connection (for CDN fonts/icons)

## Files

```
tinyhome/
├── tinyhome.py    # Dashboard generator
├── config.ini     # Your links and settings
├── index.html     # Generated output
└── README.md
```

## Why a rewrite?

The original [bderenzo/tinyhome](https://github.com/bderenzo/tinyhome) is a fantastic minimal solution using pure shell. This Python reimplementation trades shell portability for:

- **Faster generation** — Python vs subshell overhead
- **INI config** — no more `END` markers or CSV quirks
- **Modern styling** — gradient borders, glassmorphism options, animations
- **Dark mode toggle** — click to switch, remembers preference
- **CDN-only assets** — no local css/webfonts folders needed

If you want maximum portability with zero dependencies, use the original. If you want a prettier output with Python available, use this one.

## Credits

- Original concept: [bderenzo/tinyhome](https://github.com/bderenzo/tinyhome)
- Icons: [Font Awesome](https://fontawesome.com)
- Font: [Inter](https://fonts.google.com/specimen/Inter)

