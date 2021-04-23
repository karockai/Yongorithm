# https://programmers.co.kr/learn/courses/30/lessons/42579

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


import heapq
def solution(genres, plays):
    answer = []
    genrePlayDic = {}
    genreSongDic = {}
    for i in range(len(genres)):
        if (genres[i] in genrePlayDic):
            # 1. 우선 장르 총 재생수가 필요함 {genre : totalPlay}
            genrePlay = genrePlayDic[genres[i]] + plays[i]
            genrePlayDic[genres[i]] = genrePlay

            # 2. 노래를 장르별로 담아둠 {genre : [[plays, idx]]}
            songList = genreSongDic[genres[i]]
            songList.append([plays[i], i])
        else:
            genrePlayDic[genres[i]] = plays[i]
            genreSongDic[genres[i]] = [[plays[i], i]]

    genreRank = list(genrePlayDic.items())
    genreRank.sort(reverse=True, key=lambda x: (x[1]))

    for genreInfo in genreRank:
        genre = genreInfo[0]
        songList = genreSongDic[genre]
        songList.sort(reverse=True, key=lambda x: (x[0], -x[1]))

        answer.append(songList[0][1])
        if (len(songList) > 1):
            answer.append(songList[1][1])

    
    return answer

print(solution(genres, plays))