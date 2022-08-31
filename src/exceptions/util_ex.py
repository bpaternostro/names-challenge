class InvalidExtensionFile(Exception):
    def __init__(self, details):
        self.message = "File extension : {} is not a valid file to be processed".format(
            details
        )


class FileIsOpen(Exception):
    def __init__(self):
        self.message = "File is open by another process"


class FilterListException(Exception):
    def __init__(self):
        self.message = "There were problems filtering. Dictionary keys are not valid"


class SwapingDictonaryArray(Exception):
    def __init__(self):
        self.message = "There were problems swaping dictionary"


class CreateFileException(Exception):
    def __init__(self):
        self.message = "There were problems creating result file"


class GetLimitedGeneratorException(Exception):
    def __init__(self):
        self.message = "There were problems creating limited generator"

class GetCardinalityException(Exception):
    def __init__(self):
        self.message = "There were problems creating counters"

class ParseDataForFinalReportException(Exception):
    def __init__(self):
        self.message = "There were problems parsing data for final report"

class CreateHtmlRepoExcepcion(Exception):
    def __init__(self):
        self.message = "There were problems creating html report"
