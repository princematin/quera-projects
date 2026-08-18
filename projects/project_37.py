import os


def extension_combat(salib_format: str, sajjad_format: str, path: str) -> str:
    salib_count = 0
    sajjad_count = 0
    files = dict()

    for root, dirs, files2 in os.walk(path):
        for file in files2:
            splited_path_file = file.split(".")
            file_name = splited_path_file[0].lower()
            file_postfix = splited_path_file[1].lower()

            if file_name not in files:
                files[file_name] = {
                    "total" : 0,
                    "salib" : 0,
                    "sajjad" : 0
                }

            if file_postfix == sajjad_format:
                files[file_name]["sajjad"] += 1
                sajjad_count += 1

            elif file_postfix == salib_format:
                files[file_name]["salib"] += 1
                salib_count += 1

            files[file_name]["total"] += 1

    if sajjad_count > salib_count:
        return "Win! Normally!"

    for key, value in files.items():
        win_count_sajjad = sajjad_count + value["total"]
        win_count_salib = salib_count - value["salib"]

        if win_count_sajjad > win_count_salib:
            cheat_name = key
            return f"Win! you can win if you cheat on '{cheat_name}'!"

    return "Lose! you can't win this game!"