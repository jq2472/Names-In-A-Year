"""
file: names_in_year.py
course: CSCI-141
topic: Dictionaries & Dataclasses
homework: BabyNames
author: RIT CS
author: Jolin Qiu

The program compiles counts of baby names for a given year, ignoring gender,
and runs a query session that searches for a name and reports information.

A YearStats dataclass object stores the year, the total name count, and
the name-to-count dictionary compiled from the year's data file.

The program requires one command line argument: the year; for example:
        $ python3 names_in_year.py 2017

"""

import sys              # sys.argv
from dataclasses import dataclass

# The range of valid years of data is 1880 to 2018.
START_YEAR = 1880
END_YEAR = 2018


@dataclass
class YearStats:
    """
    A YearStats structure stores information produced by get_names_in_year().
    Fields:
    year: (int) the year that was given on the command line
    total: (int) the total count of all names in that year)
    names: (dict) a dictionary mapping baby names to the count that appeared in the year
    The counts stored in the dictionary are counts of each name regardless of gender.
    """
    year: int
    total: int
    names: dict


def get_filename(year):
    """
    get the file path, a string for a filename associated with the year.
    :param year: the desired year
    :return: a string, e.g. './data/yob1990.txt' if year = 1990
    """
    return '../data/yob' + str(year) + '.txt'


def get_names_in_year(year):
    """
    For the given year, compute the total number of all names and
    the counts of each individual name but ignoring gender; that is
    combine counts of both genders of a name that is both female and male.
    :param year: the year
    :return: YearStats of year, total names, dictionary mapping names to counts
    """
    # Create an initially empty dictionary mapping names to counts of babies.
    names = {}  # {baby_names: count}
    # Keep track of the overall total of babies encountered
    total_names = 0
    with open(get_filename(year)) as file:
        for line in file:
            stats = line.split(",")  # stats = [Mary, F, 7065]
            total_names += int(stats[2])  # 7065 + ...
            baby_name = stats[0]  # Mary
            count = int(stats[2])  # 7065
            # names[baby_name] = count  # assigns count (value) to baby_name (key) in dict. Mary = 7065
            if baby_name in names:
                names[baby_name] += int(count)
            else:
                names[baby_name] = count
    return YearStats(year, total_names, names)  # return object: YearStats(2018, 7065 + ..., {Mary, 7065})


def run_query(stats):
    """
    get total names and dictionary of gender insensitive names->count in year,
    and offer a choice to query about any name. 
    If the name is present, print the year, the name,
    the gender neutral count of occurrences, and the percent of
    the total. If the name is not present, print it is absent,
    Reprompt until the name input is an empty string.
    :param stats: YearStats object
    """
    if stats is None:
        print("Error: no statistics to query")
    else:
        name = input("Enter a name to investigate: ")  # Mary , YearStats(2018, 7065 + ..., {Mary, 7065})
        while name != "":
            # changes the name to be a Proper Noun as 'brian' is not going to be in the data
            name = name.title()
            if name in stats.names:
                year = stats.year
                # accessing count of "name" that the user had inputted from the actual dict.key names
                count = stats.names[name]
                percent = (count / stats.total) * 100
                print(year)
                print(name)
                print(count)
                print(str('%.2f' % percent) + "% of all names")  # truncates value to 3 places

            else:
                print(name, "is not in the data.")

            name = input("Enter a name to investigate: ")  # Mary , YearStats(2018, 7065 + ..., {Mary, 7065})


def main():
    """
    The main program reads the command line, calls get_names_in_year
    to compute and return the result, and runs a details of the result.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 names_in_year.py year")
        return
    else:
        # there is a command line argument, sys.argv[1], the year of the baby names
        year = int(sys.argv[1])
        if 1880 <= year <= 2018:
            run_query(get_names_in_year(year))  # object: YearStats(2018, 7065 + ..., {Mary, 7065})
        else:
            print("Please enter within a valid range of years (1880-2018")


if __name__ == '__main__':
    main()
