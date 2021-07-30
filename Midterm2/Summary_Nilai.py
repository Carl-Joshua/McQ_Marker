in_chapter = input("Chapter(s) (comma-separated): ")

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

avg = sum(scores)/len(scores)
print(avg)
input()
