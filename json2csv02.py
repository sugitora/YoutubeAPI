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
    client_secrets_file = "credentials.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode="jp"
    )
    response = request.execute()

    # CSVファイルを開く
    with open('youtube_videos.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # ヘッダーを書き込む
        writer.writerow([
            "Video ID", "Published At", "Channel ID", "Title", "Description",
            "Thumbnail URL", "Channel Title", "Category ID", "View Count",
            "Like Count", "Favorite Count", "Comment Count"
        ])

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

    print("CSVファイルが作成されました。")

if __name__ == "__main__":
    main()
