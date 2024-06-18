import numpy as np
import pandas as pd
import re
df = pd.read_csv('GIT_translate_full_last.csv')

def clean_symbols(text):
    text = text.split(' ')
    result = []
    for i in text:
        if i =='':
            continue
        a = re.findall(r'[a-zA-Zก-๘]', i)
        if ''.join(a).strip() != '':
            result.append(''.join(a).strip())
    return ' '.join(result)
if __name__ == "__main__":
    df['caption'] = df['caption'].str.replace("[ ไม่ได้ใช้0 ]", "")
    df['caption'] = df['caption'].str.replace("[ unused0 ]", "")
    df[df['caption'].str.contains('"')]
    df['caption'] = df['caption'].map(clean_symbols)
    df.to_csv('kdd-14.csv',index=False)