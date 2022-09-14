# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    name = "webMD_Reviews"
    drugNames = []

    # URLS to be parsed
    start_urls = []

    # Link to be appended to the begging of the name
    startingLink = '?conditionid=&sortval=1&page=2'
    split = '&next_page'

    res = startingLink.partition(split)[0]

    print(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
