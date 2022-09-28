
#!/usr/bin/python3
""" Module for appending after a string """


def append_after(filename, search_string="", new_string=""):
    """ inserts a line of text to a file,
    after each line containing a specific string
    """
    new_content = []
    with open(filename, 'r', encoding='utf8') as fs:
        for line in fs:
            new_content += [line]
            if line.find(search_string) != -1:
                new_content += [new_string]

    with open(filename, 'w', encoding='utf8') as fs:
        fs.write("".join(new_content))
