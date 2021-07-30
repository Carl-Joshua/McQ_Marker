import PyPDF2

with open("Practice MCQ Question - Midterm Test #2 answer.pdf", 'rb') as f:
    pdfReader = PyPDF2.PdfFileReader(f)
    num_page = pdfReader.numPages

    # text = pdfReader.getPage(0).extractText()
    # print(text[text.index("Answer: ", text.index(str(2) + '.')) + len("Answer: ")+1])

    full_text = []
    for i in range(num_page):
        full_text.append(pdfReader.getPage(i).extractText())
    full_text = ''.join(full_text)
    full_text = full_text.replace("\n", "")
chapter = input("Chapter: ")
with open("Chapter"+str(chapter)+"_as.txt", 'r') as f:
    total_number = len(f.readlines())

number = 1
index_of_chapter = full_text.index("Ch " + str(chapter))
res = []
go = True
while go:
    index_of_ans = full_text.index("Answer: ", full_text.index(" " + str(number) + ". ", index_of_chapter))
    res.append(str(number) + ". " + full_text[index_of_ans + len("Answer: ") + 1] + "\n")
    if number >= total_number:
        go = False
    number += 1

with open("Chapter" + str(chapter) + "_ms.txt", 'w') as f:
    for line in res:
        f.write(line)

