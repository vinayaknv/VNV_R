import re
def rearrange_name(text):
    result = re.search(r"^([\w .]*),([\w .]*)$",text)
    if result is None:
        return text
    return "{} {}".format(result[2],result[1])