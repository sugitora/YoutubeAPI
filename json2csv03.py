import os
import csv
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # CSVファイルを開く
    with open('youtube_videos.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Video ID", "Published At", "Channel ID", "Title", "Description",
            "Thumbnail URL", "Channel Title", "Category ID", "View Count",
            "Like Count", "Favorite Count", "Comment Count"
        ])

        # ページトークンを管理
        nextPageToken = None
        while True:
            request = youtube.videos().list(
                part="snippet,statistics",
                chart="mostPopular",
                regionCode="jp",
                maxResults=50,  # 最大50件のデータを取得
                pageToken=nextPageToken
            )
            response = request.execute()

            # JSONからデータを抽出し、CSVに書き込む
            for item in response.get('items', []):
                writer.writerow([
                    item['id'],
                    item['snippet']['publishedAt'],
                    item['snippet']['channelId'],
                    item['snippet']['title'],
                    item['snippet']['description'],
                    item['snippet']['thumbnails']['high']['url'],
                    item['snippet']['channelTitle'],
                    item['snippet']['categoryId'],
                    item.get('statistics', {}).get('viewCount', 'N/A'),
                    item.get('statistics', {}).get('likeCount', 'N/A'),
                    item.get('statistics', {}).get('favoriteCount', 'N/A'),
                    item.get('statistics', {}).get('commentCount', 'N/A')
                ])

            # 次のページがあるかチェック
            nextPageToken = response.get('nextPageToken')
            if not nextPageToken:
                break

    print("CSVファイルが作成されました。")

if __name__ == "__main__":
    main()
