def comfortable_word(word):
    left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
    right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"}
    list1 = list()
    list2 = list()

    for item in word[::2]:
        list1.append(item)
    for el in word[1::2]:
        list2.append(el)
    result = all(elem in left for elem in list1)
    result2 = all(elem in right for elem in list1)
    result3 = all(elem in left for elem in list2)
    result4 = all(elem in right for elem in list2)
    if result and result4:
        return True
    elif result2 and result3:
        return True
    else:
        return False

import re
def comfortable_word(word):
    uncomfortable = re.compile("([qwerasdfgzxcvb]{2}|[yuiophjklnm]{2})+")
    return False if uncomfortable.search(word) else True

print(comfortable_word("test"))
print(comfortable_word("yams"))
print(comfortable_word("touts"))
