current_year = 2021
try:
    while True:
        print("Welcome To Program - Your Age In 2090")
        print("First you will enter your age or birth year :-")
        ageoryear = int(input())
        if len(str(ageoryear)) <= 3 and ageoryear > 100 and ageoryear > 105:
            print("You seem to be the oldest person alive")
            print("Please enter correct value")
            continue
        elif len(str(ageoryear)) <= 3 and 100 < ageoryear < 105:
            age = 100 - ageoryear
            year = current_year + age
            print(f"You have already turned 100 in year {year}")
        elif len(str(ageoryear)) == 4 and ageoryear > current_year:
            print("You are not yet born")
            print("Please enter correct value")
            continue
        elif len(str(ageoryear)) == 4 and current_year - ageoryear > 100:
            print("You seem to be the oldest person alive")
            print("Please enter correct value")
            continue
        elif len(str(ageoryear)) == 4:
            print("You have entered your birth year")
            yearin100 = ageoryear + 100
            print(f"You turn 100 in year {yearin100}")

        elif len(str(ageoryear)) <= 3:
            print("You have entered your age")
            age = 100 - ageoryear
            year = current_year + age
            print(f"You turn 100 in year {year}")
        elif len(str(ageoryear)) > 4:
            print("Please enter correct value")
            continue
        elif len(str(ageoryear)) == 4 and yearin100 < current_year:
            print("You seem to be the oldest person alive")
            print("Please enter correct value")
            continue

        print("If you want to know your age in a particular year, press C or if you want exit please press E")
        yore = input()
        if yore == "E":
            print("Thanks for coming")
            exit()
        elif yore == "C":
            if len(str(ageoryear)) <= 3:
                agefory = ageoryear
            elif len(str(ageoryear)) == 4:
                agefory = current_year - ageoryear
            print("Please enter your desire year")
            party = int(input())
            if len(str(ageoryear)) == 4 and party < ageoryear:
                print("Please enter correct value")
                print("You are born after this year")
            elif len(str(ageoryear)) <= 3 and current_year - ageoryear > party:

                print("Please enter correct value")
                print("You are born after this year")

            elif current_year > party:
                your_age_inparticular_year = current_year - party
                print(f"Your age in {party} is {agefory + your_age_inparticular_year}")
            elif current_year < party:
                your_age_inparticular_year = party - current_year
                print(f"Your age in {party} is {agefory + your_age_inparticular_year}")

            print("If you want to exit the program enter E or if you want try one more time enter C ")
            try_or_not = input()
            if try_or_not == "E":
                print("Thanks for coming")
                exit()
            elif try_or_not == "C":
                continue
except ValueError as e:
    print("Please enter correct value.",e)
    print("Please restart the program")

