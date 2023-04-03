import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_rq_prompt(query):
    return """Query에 대해 Related Query를 만들어줘

        Query: 아이유 콘서트
        Rq: 아이유 콘서트 일정, 아이유 콘서트 티켓, 아이유 콘서트 가격
        Query: bts 멤버 이름
        Rq: 뷔, 정국, 제이홉
        Query: {}
        Rq:""".format(
        query.capitalize()
    )

    # 에이핑크 멤버 ->  손나은, 이엑


def generate_suggest_prompt(query):
    return """Query에 대해 Suggest를 만들어줘

        Query: 아
        Rq: 알바몬, 알바천국, 알라딘
        Query: 오
        Rq: 오늘의 운세, 옥션, 오늘의 날씨
        Query: {}
        Rq:""".format(
        query.capitalize()
    )

    # 가 -> 가방, 가상


if __name__ == '__main__':
    query = "가"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_suggest_prompt(query),
        temperature=0.6,  # Randomness
    )

    result = response.choices[0].text
    print(result)
