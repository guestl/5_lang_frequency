import codecs
import sys
import os.path
from collections import Counter


def load_file(file_path):
    file_data = None
    with codecs.open(file_path, 'r', 'utf8') as f:
        file_data = f.read()
    return file_data


def get_most_frequent_words(text_to_process):
    words_dict = Counter(text_to_process.split())

    return sorted(words_dict.items(), reverse = True, key=lambda x: x[1])[:10]



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You have to use file name as parameters. \
               \nExample: python lang_frequency.py <path to file>")
        exit()

    file_name = sys.argv[1]

    if os.path.isfile(file_name):
        loaded_data = load_file(file_name)
    else:
        print("File '%s' must exists" % file_name)
        exit()

    list_top_10 = get_most_frequent_words(loaded_data)

    for single_word in list_top_10:
        print(single_word[0])
