import streamlit as st
import converter
import pickle
import pandas as pd

st.title('I could assess english level for movie')

st.write('Load your subtitles')

sub = st.file_uploader("",type = 'srt')

m = open('./models/model.pickle', 'rb')
model = pickle.load(m)
m.close()

s = open('./models/scaller.pickle', 'rb')
scaler = pickle.load(s)
s.close()

level_code = {0:'A1',
              1:'A2',
              2:'B1',
              3:'B2',
              4:'C1',
              5:'C2'}

if sub:

    sub_tx = sub.getvalue()
    sub_tx = sub_tx.decode(encoding='cp1252')
    
    result = converter.convert_srt_to_txt(sub_tx)
    level = model.predict(scaler.transform(result.loc[:,'total_time':'c2_uniq']))
    st.write(f'The complexity of the film: {level_code[level[0][0]]}')
    
    st.title(f'Other insteresting information by {sub.name[:-4]}')

    st.write(f'Total numeb of words: {result["total_words"].values[0]}')
    st.write('Distribution of words by levels')
    bar = pd.DataFrame(index=range(5))
    j = 0 
    for i in result.loc[:,'a1':'c2'].columns:
        bar.loc[j,'level'] = i.upper()
        bar.loc[j,'words'] = result[i].values[0]
        j += 1
    st.bar_chart(bar, y='words', x='level')

    st.write('')
    st.write('Distribution of unique words by levels')
    st.write(f'Number of uniq words: {result["uniq"].values[0]}')
    bar = pd.DataFrame(index=range(5))
    j = 0 
    for i in result.loc[:,'a1_uniq':'c2_uniq'].columns:
        bar.loc[j,'level'] = i[:-5].upper()
        bar.loc[j,'words'] = result[i].values[0]
        j += 1
    st.bar_chart(bar, y='words', x='level')
    


