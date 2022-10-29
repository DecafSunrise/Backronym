from fastapi import FastAPI
import pandas as pd
import random
df = pd.read_csv(r"words.csv")
df['word'] = df['word'].astype(str)

app = FastAPI()


@app.get("/backronym/{text}")
async def backronym(text):
    outlist = []
    for x in text.lower():
        outlist.append(random.choice(df[df['word'].str.startswith(x)]['word'].tolist()).title())

    return {text.upper(): ' '.join(outlist)}

@app.get("/")
async def root():
    return {"message": "Hello World"}