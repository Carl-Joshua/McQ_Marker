

# importing txt files
with open("Final_ms.txt", 'r') as f:
    marking_scheme = f.readlines()
    for i in range(len(marking_scheme)):
        marking_scheme[i] = marking_scheme[i].split(". ")[0] + marking_scheme[i].split(". ")[1][0]
        # marking_scheme[i] = marking_scheme[i][0, -2] + marking_scheme[i][-2]
with open("Final_as.txt", 'r') as f:
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

with open("Nilaimu.txt", 'w') as f:
    f.write(''.join(tetot))

print(tetot)
print(marking_scheme)
print(answer_sheet)
