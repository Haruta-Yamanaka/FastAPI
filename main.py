from typing import Optional

from fastapi import FastAPI
import random  # randomライブラリを追加

question_text = "ドラえもんは西暦何年からやってきたでしょう？"
correct_answer = os.getenv("CORRECT_ANSWER", "")


@app.get("/quiz")
async def quiz():
    return {"question": question_text}


@app.get("/quiz")
async def quiz_answer(answer: str):
    # 結果を格納するためのリストを作成します
    result = []
    all_correct = True  # すべて正解かどうかを示すフラグ

    # ユーザーの答えと正解の答えを比較します
    for i in range(len(correct_answer)):
        if i < len(answer) and answer[i] == correct_answer[i]:
            # 一致する文字はそのまま追加します
            result.append(answer[i])
        else:
            # 一致しない部分は '?' を追加する
            result.append("?")
            all_correct = False

    result_str = "".join(result)

    return {"result": result_str, "all_correct": all_correct, "question": question_text}
