from omikuji import get_omikuji_results, draw_omikuji, format_omikuji_result

results = get_omikuji_results()
print(results)

selected_result = draw_omikuji(results)
print(selected_result)

formatted_result = format_omikuji_result(selected_result)
print(formatted_result)
