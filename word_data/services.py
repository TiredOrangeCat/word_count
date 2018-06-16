import os
import sqlalchemy
from word_data.database import db_session
from word_data.models import Dialogue, Paragraph, Sentence, Word


class WordCount(object):

    def __init__(self):
        pass

    def open_file(self, file):
        with open(file=file, encoding='utf=8') as raw_file:
            db = db_session()
            for chunk in raw_file:
                cs = chunk.split('   ')
                pc = Paragraph(paragraph=cs)
                db.add(pc)
                self.parse_sentence(chunk=cs)
            db.commit()
            # return raw_file

    def parse_file(self, file):
        raw_file = self.open_file(file=file)
        # self.parse_paragraph(file=raw_file)
        # parse_sentence
        # parse_word
        pass

    def parse_paragraph(self, file):

        # not really paragraphs, chunks
        # break apart file by page breaks
        # single sentence "paragraphs" are fine, this is a top level id
        # validate a paragraph is composed of more than one sentence
        # write to db
        pass

    def parse_sentence(self, chunk):
        db = db_session()
        try:
            # cs = chunk.split('. ')
            # p_id = db.query(Paragraph).filter_by(id()).first
            for line in chunk:
                ls = line.split('. ')
                for sent in ls:
                    sl = Sentence(sentence=sent)
                    db.add(sl)
                    self.parse_word(line=sent)
        except AttributeError:
            sl = Sentence(sentence=chunk)
            db.add(sl)
            self.parse_word(line=chunk)
        db.commit()

        # query db for paragraph chunk
        # break apart paragraph by punctuation
        # dialogue parser - speaker should be included

        # regex?
        # write to db
        pass

    def parse_word(self, line):
        db = db_session()
        ws = line.split(' ')
        for word in ws:
            sw = Word(word=word)
            db.add(sw)
        db.commit()
        # query db for sentence lines
        # break apart words


    def dialogue_parser(self, query):
        # if
        pass

    # def word_dict(self):
    #     db = get_db()
    #     line_n = 0
    #     words_l = []
    #     words_s = [] #split words
    #     words_d = {} #display words
    #
    #     #open file
    #     with open('/Users/cmesser/Development/word_data/HRPG.txt', encoding='utf-8') as word_list:
    #         #split lines
    #         for a_line in word_list:
    #             line_n += 1
    #             line_s = words_l.append(a_line.rstrip())
    #             #  split words
    #             for a_word in a_line.split(' '):
    #                 words_s.append(a_word)

    #  isolate words
    # for w_word in words_s:
    #     if w_word not in words_d.keys():
    #         word_data = words_s.count(w_word)
    #         words_d.update({w_word: word_data})
    #     else:
    #         continue

# count as a function
