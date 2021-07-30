import PyPDF2

with open("Practice MCQ Question - Midterm Test #1 answer.pdf", 'rb') as f:
    pdfReader = PyPDF2.PdfFileReader(f)
    num_page = pdfReader.numPages

    text = pdfReader.getPage(0).extractText()
    print(text[text.index("Answer: ", text.index(str(2) + '.')) + len("Answer: ")+1])

    full_text = []
    for i in range(num_page):
        full_text.append(pdfReader.getPage(i).extractText())
    full_text = ''.join(full_text)
    print(len(full_text))

    ms = []
    missing_number = [74, 97, 111, 115, 132, 139]


    current_number = 1
    counter = 0
    while current_number <= 140:
        if current_number not in missing_number:
            ms.append(str(current_number) + '. ' + full_text[full_text.index("Answer: ", full_text.index(str(current_number) + '.')) + len("Answer: ")+1] + '\n')
        else:
            ms.append(str(missing_number[counter]) + '. NaN\n')
            counter += 1
        current_number += 1
        # print(current_number)
    print(ms)


    with open("marking_scheme1.txt", 'w') as m:
        m.write("test1\n")
        for i in range(len(ms)):
            m.write(ms[i])
