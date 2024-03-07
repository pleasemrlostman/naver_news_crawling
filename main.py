
import pandas as pd
from naver_news_functions import *
from save_to_csv import save_to_csv
from merge_csv_files import merge_csv_files
from parse_naver_news_response import parse_naver_news_response
from get_naver_api_credentials import get_naver_api_credentials


def main():
    client_id, client_secret = get_naver_api_credentials()

    keywords = [
        "수변감성", "악취", "하수", "물순환", "물재생센터", "물재생시설공단", "수질", "청계천",
        "하천", "지천", "호우", "빗물펌프장", "도림천", "홍제천", "수방", "배수", "유수지",
        "저류", "신곡수중보", "슬러지", "용산미군기지", "빗물", "한강", "태풍", "토양",
        "싱크홀", "도시안전건설위원회", "서운로", "토양오염", "땅꺼짐", "홍수", "빗물터널",
        "반지하", "빗물받이", "끈벌레", "하수도", "침수", "지하수", "수변활력", "치수",
        "대심도", "물순환안전국"
    ]

    csv_files = []

    user_input = input(f"(Y/N): 오늘 날짜의 기사만 받으시겠습니까? ")

    if user_input.upper() == 'Y':
        for keyword in keywords:
            query_with_seoul = keyword + " 서울"
            response = search_naver_news(query_with_seoul, client_id, client_secret)
            if response:
                df = parse_naver_news_response(response)
                if not df.empty:
                    today = pd.Timestamp.now(tz='Asia/Seoul').floor('D')  # 오늘의 날짜를 가져와서 시간을 00:00:00으로 설정
                    # 오늘 이후의 행만 필터링
                    df = df[df['pubDate'] >= today]
                    filename = f"naver_news_results_{keyword}.csv"
                    save_to_csv(df, filename)
                    csv_files.append(filename)
                else:
                    print(f"No results found for the given query '{keyword}' with '서울'.")
            else:
                print(f"Failed to retrieve data from Naver API for the query '{keyword}'.")

        merge_csv_files(csv_files, "merged_naver_news_results.csv")
    elif user_input.upper() == 'N':
        days_ago_input = int(input("며칠 이전의 기사를 받으시겠습니까? "))
        for keyword in keywords:
            query_with_seoul = keyword + " 서울"
            response = search_naver_news(query_with_seoul, client_id, client_secret)
            if response:
                df = parse_naver_news_response(response)
                if not df.empty:
                    today = pd.Timestamp.now(tz='Asia/Seoul')  # 오늘의 날짜를 가져옴
                    three_days_ago = today - pd.Timedelta(days=days_ago_input)  # 3일 이전의 날짜를 계산
                    # 3일 이전 이후의 행만 필터링
                    df = df[df['pubDate'] >= three_days_ago]
                    filename = f"naver_news_results_{keyword}.csv"
                    save_to_csv(df, filename)
                    csv_files.append(filename)
                else:
                    print(f"No results found for the given query '{keyword}' with '서울'.")
            else:
                print(f"Failed to retrieve data from Naver API for the query '{keyword}'.")

        merge_csv_files(csv_files, "merged_naver_news_results.csv")


if __name__ == "__main__":
    main()