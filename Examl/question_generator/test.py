import PyPDF2

def getPDFContent(path):
    content = ""
    num_pages = 10
    # p = file(path, "rb")
    p = open(path, 'rb')
    pdf = PyPDF2.PdfFileReader(p)
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content


def get_json(lesson_name):
    docs = ''
    pdfContent = str(getPDFContent('data/' + lesson_name).encode("ascii", "ignore")).split('.')
    for line in pdfContent:
        docs += docs + ' ' + str(line.strip())

    return docs


print(get_json('Chapter 01.pdf'))
