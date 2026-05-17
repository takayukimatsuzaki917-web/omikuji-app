import random

KINGEN = {
    "大吉": [
        "天は自ら助くる者を助く",
        "笑う門には福来たる",
        "七転び八起き、何度でも立ち上がれ",
        "千里の道も一歩から",
        "花は咲いても根を忘れるな",
    ],
    "中吉": [
        "継続は力なり",
        "急がば回れ",
        "石の上にも三年",
        "実るほど頭を垂れる稲穂かな",
        "努力に勝る天才なし",
    ],
    "小吉": [
        "塵も積もれば山となる",
        "焦らず、着実に一歩ずつ",
        "丁寧に生きることが大切",
        "小さな幸せを見逃さないように",
        "今日の積み重ねが明日を作る",
    ],
    "吉": [
        "感謝の心が幸福の扉を開く",
        "今この瞬間を大切に",
        "人との縁を大切にしよう",
        "平穏な心が最大の宝",
        "小さなことにも感謝を忘れずに",
    ],
    "凶": [
        "雨降って地固まる",
        "冬来たりなば春遠からじ",
        "困難は成長のチャンス",
        "暗いうちは星が美しく見える",
        "今日の試練が明日の糧となる",
    ],
}


def get_omikuji_results() -> list[str]:
    return ["大吉", "中吉", "小吉", "吉", "凶"]


def draw_omikuji(results: list[str]) -> str:
    return random.choice(results)


def get_kingen(result: str) -> str:
    quotes = KINGEN.get(result, ["今日も一日、丁寧に過ごしましょう"])
    return random.choice(quotes)


def format_omikuji_result(result: str) -> str:
    return f"あなたの運勢は「{result}」です！"
