#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["pelican-yaml-metadata"]

AUTHOR = 'UndecV'
SITENAME = 'キャンディージャー'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    # 'extra/custom.css': {'path': 'custom.css'},
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/LICENSE': {'path': 'LICENSE'},
    # 'extra/README': {'path': 'README'},
}

TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'en'

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# LINKS = (
#   ('Pelican', 'http://getpelican.com/'),
#   ('Python.org', 'http://python.org/'),
#   ('Jinja2', 'http://jinja.pocoo.org/'),
#   ('You can modify those links in your config file', '#'),
#   )

FRIEND_LINKS = (
  ('通訊雜記', 'https://wenyuangg.github.io/'),
)

SOCIAL = (
    ('github', 'https://github.com/undecv'),
    ('twitter', 'https://twitter.com/phinhdgxiaohai'),
    ('telegram', 'https://t.me/s/poi0048'),
    ('rss','/feeds/all.atom.xml')
)
# ('envelope-o',''),
# ('facebook',''),
# ('github', ''),
# ('gitlab',''),
# ('github-alt',''),
# ('google',''),
# ('linkedin',''),
# ('pinterest',''),
# ('reddit',''),
# ('rss','feeds/all.atom.xml'),
# ('stack-overflow',''),
# ('soundcloud',''),
# ('twitter', ''),
# ('youtube',''),
# ('xing','')

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "./themes/Flex"
# Ref: 
#   https://github.com/alexandrevicenzi/Flex
#   https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example
#   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

SITETITLE = 'キャンディージャー'
SITESUBTITLE = 'Candy jar'
SITELOGO = '/images/128.png'
# SITEDESCRIPTION = ""
# FAVICON = '/images/favicon.ico'

PYGMENTS_STYLE = 'emacs'
# http://pygments.org/demo/3738752/?style=emacs

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

COPYRIGHT_NAME = SITETITLE
COPYRIGHT_YEAR = 2019
# CC_LICENSE = {
#     'name': 'Creative Commons Attribution-ShareAlike',
#     'version': '4.0',
#     'slug': 'by-sa'
# }

# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }
# CUSTOM_CSS = 'theme/custom.css'

MAIN_MENU = True

# ADD_THIS_ID = 'ra-77hh6723hhjd'
# DISQUS_SITENAME = 'yoursite'
# GOOGLE_ANALYTICS = 'UA-1234-5678'
# GOOGLE_TAG_MANAGER = 'GTM-ABCDEF'
# STATUSCAKE = { 'trackid': 'your-id', 'days': 7, 'design': 6, 'rumid': 1234 }
