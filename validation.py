from datetime import datetime

class InputValidator:

    def enter_data(self, message, validation, error_message):
        while True:
            entry = input(message).strip()

            if validation(entry):
                return entry

            print(error_message)

    def enter_name(self):
        name = self.enter_data("Enter the name of the movie:\n", self.validate_name, "Name of the movie is empty.")
        return name

    def enter_genre(self):
        genre = self.enter_data("Enter genre (animated, adventure, comedy, crime, drama, fantasy, historical, horror, sci-fi):\n", self.validate_genre, "Invalid genre.")
        return genre

    def enter_year(self):
        year = int(self.enter_data("Enter year:\n", self.validate_year, "Enter valid year (yyyy)."))
        return year


    def validate_name(self, entry):
        return entry != ""

    def validate_genre(self, entry):
        valid_genres = {
            "animated",
            "adventure",
            "comedy",
            "crime",
            "drama",
            "fantasy",
            "historical",
            "horror",
            "sci-fi"
        }

        return entry.strip().lower() in valid_genres

    def validate_year(self, entry):
        return entry.isdigit() and 1900 < int(entry) <= datetime.now().year


