all_users = {}
all_albums = {}


def add_user(username: str, age: int, city: str, albums: list, all_users: dict) -> None:
    user = {
        "age" : age,
        "city" : city,
        "albums" : albums
    }
    all_users[username] = user

def add_album(name: str, artist: str, genre: str, tracks: int, all_albums: dict) -> None:
    album = {
        "artist" : artist,
        "genre" : genre,
        "tracks" : tracks
    }
    all_albums[name] = album


def query_user_artist(username: str, artist: str, all_users: dict, all_albums: dict) -> int:
    tracks = 0
    for item in all_users[username]["albums"]:
        if all_albums[item]["artist"] == artist:
            tracks += all_albums[item]["tracks"]
    return tracks


def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    tracks = 0
    for item in all_users[username]["albums"]:
        if all_albums[item]["genre"] == genre:
            tracks += all_albums[item]["tracks"]
    return tracks
 
def query_age_artist(age: int, artist: str, all_users: dict, all_albums: dict) -> int:
    tracks = 0
    for item in all_users:
        if all_users[item]["age"] == age:
            for j in all_users[item]["albums"]:
                if all_albums[j]["artist"] == artist:
                    tracks += all_albums[j]["tracks"]
    return tracks


def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    tracks = 0
    for item in all_users:
        if all_users[item]["age"] == age:
            for j in all_users[item]["albums"]:
                if all_albums[j]["genre"] == genre:
                    tracks += all_albums[j]["tracks"]
    return tracks

def query_city_artist(city: str, artist: str, all_users: dict, all_albums: dict) -> int:
    tracks = 0
    for item in all_users:
        if all_users[item]["city"] == city:
            for j in all_users[item]["albums"]:
                if all_albums[j]["artist"] == artist:
                    tracks += all_albums[j]["tracks"]
    return tracks


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    tracks = 0
    for item in all_users:
        if all_users[item]["city"] == city:
            for j in all_users[item]["albums"]:
                if all_albums[j]["genre"] == genre:
                    tracks += all_albums[j]["tracks"]
    return tracks




# add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users)
# add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users)
# add_album("eclipse", "malmsteen", "classic", 10, all_albums)
# add_album("barf", "beeptunes", "pop", 22, all_albums)
# add_album("tekunbede", "beeptunes", "pop", 14, all_albums)
# add_album("gavazn", "sorena", "persian", 18, all_albums)
# add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users)
# add_album("bidad", "shajarian", "classic", 10, all_albums)
# add_album("blaze", "ghorbani", "pop", 9, all_albums)

# print(query_user_artist("Ali", "ghorbani", all_users, all_albums))
# print(query_user_genre("Ali", "classic", all_users, all_albums))
# print(query_age_artist(12, "shajarian", all_users, all_albums))
# print(query_age_genre(12, "pop", all_users, all_albums))
# print(query_city_artist("Bushehr", "ghorbani", all_users, all_albums))
# print(query_city_genre("Bushehr", "pop", all_users, all_albums))


# add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users)
# add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users)
# add_album("eclipse", "malmsteen", "classic", 10, all_albums)
# add_album("barf", "beeptunes", "pop", 22, all_albums)
# add_album("tekunbede", "beeptunes", "pop", 14, all_albums)
# add_album("gavazn", "sorena", "persian", 18, all_albums)
# add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users)
# add_album("bidad", "shajarian", "classic", 10, all_albums)
# add_album("blaze", "ghorbani", "pop", 9, all_albums)

# print(query_user_artist("SAliB", "sorena", all_users, all_albums))
# print(query_user_artist("SAliB", "beeptunes", all_users, all_albums))
# print(query_user_genre("SAliB", "pop", all_users, all_albums))
# print(query_age_artist(22, "malmsteen", all_users, all_albums))
# print(query_age_genre(19, "pop", all_users, all_albums))
# print(query_city_artist("Tehran", "sorena", all_users, all_albums))
# print(query_city_genre("Tehran", "pop", all_users, all_albums))
