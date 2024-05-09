#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from apiclient.discovery import build

API_KEY = '<取得した API キーを入力します>'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
SEARCH_TEXT = '<検索したいチャンネル名>'

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)

response = youtube.search().list(q=SEARCH_TEXT, part='id,snippet', maxResults=25).execute()

for item in response.get('items', []):
    if item['id']['kind'] != 'youtube#channel':
        continue
    print('*' * 10)
    print(json.dumps(item, indent=2, ensure_ascii=False))
    print('*' * 10)