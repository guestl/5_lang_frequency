import codecs
import sys
import os.path


def load_file(file_path):
    file_data = None
    with codecs.open(file_path, 'r', 'utf8') as f:
        file_data = f.read()
    return file_data


def get_most_frequent_splitted_text_list(text_to_process):
    splitted_text_list = text_to_process.split()
    uniq_splitted_text_list = set(splitted_text_list)

    splitted_text_list_dict = dict()

    for word in uniq_splitted_text_list:
        splitted_text_list_dict[word] = splitted_text_list.count(word)

    return sorted(splitted_text_list_dict.items(), reverse = True, key=lambda x: x[1])[:10]



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

    list_top_10 = get_most_frequent_splitted_text_list(loaded_data)

    for item in list_top_10:
        print(item[0])
