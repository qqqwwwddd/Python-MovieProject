from movie_model import MovieModel
import requests

# pip instrall requests

def callMovieApi(page=1):  # movie를 받기위한 함수
    url = f'''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number={page}1&limit=20
    '''
    response = requests.get(url)

    responseDict = response.json() # 딕셔너리 타입으로 변환
    movies = responseDict["data"]["movies"] # list 타입
    return convert_model(movies)


def convert_model(movies): # model로 변경하는 함수
    list = []

    for movie in movies:  # movie를 movie_model에 옮겨 담아야함 
        movie_model = MovieModel(movie["title"], movie["rating"], movie["medium_cover_image"])
        list.append(movie_model) # list에 넣어줌

    print(list)
    return list