def save_to_csv(df, filename):
    df.to_csv(filename, index=False, encoding='utf-8-sig')  # UTF-8 with BOM
    print("Data has been saved to", filename)
