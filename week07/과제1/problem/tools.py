"""tools.py - 박스오피스 정보를 가져오는 도구 모음"""
import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/"
            "boxoffice/searchDailyBoxOfficeList.json")


def get_movie_audience(data, title):
    """
    그 날짜의 박스 오피스 1위 영화의 관객 수를 알려준다.

    받는 것: 8자리 날짜와 영화 제목. 예: "20260824", "오디세이"
    돌려주는 것: 관객 수 문자열. 예: 186,587명
    """

    params = {"key": API_KEY, "targetDt": data}
    response = requests.get(BASE_URL, params=params, timeout=10)
    result = response.json()

    for movie in result['boxOfficeResult']['dailyBoxOfficeList']:
        if movie['movieNm'] == title:
            return f"{int(movie['audiCnt']):,}명"

    return f"'{title}'은(는) {data} 순위에 없습니다."