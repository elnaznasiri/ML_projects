import hazm
import pandas as pd

file = "D:\Programming\ML_projects\OutputFiles\stage\\3493882.csv"
file1 = "D:\Programming\ML_projects\OutputFiles\stage\\34938821.csv"

SingleChunkData = pd.read_csv(file, chunksize=1)

df = pd.read_csv(file)


def preProcecessing(word):
    normalizer = hazm.Normalizer()
    informalNormalizer = hazm.InformalNormalizer()
    word = normalizer.normalize(word)
    word = normalizer.character_refinement(word)
    word = normalizer.punctuation_spacing(word)
    word = normalizer.affix_spacing(word)
    word = informalNormalizer.split_token_words(word)
    return word

df = df.fillna('')
for i in df['title']:
    i = preProcecessing(i)

df.to_csv(file1, index=False)    
    
    

   