import random


def get_omikuji_results() -> list[str]:
    # おみくじ結果の一覧を返す
    return ["大吉", "中吉", "小吉", "吉", "凶"]


def draw_omikuji(results: list[str]) -> str:
    # おみくじを引いて結果を返す
    return random.choice(results)
