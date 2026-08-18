def ready_up() -> None:
    global valid_words

    valid_words = {}

    with open("esm_famil_data.csv", "r", encoding="utf-8") as file:
        data = file.read()

    lines = data.splitlines()
    global headers
    headers = lines[0].split(",")

    for header in headers:
        valid_words[header] = []

    for line in lines[1:]:
        row = line.split(",")

        for index, word in enumerate(row):
            word = word.replace(" ", "")
            valid_words[headers[index]].append(word)

player_answers = dict()
def add_participant(participant: str, answers: dict[str, str]):
    for key, value in answers.items():
        answers[key] = value.replace(" ", "")
    player_answers[participant] = answers


def calculate_all() -> dict[str, int]:
    player_score = dict()

    for item in headers:
        counts = dict()
        someone_dont_answer_TRUEness = False
        
        for player in player_answers:
            answer = player_answers[player][item]
            
            if answer == "":
                someone_dont_answer_TRUEness = True
                continue

            if player_answers[player][item] in valid_words[item]:
            
                if answer not in counts:
                    counts[answer] = 0
                
                counts[answer] += 1

        for player in player_answers:
            answer = player_answers[player][item]

            if player not in player_score:
                player_score[player] = 0

            if answer == "" or answer not in valid_words[item]:
                continue

            if someone_dont_answer_TRUEness:
                if counts[answer] == 1:
                    player_score[player] += 15
                else:
                    player_score[player] += 10
            else:
                if counts[answer] == 1:
                    player_score[player] += 10
                else:
                    player_score[player] += 5
    return player_score

