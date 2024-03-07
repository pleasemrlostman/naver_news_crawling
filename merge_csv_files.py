import pandas as pd
def merge_csv_files(files, output_filename):
    all_dfs = []
    for file in files:
        df = pd.read_csv(file)
        all_dfs.append(df)

    merged_df = pd.concat(all_dfs, ignore_index=True)

    # 중복된 title 제거
    merged_df.drop_duplicates(subset='title', keep='first', inplace=True)

    # 'pubDate' 열을 기준으로 최신순으로 정렬
    merged_df.sort_values(by='pubDate', ascending=False, inplace=True)

    # 'pubDate' 열의 날짜 형식 변경
    merged_df['pubDate'] = pd.to_datetime(merged_df['pubDate']).dt.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')

    merged_df.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print("Merged data has been saved to", output_filename)