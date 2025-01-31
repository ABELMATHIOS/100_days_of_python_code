# while True:
#     playlist = {}
#     title = input("Tell me a title: ")
#     artist = input("Artist name: ")
#     duration = float(input("Duration: "))
#     def add_song(title, artist, duration):
#         if playlist  == '':
#             print('add song to the playlist')
#         # else:
#             playlist['title_name'] = title
#             playlist['artist_name'] = artist
#             playlist['duration'] = duration
#             print(playlist)
#         ask_user = input("would u like to play again type 'y' for yes or press any key to exit.: ")
#         #if ask_user ==
#
#     add_song(title=title,artist=artist,duration=duration)
# def add(a,b,c):
#     add_num = a + b + c
#     print(add_num)
#
# add(3,2,3)
# def num(n):
#     if n <= 1:
#         return n
#     else:
#         return  (num(n-1) + num(n-2))
#
# user_input = int(input("Enter a number: "))
# print(num(n=user_input))

def powerq(n,p=5):
    if p ==0:
        return 1
    elif p == 1:
        return n
    else:
        return powerq(n, p-1) * n

print(powerq(2))
