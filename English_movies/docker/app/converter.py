import re
import pandas as pd
import pysrt
import unicodedata
from bs4 import BeautifulSoup
import spacy





def level_assess(df,file):
    with open('./levels/A1.txt') as lvla1:
        with open('./levels/A2.txt') as lvla2:
            with open('./levels/B1.txt')as lvlb1:
                with open('./levels/B2.txt') as lvlb2:
                    with open('./levels/C1.txt') as lvlc1:
                        with open('./levels/C2.txt') as lvlc2:

                            A1 = lvla1.read()
                            A2 = lvla2.read()
                            B1 = lvlb1.read()
                            B2 = lvlb2.read()
                            C1 = lvlc1.read()
                            C2 = lvlc2.read()
                            levels_txt = {'a1':A1,
                                    'a2':A2,
                                    'b1':B1,
                                    'b2':B2,
                                    'c1':C1,
                                    'c2':C2}
                            sub = file.split()
                            df['uniq'] = len(set(sub))
                            lev_count = {'a1':0,
                                        'a2':0,
                                        'b1':0,
                                        'b2':0,
                                        'c1':0,
                                        'c2':0}
                            for word in sub:
                                for i in lev_count.keys():
                                    if word in levels_txt[i]: 
                                        lev_count[i] += 1
                            for k in lev_count.keys():
                                df[k] = lev_count[k]
                            lev_count = {'a1':0,
                                        'a2':0,
                                        'b1':0,
                                        'b2':0,
                                        'c1':0,
                                        'c2':0}                            
                            for word in set(sub):
                                for i in lev_count.keys():
                                    if word in levels_txt[i]: 
                                        lev_count[i] += 1
                            for k in lev_count.keys():
                                df[f'{k}_uniq'] = lev_count[k]                            
                            return (df)



def convert_srt_to_txt(file):
    df = pd.DataFrame(index= [0], columns=['total_time', 'total_words', 'raito', 'uniq', 'a1', 'a2', 'b1', 'b2',
       'c1', 'c2'])
    # создаем файл txt с названием фильма и открываем субтитры
    movie = pysrt.from_string(file)
    total_time = 0
    total_words = 0
    string = ''
    # проходимся по каждой строке субтитров и обрабатываем ее
    for i in range(len(movie)):
        
        # приводим все в нормальную кодировку
        movie_str = unicodedata.normalize('NFKD', movie[i].text).encode('ASCII', 'ignore').decode('utf-8', 'ignore')
        
        # в некоторых субтитрах есть имена авторов и сайты источники, нам они не нужны
        try:
            re.search(r"\w{3}\..*\.\w{3}", movie_str)[0]
            continue
        except:
            next
        
        # убираем не обычные символы
        movie_str = re.sub(r'[♪]','', movie_str)
        
        # убироаем html 
        movie_str = BeautifulSoup(movie_str, "html.parser").text

        # лишние пробелы и преносы строк
        movie_str = re.sub(r'\s',' ',movie_str)
        movie_str = re.sub(r'{.*?}|\(.*?\)|[,.!?"]|- ',' ', movie_str)
        movie_str = re.sub(r'','',movie_str)
        movie_str = re.sub(r'-',' ',movie_str)
        if movie_str == "": continue
        if movie_str[0] == " ": movie_str = movie_str[1:]
        movie_str = movie_str.lower()

        # подсчет слов и затраченого времени на один субтитр
        count_words = len(movie_str.split())
        duration = movie[i].duration.to_time()
        duration = duration.isoformat(timespec='milliseconds')
        duration = duration.split(':')
        duration = (int(duration[0])*60+int(duration[1]))*60 + float(duration[2]) + 0.001
    
        # записываем итоговую строку и информацию по ней
        string += f'{movie_str} '
        total_time += duration
        total_words += count_words
    
    # записываем итоговые цифры и закрываем файл
    df['total_time'] = total_time
    df['total_words'] = total_words
    df['raito'] = total_words/total_time
    string = re.sub(r'\s+',' ',string)
    return (level_assess(df, convert_to_lemm(string)))




def convert_to_lemm (text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    lemm = ''
    for token in doc:
        if token.is_stop: continue
        lemm += f'{token.lemma_} '
    return (lemm)
