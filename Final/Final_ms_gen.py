import PyPDF2

with open("Final exam_Practice MCQ answer.pdf", 'rb') as f:
    pdfReader = PyPDF2.PdfFileReader(f)
    num_page = pdfReader.numPages

    # text = pdfReader.getPage(0).extractText()
    # print(text[text.index("Answer: ", text.index(str(2) + '.')) + len("Answer: ")+1])

    full_text = []
    for i in range(num_page):
        full_text.append(pdfReader.getPage(i).extractText())
    full_text = ''.join(full_text)
    full_text = full_text.replace("\n", "")
#chapter = input("Chapter: ")
with open("Final_as.txt", 'r') as f:
    total_number = len(f.readlines())

number = 1
res = []
go = True
while go:
    index_of_ans = full_text.index("Answer: ", full_text.index(" " + str(number) + ". "))
    res.append(str(number) + ". " + full_text[index_of_ans + len("Answer: ") + 1] + "\n")
    if number >= total_number:
        go = False
    number += 1

with open("Final_ms.txt", 'w') as f:
    for line in res:
        f.write(line)
