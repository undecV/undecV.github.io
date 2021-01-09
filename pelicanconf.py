#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime


AUTHOR = 'UndecV'
SITEURL = ''  # SITEURL = 'https://undecv.github.io'
SITENAME = 'キャンディージャー'
SITETITLE = 'キャンディージャー'
SITESUBTITLE = 'Candy jar'
SITEDESCRIPTION = "undecV's Blog"
SITELOGO = SITEURL + '/images/128.png'
FAVICON = SITEURL + '/favicon.ico'
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

THEME = "./themes/Flex-v2"  # https://github.com/alexandrevicenzi/Flex
PATH = 'content'
# OUTPUT_PATH = "blog/"
TIMEZONE = 'Asia/Taipei'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican-yaml-metadata"]

# # Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# # Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# # Default theme language.
# I18N_TEMPLATES_LANG = "en"
# # Translate to German.
DEFAULT_LANG = 'zh_TW'
OG_LOCALE = "zh_TW"
# LOCALE = "de_DE"
# ARTICLE_HIDE_TRANSLATION = False

# DATE_FORMATS = {
#     "en": "%B %d, %Y",
# }

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
# REL_CANONICAL = True
# DISABLE_URL_HASH = True
# PAGES_SORT_ATTRIBUTE = 'title'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

SOCIAL = (
    ('github', 'https://github.com/undecv'),
    ('twitter', 'https://twitter.com/phinhdgxiaohai'),
    ('telegram', 'https://t.me/s/poi0048'),
    ('rss', 'feeds/all.atom.xml'),
    # ('envelope-o',''),
    # ('facebook',''),
    # ('github-alt',''),
    # ('google',''),
    # ('linkedin',''),
    # ('pinterest',''),
    # ('reddit',''),
    # ('stack-overflow',''),
    # ('soundcloud',''),
    # ('youtube',''),
    # ('xing','')
)
# GITHUB_CORNER_URL = 'https://github.com/undecv'

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# LINKS = (
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
#     ('You can modify those links in your config file', '#'),
# )
# LINKS_IN_NEW_TAB = True

# FRIEND_LINKS = (
#   ('通訊雜記', 'https://wenyuangg.github.io/'),
# )

COPYRIGHT_NAME = SITETITLE
COPYRIGHT_YEAR = datetime.now().year
# CC_LICENSE = {
#     'name': 'Creative Commons Attribution-ShareAlike',
#     'version': '4.0',
#     'slug': 'by-sa'
# }

DEFAULT_PAGINATION = False

# # Integrations
# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'yoursite'
# DUOSHUO_SITENAME = 'yoursite'
# GOOGLE_ANALYTICS = 'UA-1234-5678'
# GUAGES= ''
# GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
# GOOGLE_GLOBAL_SITE_TAG = ''
# STATUSCAKE = 'F'
# PIWIK_SITE_ID = ''
# MATOMO_SITE_ID = ''
# PIWIK_URL = ''
# MATOMO_URL = ''
# ISSO_URL = '//comments.sumnerevans.com'
# ISSO_EMBED_JS_PATH = '/static/javascript/isso-dev.min.js'
# ISSO_OPTIONS = {
#     'avatar': 'false',
#     'gravatar': 'true',
#     'reply-to-self': 'true',
#     'reply-notifications': 'true',
# }

STATIC_PATHS = [
    'images',
    'extra/custom.css',
    'extra/favicon.ico',
    # 'extra',
]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'theme/custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/CNAME': {'path': 'CNAME'},
#     'extra/LICENSE': {'path': 'LICENSE'},
#     'extra/README': {'path': 'README'},
}

CUSTOM_CSS = "theme/custom.css"

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'


# ===== DEV Options ===========================================================

# USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
