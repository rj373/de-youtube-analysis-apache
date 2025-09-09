# -*- coding: utf-8 -*-

# This script fetches ALL YouTube comments for a given video,
# processes the data, and saves it to a CSV file.

import os
import googleapiclient.discovery
import pandas as pd
import pendulum

def run_etl_workflow():
    """
    Main function to run the entire YouTube ETL process.
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    
    # ⚠️ Important: Replace "YOUR_API_KEY" with your actual API key
    DEVELOPER_KEY = "YOUTUBE_API_KEY"
    
    video_id = "ADD_VIDEO_ID"

    # Build the YouTube API service object
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    
    all_comments_data = []
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id
    )

    # Use a while loop to handle pagination
    while request:
        response = request.execute()
        
        for item in response.get('items', []):
            top_comment = item['snippet']['topLevelComment']['snippet']
            top_comment['totalReplyCount'] = item['snippet']['totalReplyCount']
            all_comments_data.append(top_comment)
            
            if 'replies' in item and 'comments' in item['replies']:
                for reply in item['replies']['comments']:
                    reply_data = reply['snippet']
                    reply_data['totalReplyCount'] = item['snippet']['totalReplyCount']
                    all_comments_data.append(reply_data)
        
        request = youtube.commentThreads().list_next(request, response)
        
    df = pd.DataFrame(all_comments_data)
    
    # Clean and select the useful columns
    df['textOriginal'] = df['textOriginal'].str.replace('\n', ' ', regex=True).str.replace('\r', ' ', regex=True)
    df = df[[
        'textOriginal',
        'authorDisplayName',
        'likeCount',
        'publishedAt',
        'totalReplyCount'
    ]]
    
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    
    # Save the DataFrame to a CSV file in S3
    df.to_csv("s3://S3_BUCKET_INFO/youtube_comments.csv", index=False)
    
    return "ETL process completed and data saved to S3."
