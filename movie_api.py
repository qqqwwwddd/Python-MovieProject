import requests

# pip instrall requests

def callMovieApi(page=1):  # movie를 받기위한 함수
    url = f'''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}1&limit=20
    '''
    response = requests.get(url)

    responseDict = response.json() # 딕셔너리 타입으로 변환
    movies = responseDict["data"]["movies"] # list 타입
    return movies
