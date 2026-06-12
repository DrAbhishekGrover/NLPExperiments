import numpy as np
import random
from collections import Counter

text=open("text8.txt").read()
text=text.split()
#text="we shall look into this matter the king and queen will be joining shortly"
#print(text[0:10])
text=text[0:100000]

vocab=list(set(text))
word2idx={w:i for i, w in enumerate(vocab)}
idx2word={i:w for w, i in word2idx.items()}
V=len(vocab)

dim=100
window=2
neg_samples=5
lr=0.025
epochs=1

freq=Counter(text)
p=np.array([freq[w] for w in vocab])
p=p**0.75
p=p/np.sum(p)

#print(len(p))
#print(V)

W=np.random.randn(V,dim)*0.01
C=np.random.randn(V,dim)*0.01

def sigmoid(z): return(1/(1+np.exp(-z)))

for _ in range(epochs):
    for i,word in enumerate(text):
        w=word2idx[word]
        context_ids=[word2idx[text[i+j]] for j in range(-window,window+1) if j!=0 and i+j>=0 and i+j<len(text)]
        forbidden=set(context_ids+[w])
        for j in range(-window,window+1):
            if j==0 or i+j<0 or i+j>=len(text):continue
            c=word2idx[text[i+j]]

            #positive samples
            score=sigmoid(np.dot(W[w],C[c]))
            scale=lr*(score-1)
            w_old = W[w].copy()
            W[w] -= scale * C[c]
            C[c] -= scale * w_old

            #negative samples
            neg=[]
            while(len(neg)<neg_samples):
                n=np.random.choice(V,p=p)
                if n not in forbidden:
                    neg.append(n)
            for n in neg:
                score=sigmoid(np.dot(W[w],C[n]))
                scale=lr*(score)
                w_old = W[w].copy()
                W[w] -= scale * C[c]
                C[c] -= scale * w_old

Emb=W
print(np.shape(Emb))

def similar(word,top=5):
    v=Emb[word2idx[word]]
    sims=Emb@v/(np.linalg.norm(Emb,axis=1)*np.linalg.norm(v))#cos b
    ids=np.argsort(-sims)[1:top+1]
    return [idx2word[i] for i in ids]

print(similar("king"))



