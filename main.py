# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.insert
# NOTES:
# 1. This sample code uploads a file and can't be executed via this interface.
#    To test this code, you must run it locally using your own API credentials.
#    See: https://developers.google.com/explorer-help/code-samples#python
# 2. This example makes a simple upload request. We recommend that you consider
#    using resumable uploads instead, particularly if you are transferring large
#    files or there's a high likelihood of a network interruption or other
#    transmission failure. To learn more about resumable uploads, see:
#    https://developers.google.com/api-client-library/python/guide/media_upload

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
# import json

# def load_credentials(filename):
#     try:
#         with open(filename, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         print("認証情報ファイルが見つかりません。")
#         exit()
#     except json.JSONDecodeError:
#         print("認証情報ファイルの形式が正しくありません。")
#         exit()

# credentials = load_credentials('credentials.json')
# CLIENT_ID = credentials['client_id']
scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json" # 修正(ダウンロードしたJSONファイル名)

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server() # 修正(「flow.run_console()」から「flow.run_local_server()」)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status", # 追記
        body={
            ### 追記(ここから) ###
            "snippet": {
                "channelId": "", # 動画を投稿するチャンネルIDを記載
                "title": "タイトルのテスト", # 動画のタイトルを設定
                "description": "説明のテストです。", # 動画の説明を追加
                "tags": ["Tag 1", "Tag 2", "Tag 3"], # タグを追加
                "categoryId": "19", # "19"は「旅行とイベント」のカテゴリ。
                "defaultLanguage": "ja_JP", # タイトルと説明の言語
                "defaultAudioLanguage": "ja_JP", # 動画の言語
            },
            "status": {
                "uploadStatus": "uploaded", # アップロードされたビデオのステータス
                "privacyStatus": "private", # 公開設定は「非公開」
                "license": "youtube", # 標準のYouTubeライセンス
                "embeddable": "true", # 動画の埋め込みを許可する
                "madeForKids": False  # 子ども向けではないと指定
            },
            ### 追記(ここまで) ###
        },
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("test.mp4") # 修正(動画ファイルのパスを記載)
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
