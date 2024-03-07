import json
import pandas as pd
from remove_html_tags import remove_html_tags
def parse_naver_news_response(response):
    news_data = json.loads(response)
    df = pd.DataFrame(news_data['items'])
    # 'pubDate' 열을 datetime 형식으로 변환
    df['pubDate'] = pd.to_datetime(df['pubDate'])
    # HTML 태그 제거
    df['title'] = df['title'].apply(remove_html_tags)
    df['description'] = df['description'].apply(remove_html_tags)  # description 열에서도 HTML 태그 제거

    return df


