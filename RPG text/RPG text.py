from time import sleep

#extext = "Ok let me execute this... I hope it doesn't crashes. Oh no... OH NO !<pause>Ah it's fine, cool I guess."

with open("C:\\Users\\franc\\Documents\\Github Repos\\Python-things\\RPG text\\SM64 - Watch for Rolling Rocks - 0.5x A Presses (Commentated).txt", "r") as f:
    extext = f.read()


def RPGprint(text, linesize=120, pause_intervals=2):
    char_time = {
        "others": 0.05,
        ".": 0.5,
        "!": 0.5,
        ",": 0.2,
        " ": 0
    }
    #analize string
    sentences = []
    keyword_flag = False
    keyword_record = ""
    keyword_reset = False
    keyword_sentence = ""
    string_record = ""
    for chars in text:

        # recorders
        if (not keyword_flag) and (not chars == "<"):
            string_record += chars

        if keyword_flag:
            keyword_record += chars

        # flags
        if chars == "<":
            keyword_flag = True
            keyword_record = "<"


        # flag ends
        if keyword_flag and keyword_record == "<<": # it wasnt a keyword
            string_record += keyword_record
            keyword_reset = True

        if keyword_flag and chars == ">":
            keyword_sentence = keyword_record
            keyword_reset = True

        # sentences
        if keyword_sentence != "":
            if keyword_sentence == "<pause>":
                sentences.extend([string_record, "<pause>"])
                string_record = ""

        # flag reset
        if keyword_reset:
            keyword_flag = False
            keyword_record = ""
            keyword_reset = False
            keyword_sentence = ""

    sentences.append(string_record)

    upsenten = []
    for senten in sentences:
        stringy = ""
        plsstop = False
        for chars in senten:
            stringy += chars


            if len(stringy) == linesize:
                plsstop = True

            if plsstop and chars == " ":
                upsenten.append(stringy)
                stringy = ""
                plsstop = False

            if stringy == "<pause>":
                upsenten.append(stringy)
                stringy = ""

        upsenten.append(stringy)
    sentences = upsenten

    def add_pauses(inputlist, intervals):
        a = 0 - intervals
        i = 0
        for ele in inputlist:
            if ele == "<pause>":
                a = 0 - intervals
            elif a == 0:
                inputlist.insert(i, "<spause>")
                a = 0 - intervals
            else:
                a += 1
            i += 1
        return inputlist

    def remove_duplicate_pauses(inputlist):
        lastele = ""
        outputlist = []
        for ele in inputlist:
            if not((lastele == "<pause>" or lastele == "<spause>") and (ele == "<spause>" or ele == "<spause>")):
                outputlist.append(ele)
            lastele = ele
        return outputlist

    def remove_empty_strings(inputlist):
        while "" in inputlist:
            inputlist.remove("")
        return inputlist

    def remove_wierd_spaces(inputlist):
        for stringy in inputlist:
            if stringy == "<pause>" or stringy == "<spause>":
                pass
            else:
                while stringy

    sentences = remove_empty_strings(sentences)
    sentences = add_pauses(sentences, pause_intervals)
    sentences = remove_duplicate_pauses(sentences)



    # print string
    def readstring(string):
        stringy = ""
        for chars in string:
            stringy += chars

            print(stringy, end="\r")

            if chars in char_time:
                sleep(char_time[chars])
            else:
                sleep(char_time["others"])
        print()

    for thing in sentences:
        if thing == "<pause>" or thing == "<spause>":
            print("")
            print("Press enter to continue")
            input("")
        else:
            readstring(thing)


#input("Ready?")
print()
RPGprint(extext)
