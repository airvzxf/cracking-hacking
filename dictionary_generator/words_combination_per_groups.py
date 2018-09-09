#!/usr/bin/python
# -*- coding: utf-8 -*-


def capitalization_permutations(word: str):
    if word == '':
        yield ''
        return
    for rest in capitalization_permutations(word[1:]):
        yield word[0].lower() + rest
        if word[0].lower() != word[0].upper():
            yield word[0].upper() + rest


def words_combination(words_list: list,
                      lower_upper_case: bool = False,
                      last_word: str = '',
                      index: int = 0,
                      file_handler=None) -> int:
    if words_list is None:
        return 0

    if len(words_list) == 0 or len(words_list) == index:
        return 0

    words = words_list[index]

    for word in words:
        if lower_upper_case:
            mixed_words = capitalization_permutations(word)

            for mixed_word in mixed_words:
                new_mixed_last_word = "{}{}".format(last_word, mixed_word)

                if file_handler is not None:
                    file_handler.write(new_mixed_last_word)
                    file_handler.write("\n")

                words_combination(words_list,
                                  lower_upper_case=lower_upper_case,
                                  last_word=new_mixed_last_word,
                                  index=index + 1,
                                  file_handler=file_handler)
        else:
            new_last_word = "{}{}".format(last_word, word)

            if file_handler is not None:
                file_handler.write(new_last_word)
                file_handler.write("\n")

            words_combination(words_list,
                              lower_upper_case=lower_upper_case,
                              last_word=new_last_word,
                              index=index + 1,
                              file_handler=file_handler)

    return 0


# rmf myFile_*
# zip2john myFile.zip > myFile_hashes
# john --session=myFile_session --wordlist=words.list --format=zip-opencl myFile_hashes
# 7z x -pMyPassword123 myFile.zip

if __name__ == '__main__':
    words_list = list()

    words_list.append(
        ["a", "b", "c"])
    words_list.append(["", "_", "!", "_", "-", " "])
    words_list.append(
        ["1", "2", "3"])
    words_list.append(["!", "!!", "!!!", "#", ".", "$"])

    f = open("words.list", "w")

    print("Working...")

    words_combination(words_list, lower_upper_case=True, file_handler=f)

    print("The permutations has been created.")
    f.close()

    print("Finished!")
