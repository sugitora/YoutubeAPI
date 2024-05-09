# -*- coding: utf-8 -*-

# Sample Python code for youtube.thumbnails.set
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

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

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

    request = youtube.thumbnails().set(
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("test.jpg"), # 修正(サムネイル画像のパス)
        videoId="b6XDYFW_iR4" # 追記(動画のIDを指定)
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()
