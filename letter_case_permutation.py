def letter_case(string):
    output = [""]
    for char in string:
        tmp = []
        if char.isalpha():
            for o in output:
                tmp.append(o+char.lower())
                tmp.append(o+char.upper())
        else:
            for o in output:
                tmp.append(o+char)
        output = tmp
    return output


s = "a1b2"
print(letter_case(s))
