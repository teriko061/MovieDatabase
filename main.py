from user_interface import UserInterface

app = UserInterface()

print("-" * 30)
print("MOVIE DATABASE")
print("-" * 30)

choice = ""

while choice != "4":
    print("\nEnter your choice number:")
    print("1 - Add a movie")
    print("2 - List all movies")
    print("3 - List movies by genre")
    print("4 - Terminate\n")

    choice = input("Your choice: ").strip()

    match choice:
        case "1":
            app.insert_movie()

        case "2":
            app.show_list()

        case "3":
            app.search_by_genre()

        case "4":
            print("Thank you for using the application.")

        case _:
            print("Invalid choice, please choose from the menu below.")