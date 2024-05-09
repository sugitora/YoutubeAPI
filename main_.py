import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "タイトルのテスト",
                "description": "説明のテストです。",
                "tags": ["Tag 1", "Tag 2", "Tag 3"],
                "categoryId": "19",
                "defaultLanguage": "ja_JP",
                "defaultAudioLanguage": "ja_JP"
            },
            "status": {
                "uploadStatus": "uploaded",
                "privacyStatus": "private",
                "license": "youtube",
                "embeddable": True,
                "madeForKids": False  # 子ども向けではないと指定
            }
        },
        media_body=MediaFileUpload("test.mp4")
    )
    response = request.execute()
    print(response)

if __name__ == "__main__":
    main()
