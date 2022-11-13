import pandas as pd
import numpy as np
from bertopic import BERTopic
import PyPDF2
import os
import nltk
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))

model = BERTopic(verbose=True)


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


def generate_topic_json(lesson_name):
    chapter_list = os.listdir('data/' + lesson_name)

    json_data = '[{"name": "' + lesson_name + '","type": "directory","children": ['

    for chapter in chapter_list:

        docs = []
        pdfContent = str(getPDFContent('data/' + lesson_name + '/' + chapter).encode("ascii", "ignore")).split('.')
        for line in pdfContent:
            docs.append(line.strip())

        topics, probabilities = model.fit_transform(docs)
        model.get_topic_freq().head(11)
        # model.visualize_topics()
        # model.visualize_barchart()
        # model.visualize_heatmap()

        topics_list = model.get_topic(0)
        # here need to remove stop words

        if chapter == chapter_list[-1]:

            json_data += '{ "name": "' + chapter.replace('.pdf', '') + '","type": "directory","children": ['
            temp_topic_list = []
            for topic in topics_list:
                if topic[0].lower() not in stops:
                    temp_topic_list.append(topic[0])

            for i, topic in enumerate(temp_topic_list):
                if i == len(temp_topic_list) - 1:
                    json_data += '{"name": "' + topic + '","type": "file"}'
                else:
                    json_data += '{"name": "' + topic + '","type": "file"},'

            json_data += ']}'
        else:
            json_data += '{ "name": "' + chapter.replace('.pdf', '') + '","type": "directory","children": ['
            temp_topic_list = []
            for topic in topics_list:
                if topic[0].lower() not in stops:
                    temp_topic_list.append(topic[0])
            for i, topic in enumerate(temp_topic_list):
                if i == len(temp_topic_list) - 1:
                    json_data += '{"name": "' + topic + '","type": "file"}'
                else:
                    json_data += '{"name": "' + topic + '","type": "file"},'

            json_data += ']},'

    json_data += ']}]'

    return json_data


print(generate_topic_json('lesson_04'))

# [('the', 0.12874668719226806), ('photosynthesis', 0.09196043279178902), ('is', 0.0909004394079779), ('of', 0.08156054895974803), ('for', 0.08156054895974803), ('in', 0.079787765345108), ('and', 0.07012387848658445), ('to', 0.06097215733870256), ('leaf', 0.058216785242571636), ('water', 0.05394992159451954)]
