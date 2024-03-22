def main():
    def read_book(title_path):
        with open(title_path, "r") as current_file:
            text = current_file.read()
        return text

    def word_counter(file_contents):
        words = file_contents.split()
        return len(words)

    def letters_counter(file_contents):
        letters = file_contents.lower()
        letter_map = {}

        for letter in letters:
            if not letter.isalpha():
                continue
            if letter not in letter_map:
                letter_map[letter] = 0
            letter_map[letter] += 1

        return letter_map

    def letter_distribution_report(letter_map):
        for letter, count in letter_map.items():
            print(f"The '{letter}' character was found {count} times")

    def sorted_letter_distribution_report(letter_map):
        sorted_letter_map = dict(
            sorted(letter_map.items(), key=lambda item: item[1], reverse=True)
        )
        for letter, count in sorted_letter_map.items():
            print(f"The '{letter}' character was found {count} times")

    book = read_book("./books/frankenstein.txt")
    count = word_counter(book)
    letters = letters_counter(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print("The book has " + str(count) + " words")
    # letter_distribution_report(letters)
    sorted_letter_distribution_report(letters)


main()
