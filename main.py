path_to_file = "books/frankenstein.txt"

def main():
    file_content = read_file(path_to_file)
    num_words = get_num_words(file_content)
    chars_dict = get_chars_dict(file_content)
    sorted_chars_dict = sort_chars_dict(chars_dict)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document")
    print("\n")

    for char, count in sorted_chars_dict.items():
        if char == '\n':
            continue
        print(f"The \'{char}\' character was found {count} times")
    
    print("--- End report ---")
    
    

def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(file_content):
    words = file_content.split()
    return len(words)

def get_chars_dict(file_content):
    chars = {}
    for char in file_content:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars_dict(chars_dict):
    # Convert to list of tuples
    chars_tuples = chars_dict.items()
    # Sort tuple
    sorted_chars_tuples = sorted(chars_tuples, key=lambda item: item[1], reverse=True)
    # Convert back into dictionary
    return dict(sorted_chars_tuples)

main()