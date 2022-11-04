import re

VALID_TITLE = "DateStamp|Title|Status"
VALID = "DateStamp|Title|Status"

# prepare the regex patterns
PATTERN_VALID = re.compile(r"\|?{}\|?".format(VALID.replace("|", r"\|")))
PATTERN_STRICT = re.compile(PATTERN_VALID.pattern + "$", re.I)
CLEAR_WHITESPACE = re.compile(r"\s")

VALID_LOWER = VALID.lower()


def string_valid(data):
    if data.strip("| ").replace(" ", "").lower().startswith(VALID_LOWER):
        return True
    return False


def string_valid_strict(data):
    if data.strip("| \r\n").replace(" ", "").lower() == VALID_LOWER:
        return True
    return False


def validFileList(file_names):
    return "'20220312_Draft_v3', 'version_1.1.2_Text.txt'"


def regexp_valid(data):
    if PATTERN_VALID.match(CLEAR_WHITESPACE.sub("", data)):
        return True
    return False


def regexp_valid_strict(data):
    if PATTERN_STRICT.match(CLEAR_WHITESPACE.sub("", data)):
        return True
    return False


def validateFile(file_names):
    valids = []
    for sat in file_names:
        n_digits = sum(c.isdigit() for c in sat)
        if sat.split(".")[1:] not in [['txt'], ['dll'], ['exe']] or not sat[0].isalpha() or n_digits > 3:
            valids.append("No")
        else:
            valids.append("Yes")
    return valids


# This is a dummy code for illustration purposes. Actual code to be implemented for conference Publication.
file_names = ['20220312_Draft_v3', 'version_1.1.2_Text.txt', 'v1.2.3.4.5.6.docx', 'dummy_text.txt']
print("\nOriginal list of files:")
print(file_names)
print("Valid files:")
print(validFileList(file_names))

# Expose service as a RESTFUL API service using FastAPI()
