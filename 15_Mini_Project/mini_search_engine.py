"""
Project: Mini Search Engine
Description: Search keyword inside a text file and show occurrences
"""

def search_word_in_file(filename, keyword):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        count = 0
        matched_lines = []

        for line_number, line in enumerate(lines, start=1):
            if keyword.lower() in line.lower():
                occurrences = line.lower().count(keyword.lower())
                count += occurrences
                matched_lines.append((line_number, line.strip()))

        if count == 0:
            print(f" '{keyword}' not found in file.")
        else:
            print(f"\n🔎 Keyword '{keyword}' found {count} times.\n")
            print("Matching Lines:")
            for line_number, content in matched_lines:
                print(f"Line {line_number}: {content}")

    except FileNotFoundError:
        print(" File not found.")


def main():
    print("=== Mini Search Engine ===")
    filename = input("Enter file name (example: data.txt): ")
    keyword = input("Enter word to search: ")

    search_word_in_file(filename, keyword)


if __name__ == "__main__":
    main()