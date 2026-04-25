from omikuji import get_omikuji_results, draw_omikuji, format_omikuji_result

def main() -> None:
    # おみくじの結果を取得
    results = get_omikuji_results()
    
    # おみくじを引く
    result = draw_omikuji(results)
    
    # 結果をフォーマットして表示
    formatted_result = format_omikuji_result(result)
    print(formatted_result)

if __name__ == "__main__":
    main()  
    