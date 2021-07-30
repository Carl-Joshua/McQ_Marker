
in_chapter = input("Chapter: ")
if len(in_chapter) != 1:
    in_chapter = in_chapter.split(',')

    scores = []
    for chap in range(len(in_chapter)):
        chapter = in_chapter[chap]
        chapter = chapter.strip()

        with open("Nilaimu_for_chapter" + str(chapter) + ".txt", 'r') as f:
            f_read = f.readlines()
            for i in range(len(f_read)):
                if f_read[i].find("Nilaimu") != -1:
                    scores.append(float(f_read[i].split(' ')[1]))
            print(f_read)

    avg = sum(scores) / len(scores)
    print(avg)
    input()
else:
    # importing txt files
    with open("Chapter" + str(in_chapter) + "_ms.txt", 'r') as f:
        marking_scheme = f.readlines()
        for i in range(len(marking_scheme)):
            marking_scheme[i] = marking_scheme[i].split(". ")[0] + marking_scheme[i].split(". ")[1][0]
            # marking_scheme[i] = marking_scheme[i][0, -2] + marking_scheme[i][-2]
    with open("Chapter" + str(in_chapter) + "_as.txt", 'r') as f:
        answer_sheet = f.readlines()
        for i in range(len(answer_sheet)):
            answer_sheet[i] = answer_sheet[i].split(". ")[0] + answer_sheet[i].split(". ")[1][0]


    # kimochi starts here
    number_of_question = len(marking_scheme)
    tetot = []
    for i in range(number_of_question):
        if answer_sheet[i] == "NaN":
            continue
        if answer_sheet[i] != marking_scheme[i]:
            tetot.append(answer_sheet[i] + " harusnya " + marking_scheme[i][-1] + "\n")

    score = ((number_of_question - len(tetot))/number_of_question) * 100
    if score <= 90:
        tetot.append("Nilaimu " + str(score) + "\nCupu DO sana\n")
    else:
        tetot.append("Nilaimu " + str(score) + "\nBole la...\n")

    with open("Nilaimu_for_chapter" + str(in_chapter) + ".txt", 'w') as f:
        f.write(''.join(tetot))

    print(tetot)
    print(marking_scheme)
    print(answer_sheet)
