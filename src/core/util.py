import itertools
import re

from itertools import chain
from collections import Counter

from src.core.constants import (
    VALID_FORMATS,
    SPECIAL_CHARACTERS,
    PATH_TO_RESULTS,
    FINAL_REPORT,
)
from src.core.html_generator import get_html_report
from src.core.logs import logging
from src.exceptions.util_ex import (
    InvalidExtensionFile,
    FileIsOpen,
    FilterListException,
    SwapingDictonaryArray,
    CreateFileException,
    GetLimitedGeneratorException,
    GetCardinalityException,
    ParseDataForFinalReportException,
    CreateHtmlRepoExcepcion
)

def parse_for_final_report(data:dict):
    """
    Builds a dictionary with rows for html report

        Parameters:
            [dict] data: dictionaries with lists
        
        Returns:
            [dict] returns a dictionary with html rows
    """
    def row_creator(r:str):
        return "<tr><td>{}</td><td style='width:25%; text-align: center; vertical-align: middle;'>{}</td></tr>".format(r[0],r[1])

    try:
        return {
            "full_names": ''.join([row_creator(r) for r in data["full_names"]]),
            "last_names":''.join([row_creator(r) for r in data["last_names"]]),
            "names":''.join([row_creator(r) for r in data["names"]]),
            "distincts":''.join([row_creator(r) for r in data["distincts"]])
        }
    except Exception as e:
        raise ParseDataForFinalReportException()

def create_file(file_name: str, rows):
    """
    Fill a file with the results.

            Parameters:
                    file_name (str): output filename
                    rows (list/generator): list to be printed in the file

            Returns:
                    None
    """
    try:
        with open(
            "{relative}/{file_name}".format(
                relative=PATH_TO_RESULTS, file_name=file_name
            ),
            "w",
        ) as result:
            [result.write(item["full_name"] + "\n") for item in rows]
    except Exception as e:
        raise CreateFileException()

def create_html_repo(**kwargs):
    """
    Creates a result in folder results with name report.html.

            Parameters:
                    [dict] kwargs:
                        [str] step1 result filename
                        [str] step2 result filename
                        [str] filename processed
                        [int] limited rows
                        [str] time spended

            Returns:
                    None
    """

    def row_creator(r: str):
        return "<tr><td>{}</td></tr>".format(r.replace("\n", ""))

    def create_html(html: str):
        with open("{}/{}".format(PATH_TO_RESULTS, FINAL_REPORT), "w") as f:
            f.write(html)

    try:
        with open("{}/{}".format(PATH_TO_RESULTS, kwargs["file"]), "r") as f:
            rows = [row_creator(r) for r in f]
            results = "".join(rows)

        create_html(
            get_html_report(
                result=results,
                counts=kwargs["counts"],
                file_name=kwargs["file_name"],
                rows=kwargs["rows"],
                time=kwargs["time"],
            )
        )
    except Exception as e:
        raise CreateHtmlRepoExcepcion()

def filter_list(limited_list):
    """
    Filters generator with rules defined in step1

        Parameters:
            [generator] limited_list: generator to be processed

        Returns:
            [list] returns a list with valid users
    """
    final_name_list = []

    def _should_enter(person: dict):
        # cheking if person last_name and name is in list
        checker = list(
            map(
                lambda p: (person["last_name"] in p["last_name"])
                or (person["name"] in p["name"]),
                final_name_list,
            )
        )
        if not (True in checker):
            final_name_list.append(person)

    try:
        temp_list = list(map(lambda p: _should_enter(p), limited_list))
    except Exception as e:
        raise FilterListException()
    else:
        return final_name_list

def get_cardinality(persons):
    """
    Builds a dictionary with a counter by full_name, last_name and name

        Parameters:
            [generator] persons: list of dictionaries
        
        Returns:
            [dict] returns a dictionary with counters
    """
    try:
        c_full_names = Counter()
        c_last_names = Counter()
        c_names = Counter()
        for p in persons:
            c_full_names[p["full_name"]] += 1
            c_last_names[p["last_name"]] += 1
            c_names[p["name"]] += 1

        # prepares everything for the html report
        distincts = [("full_names",len(c_full_names)),("last_name",len(c_last_names)),("names",len(c_names))]
        return {
            "full_names": c_full_names.most_common(),
            "last_names":c_last_names.most_common(),
            "names":c_names.most_common(),
            "distincts":distincts
        }
    except Exception as e:
        raise GetCardinalityException()

def get_limited_generator(path: str, limit: int, copies: int):
    """
    Builds generator with specific parameters

        Parameters:
            [string] path: path to file to be processed
            [int] limit: limit to be applied to the generator
            [int] copies: # copies to be generated

        Returns:
            [generator] returns a limited generator with users
    """
    try:
        lines = get_names_generator(path=path)  # creates generator
        limited_list = itertools.islice(lines, limit) if limit!=0 else limited_list # grab n elements
        return itertools.tee(limited_list,copies) # creates copies
    except Exception as e:
        logging.error(str(e))
        raise GetLimitedGeneratorException()

def get_names_generator(path: str):
    """
    Yield a name checking line by line of the file

        Parameters:
            [string] path: path to file to be processed

        Returns:
            [dict] yield a dict for each user

    """

    def _is_name(line: str):
        # check if it is a name and returns line name part
        return (
            str(line).split("--")[0].replace("b'", "")
            if str(line).split(" ")[0] != "b'" and str(line).split(" ")[0] != ""
            else None
        )

    def _check_special_ch(name: str):
        # check with regular expressions if the string has special characters
        string_check = re.compile(SPECIAL_CHARACTERS)
        return string_check.search(name) == None  # check if it has special characters

    def _get_dict(name):
        # creates a dict of each person (if it is valid)
        aux = name.split(",")
        name = aux[1].replace(" ", "")
        last_name = aux[0]
        return {
            "last_name": last_name,
            "name": name,
            "full_name": "{last_name}, {name}".format(last_name=last_name, name=name),
        }

    file_extension = path.split(".")[-1]
    if not (file_extension in VALID_FORMATS):
        raise InvalidExtensionFile(details=file_extension)

    try:
        with open(path, "r") as f:
            for line in f:
                name = _is_name(line)
                if name is not None and _check_special_ch(name):
                    yield _get_dict(name)
    except IOError:
        # Raise error if the file is opened
        raise FileIsOpen()

def mix_person_names(person_list, last_name: dict):
    """
    Mix persons names from generator with rules defined in step2

        Parameters:
            [generator] person_list: generator to be processed
            [dict] last_name: last name in list [:-1]

        Returns:
            [dict] yields each new user
    """

    def _set_person_new_name(person, name):
        person["name"] = name
        person["full_name"] = "{}, {}".format(person["last_name"], person["name"])
        return person

    aux_name = last_name["name"]
    try:
        for p in person_list:
            actual_name = p["name"]
            swap_person = _set_person_new_name(p, aux_name)
            aux_name = actual_name
            yield swap_person
    except Exception as e:
        raise SwapingDictonaryArray()
