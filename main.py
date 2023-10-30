from io import TextIOWrapper


class File:
    def __init__(self, file) -> None:
        self.file: TextIOWrapper = file
        self.words_list: list[str] = []

    def read(self) -> None:
        with open(self.file, "r") as f:
            print(f.read())

    def read_by_line(self) -> None:
        with open(self.file, "r") as f:
            line_no = 0
            for line in f:
                line_no += 1
                print(f"--line({line_no}): {line}")

    def read_words(self) -> list[str]:
        with open(self.file, "r") as f:
            line_no = 0
            for line in f:
                line_no += 1
                for word in line.split():
                    self.words_list.append(word)
            return self.words_list

    def compare_against(self, text) -> dict:
        words_in_text: list[str] = [word for word in text.split()]
        word_counts: dict = {}
        for word in words_in_text:
            count: int = self.words_list.count(word)
            word_counts[word] = count
        return word_counts


my_file = File("./file.txt")
my_file.read_words()
seo: dict = my_file.compare_against("hello from the other side")


print(seo)
