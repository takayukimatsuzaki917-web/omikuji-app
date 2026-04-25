from omikuji import get_omikuji_results, draw_omikuji

results = get_omikuji_results()
print(results)

selected_result = draw_omikuji(results)
print(selected_result)
