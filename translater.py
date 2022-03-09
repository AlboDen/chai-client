class TRANSLATE():
    into_str = "*ogurt"
    out_str = ""
    def rus_in_eng():
        # out_str = ""
        print("Translating from RU to EN:")
        for i in TRANSLATE.into_str:
            if i == "№":
                TRANSLATE.out_str += "№"
            if i == " ":
                TRANSLATE.out_str += " "
            if i == ",":
                TRANSLATE.out_str += ","
            if i == ":":
                TRANSLATE.out_str += ":"
            if i == "/":
                TRANSLATE.out_str += "/"
            if i == ".":
                TRANSLATE.out_str += "."
            if i == "'":
                TRANSLATE.out_str += "'"
            if i == '"':
                TRANSLATE.out_str += '"'
            if i == "-":
                TRANSLATE.out_str += "-"
            if i == "_":
                TRANSLATE.out_str += "_"
            if i == "+":
                TRANSLATE.out_str += "+"
            if i == "=":
                TRANSLATE.out_str += "="
            if i == "(":
                TRANSLATE.out_str += "("
            if i == ")":
                TRANSLATE.out_str += ")"
            if i == "#":
                TRANSLATE.out_str += "#"
            if i == "%":
                TRANSLATE.out_str += "%"
            if i == "1":
                TRANSLATE.out_str += "1"
            if i == "2":
                TRANSLATE.out_str += "2"
            if i == "3":
                TRANSLATE.out_str += "3"
            if i == "4":
                TRANSLATE.out_str += "4"
            if i == "5":
                TRANSLATE.out_str += "5"
            if i == "6":
                TRANSLATE.out_str += "6"
            if i == "7":
                TRANSLATE.out_str += "7"
            if i == "8":
                TRANSLATE.out_str += "8"
            if i == "9":
                TRANSLATE.out_str += "9"
            if i == "0":
                TRANSLATE.out_str += "0"

            if i == "а":
                TRANSLATE.out_str += "a"
            if i == "А":
                TRANSLATE.out_str += "A"
            if i == "б":
                TRANSLATE.out_str += "b"
            if i == "Б":
                TRANSLATE.out_str += "B"
            if i == "в":
                TRANSLATE.out_str += "v"
            if i == "В":
                TRANSLATE.out_str += "V"
            if i == "г":
                TRANSLATE.out_str += "g"
            if i == "Г":
                TRANSLATE.out_str += "G"
            if i == "д":
                TRANSLATE.out_str += "d"
            if i == "Д":
                TRANSLATE.out_str += "D"
            if i == "е":
                TRANSLATE.out_str += "ye"
            if i == "Е":
                TRANSLATE.out_str += "Ye"
            if i == "Ё":
                TRANSLATE.out_str += "Yo"
            if i == "ё":
                TRANSLATE.out_str += "yo"
            if i == "ж":
                TRANSLATE.out_str += "j"
            if i == "Ж":
                TRANSLATE.out_str += "J"
            if i == "з":
                TRANSLATE.out_str += "z"
            if i == "З":
                TRANSLATE.out_str += "Z"
            if i == "и":
                TRANSLATE.out_str += "yi"
            if i == "И":
                TRANSLATE.out_str += "Yi"
            if i == "к":
                TRANSLATE.out_str += "k"
            if i == "К":
                TRANSLATE.out_str += "K"
            if i == "л":
                TRANSLATE.out_str += "l"
            if i == "Л":
                TRANSLATE.out_str += "L"
            if i == "м":
                TRANSLATE.out_str += "m"
            if i == "М":
                TRANSLATE.out_str += "M"
            if i == "н":
                TRANSLATE.out_str += "n"
            if i == "Н":
                TRANSLATE.out_str += "N"
            if i == "о":
                TRANSLATE.out_str += "o"
            if i == "О":
                TRANSLATE.out_str += "O"
            if i == "п":
                TRANSLATE.out_str += "p"
            if i == "П":
                TRANSLATE.out_str += "P"
            if i == "р":
                TRANSLATE.out_str += "r"
            if i == "Р":
                TRANSLATE.out_str += "R"
            if i == "с":
                TRANSLATE.out_str += "s"
            if i == "С":
                TRANSLATE.out_str += "S"
            if i == "т":
                TRANSLATE.out_str += "t"
            if i == "Т":
                TRANSLATE.out_str += "T"
            if i == "у":
                TRANSLATE.out_str += "u"
            if i == "У":
                TRANSLATE.out_str += "U"
            if i == "ф":
                TRANSLATE.out_str += "f"
            if i == "Ф":
                TRANSLATE.out_str += "F"
            if i == "х":
                TRANSLATE.out_str += ">"
            if i == "Х":
                TRANSLATE.out_str += "%"
            if i == "ч":
                TRANSLATE.out_str += "<"
            if i == "Ч":
                TRANSLATE.out_str += "^"
            if i == "ц":
                TRANSLATE.out_str += "c"
            if i == "Ц":
                TRANSLATE.out_str += "C"
            if i == "ш":
                TRANSLATE.out_str += "sh"
            if i == "Ш":
                TRANSLATE.out_str += "Sh"
            if i == "щ":
                TRANSLATE.out_str += "sh`"
            if i == "Щ":
                TRANSLATE.out_str += "Sh`"
            if i == "ъ":
                TRANSLATE.out_str += "~"
            if i == "ы":
                TRANSLATE.out_str += "i"

            if i == "й":
                TRANSLATE.out_str += "}"
            if i == "Й":
                TRANSLATE.out_str += "{"

            if i == "ь":
                TRANSLATE.out_str += "`"
            if i == "э":
                TRANSLATE.out_str += "e"
            if i == "Э":
                TRANSLATE.out_str += "E"
            if i == "ю":
                TRANSLATE.out_str += "yu"
            if i == "Ю":
                TRANSLATE.out_str += "Yu"
            if i == "я":
                TRANSLATE.out_str += "ya"
            if i == "Я":
                TRANSLATE.out_str += "Ya"
        print("     TRANSLATE.into_str: ", TRANSLATE.into_str)
        print("     TRANSLATE.out_str: ", TRANSLATE.out_str)

    def eng_in_rus():
        counter = 0
        print("Translating from EN to RU:")
        TRANSLATE.into_str += " "
        TRANSLATE.into_str += " "
        while True:
            try:
                # if TRANSLATE.into_str[counter] == "":
                #     TRANSLATE.out_str += ""
                if TRANSLATE.into_str[counter] == " ":
                    TRANSLATE.out_str += " "
                if TRANSLATE.into_str[counter] == "№":
                    TRANSLATE.out_str += "№"
                if TRANSLATE.into_str[counter] == ",":
                    TRANSLATE.out_str += ","
                if TRANSLATE.into_str[counter] == ":":
                    TRANSLATE.out_str += ":"
                if TRANSLATE.into_str[counter] == "/":
                    TRANSLATE.out_str += "/"
                if TRANSLATE.into_str[counter] == ".":
                    TRANSLATE.out_str += "."
                if TRANSLATE.into_str[counter] == "'":
                    TRANSLATE.out_str += "'"
                if TRANSLATE.into_str[counter] == '"':
                    TRANSLATE.out_str += '"'
                if TRANSLATE.into_str[counter] == "-":
                    TRANSLATE.out_str += "-"
                if TRANSLATE.into_str[counter] == "_":
                    TRANSLATE.out_str += "_"
                if TRANSLATE.into_str[counter] == "+":
                    TRANSLATE.out_str += "+"
                if TRANSLATE.into_str[counter] == "=":
                    TRANSLATE.out_str += "="
                if TRANSLATE.into_str[counter] == "(":
                    TRANSLATE.out_str += "("
                if TRANSLATE.into_str[counter] == ")":
                    TRANSLATE.out_str += ")"
                if TRANSLATE.into_str[counter] == "#":
                    TRANSLATE.out_str += "#"
                if TRANSLATE.into_str[counter] == "%":
                    TRANSLATE.out_str += "%"
                if TRANSLATE.into_str[counter] == "1":
                    TRANSLATE.out_str += "1"
                if TRANSLATE.into_str[counter] == "2":
                    TRANSLATE.out_str += "2"
                if TRANSLATE.into_str[counter] == "3":
                    TRANSLATE.out_str += "3"
                if TRANSLATE.into_str[counter] == "4":
                    TRANSLATE.out_str += "4"
                if TRANSLATE.into_str[counter] == "5":
                    TRANSLATE.out_str += "5"
                if TRANSLATE.into_str[counter] == "6":
                    TRANSLATE.out_str += "6"
                if TRANSLATE.into_str[counter] == "7":
                    TRANSLATE.out_str += "7"
                if TRANSLATE.into_str[counter] == "8":
                    TRANSLATE.out_str += "8"
                if TRANSLATE.into_str[counter] == "9":
                    TRANSLATE.out_str += "9"
                if TRANSLATE.into_str[counter] == "0":
                    TRANSLATE.out_str += "0"

                if TRANSLATE.into_str[counter] == "a":
                    TRANSLATE.out_str += "а"
                if TRANSLATE.into_str[counter] == "A":
                    TRANSLATE.out_str += "А"
                if TRANSLATE.into_str[counter] == "b":
                    TRANSLATE.out_str += "б"
                if TRANSLATE.into_str[counter] == "B":
                    TRANSLATE.out_str += "Б"
                if TRANSLATE.into_str[counter] == "v":
                    TRANSLATE.out_str += "в"
                if TRANSLATE.into_str[counter] == "V":
                    TRANSLATE.out_str += "В"
                if TRANSLATE.into_str[counter] == "g":
                    TRANSLATE.out_str += "г"
                if TRANSLATE.into_str[counter] == "G":
                    TRANSLATE.out_str += "Г"
                if TRANSLATE.into_str[counter] == "d":
                    TRANSLATE.out_str += "д"
                if TRANSLATE.into_str[counter] == "D":
                    TRANSLATE.out_str += "Д"

                if TRANSLATE.into_str[counter] == "j":
                    TRANSLATE.out_str += "ж"
                if TRANSLATE.into_str[counter] == "J":
                    TRANSLATE.out_str += "Ж"
                if TRANSLATE.into_str[counter] == "z":
                    TRANSLATE.out_str += "з"
                if TRANSLATE.into_str[counter] == "Z":
                    TRANSLATE.out_str += "З"

                if TRANSLATE.into_str[counter] == "k":
                    TRANSLATE.out_str += "к"
                if TRANSLATE.into_str[counter] == "K":
                    TRANSLATE.out_str += "К"
                if TRANSLATE.into_str[counter] == "l":
                    TRANSLATE.out_str += "л"
                if TRANSLATE.into_str[counter] == "L":
                    TRANSLATE.out_str += "Л"
                if TRANSLATE.into_str[counter] == "m":
                    TRANSLATE.out_str += "м"
                if TRANSLATE.into_str[counter] == "M":
                    TRANSLATE.out_str += "М"

                if TRANSLATE.into_str[counter] == "^":
                    TRANSLATE.out_str += "Ч"
                if TRANSLATE.into_str[counter] == "<":
                    TRANSLATE.out_str += "ч"
                if TRANSLATE.into_str[counter] == "n":
                    TRANSLATE.out_str += "н"
                if TRANSLATE.into_str[counter] == "N":
                    TRANSLATE.out_str += "Н"
                if TRANSLATE.into_str[counter] == "o":
                    TRANSLATE.out_str += "о"
                if TRANSLATE.into_str[counter] == "O":
                    TRANSLATE.out_str += "О"
                if TRANSLATE.into_str[counter] == "p":
                    TRANSLATE.out_str += "п"
                if TRANSLATE.into_str[counter] == "P":
                    TRANSLATE.out_str += "П"
                if TRANSLATE.into_str[counter] == "r":
                    TRANSLATE.out_str += "р"
                if TRANSLATE.into_str[counter] == "R":
                    TRANSLATE.out_str += "Р"

                if TRANSLATE.into_str[counter] == "t":
                    TRANSLATE.out_str += "т"
                if TRANSLATE.into_str[counter] == "T":
                    TRANSLATE.out_str += "Т"
                if TRANSLATE.into_str[counter] == "u":
                    TRANSLATE.out_str += "у"
                if TRANSLATE.into_str[counter] == "U":
                    TRANSLATE.out_str += "У"
                if TRANSLATE.into_str[counter] == "f":
                    TRANSLATE.out_str += "ф"
                if TRANSLATE.into_str[counter] == "F":
                    TRANSLATE.out_str += "Ф"
                if TRANSLATE.into_str[counter] == ">":
                    TRANSLATE.out_str += "х"
                if TRANSLATE.into_str[counter] == "%":
                    TRANSLATE.out_str += "Х"


                if TRANSLATE.into_str[counter] == "i":
                    TRANSLATE.out_str += "ы"
                if TRANSLATE.into_str[counter] == "~":
                    TRANSLATE.out_str += "ъ"
                if TRANSLATE.into_str[counter] == "`":
                    TRANSLATE.out_str += "ь"
                if TRANSLATE.into_str[counter] == "}":
                    TRANSLATE.out_str += "й"
                if TRANSLATE.into_str[counter] == "{":
                    TRANSLATE.out_str += "Й"

                if TRANSLATE.into_str[counter] == "e":
                    TRANSLATE.out_str += ""
                if TRANSLATE.into_str[counter] == "E":
                    TRANSLATE.out_str += ""

                if TRANSLATE.into_str[counter] == "y":
                    if TRANSLATE.into_str[counter + 1] == "e":
                        TRANSLATE.out_str += "е"
                        counter += 1
                    else:
                        if TRANSLATE.into_str[counter + 1] == "o":
                            TRANSLATE.out_str += "ё"
                            counter += 1
                        else:
                            if TRANSLATE.into_str[counter + 1] == "i":
                                TRANSLATE.out_str += "и"
                                counter += 1
                            else:
                                if TRANSLATE.into_str[counter + 1] == "u":
                                    TRANSLATE.out_str += "ю"
                                    counter += 1
                                else:
                                    if TRANSLATE.into_str[counter + 1] == "a":
                                        TRANSLATE.out_str += "я"
                                        counter += 1
                                    # else:
                                    #     TRANSLATE.out_str += "й"

                if TRANSLATE.into_str[counter] == "Y":
                    if TRANSLATE.into_str[counter + 1] == "u":
                        TRANSLATE.out_str += "Ю"
                        counter += 1
                    else:
                        if TRANSLATE.into_str[counter + 1] == "i":
                            TRANSLATE.out_str += "И"
                            counter += 1
                        else:
                            if TRANSLATE.into_str[counter + 1] == "o":
                                TRANSLATE.out_str += "Ё"
                                counter += 1
                            else:
                                if TRANSLATE.into_str[counter + 1] == "e":
                                    TRANSLATE.out_str += "Е"
                                    counter += 1
                                else:
                                    if TRANSLATE.into_str[counter + 1] == "a":
                                        TRANSLATE.out_str += "Я"
                                        counter += 1
                                    # else:
                                    #     TRANSLATE.out_str += "Й"

                if TRANSLATE.into_str[counter] == "s" and TRANSLATE.into_str[counter+1] != "h":
                    TRANSLATE.out_str += "с"
                else:
                    if TRANSLATE.into_str[counter] == "s" and TRANSLATE.into_str[counter+1] == "h" and TRANSLATE.into_str[counter+2] == "`":
                        TRANSLATE.out_str += "щ"
                        counter += 1
                        counter += 1
                    if TRANSLATE.into_str[counter] == "s" and TRANSLATE.into_str[counter + 1] == "h" and TRANSLATE.into_str[counter + 2] != "`":
                        TRANSLATE.out_str += "ш"
                        counter += 1

                if TRANSLATE.into_str[counter] == "S" and TRANSLATE.into_str[counter+1] != "h":
                    TRANSLATE.out_str += "С"
                else:
                    if TRANSLATE.into_str[counter] == "S" and TRANSLATE.into_str[counter+1] == "h" and TRANSLATE.into_str[counter+2] == "`":
                        TRANSLATE.out_str += "Щ"
                        counter += 1
                        counter += 1
                    if TRANSLATE.into_str[counter] == "S" and TRANSLATE.into_str[counter+1] == "h" and TRANSLATE.into_str[counter+2] != "`":
                        TRANSLATE.out_str += "Ш"
                        counter += 1

                # or TRANSLATE.into_str[counter] == "Y":
            except:
                print("break")
                break
            counter += 1

        print("     TRANSLATE.into_str: ", TRANSLATE.into_str)
        print("     TRANSLATE.out_str: ", TRANSLATE.out_str)
