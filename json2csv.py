import json
import csv

# JSONデータをPythonの辞書に変換
data = """
{
  "kind": "youtube#videoListResponse",
  "etag": "QoKbWhQs4ZT3BO36B8Jrx67wBNc",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "EvaF9sgcGeiNX4JbWqv5reFFA6c",
      "id": "75JPzYvOf1s",
      "snippet": {
        "publishedAt": "2024-05-09T06:57:19Z",
        "channelId": "UCJHAT3Uvv-g3I8H3GhHWV7w",
        "title": "The May 8, 2024 Severe Weather Outbreak, As It Happened...",
        "description": "Description text here with proper escaping.",
        "channelTitle": "Channel Name",
        "categoryId": "10",
        "thumbnails": {
          "high": {
            "url": "https://example.com/high.jpg"
          }
        }
      },
      "statistics": {
        "viewCount": "1000",
        "likeCount": "100",
        "favoriteCount": "50",
        "commentCount": "30"
      }
    }
  ]
}
"""

json_data = json.loads(data)

# CSVファイルを開く
with open('youtube_videos.csv', 'w', newline='', encoding='utf-8') as file:
    # CSVライターオブジェクトを作成
    writer = csv.writer(file)
    
    # ヘッダーを書き込む
    headers = [
        'Video ID', 'Published At', 'Channel ID', 'Title', 'Description', 
        'Thumbnail URL', 'Channel Title', 'Category ID', 'View Count', 
        'Like Count', 'Favorite Count', 'Comment Count'
    ]
    writer.writerow(headers)
    
    # 各ビデオの情報を書き込む
    for item in json_data['items']:
        video_id = item['id']
        published_at = item['snippet']['publishedAt']
        channel_id = item['snippet']['channelId']
        title = item['snippet']['title']
        description = item['snippet']['description']
        thumbnail_url = item['snippet']['thumbnails']['high']['url']
        channel_title = item['snippet']['channelTitle']
        category_id = item['snippet']['categoryId']
        view_count = item['statistics']['viewCount']
        like_count = item['statistics']['likeCount']
        favorite_count = item['statistics']['favoriteCount']
        comment_count = item['statistics']['commentCount']
        
        # CSVファイルに書き込む
        writer.writerow([
            video_id, published_at, channel_id, title, description, thumbnail_url, 
            channel_title, category_id, view_count, like_count, favorite_count, comment_count
        ])

print("CSVファイルが作成されました。")
