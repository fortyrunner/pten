from power_of_10 import athletes, coaches, exceptions


def get_arena_members():
    members = athletes.search_athletes(club="Arena 80")
    members.sort(key=lambda item: int(item.get("athlete_id")))
    return members


def print_member_list(members):
    print(" There are ", len(members), " Arena 80 athletes")
    print("id,firstname,surname,age,sex")
    for athlete in members:
        print(athlete["athlete_id"], ",", athlete["firstname"], ",", athlete["surname"], ",", athlete["sex"], ",",
              athlete["track"])


members = get_arena_members()
print_member_list(members)



