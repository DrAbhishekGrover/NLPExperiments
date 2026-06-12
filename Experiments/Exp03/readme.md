This experiment demonstrates an implementation of word2vec (skip-gram) algorithm on a text file.
1) Read text8.txt file and extract all words in a list
2) Create a vocabalary and two dictionaries for indexing the vocabalary.
3) Use following hyperparameters for the algorithm: Embedding dimension=100; Window length=2; neg_samples=5; learning rate=0.025; Number of epochs=1
4) Evaluate probability of each word in the list. This will be used for randomly sampling negative samples for skip-gram algorithm
5) Randomly initialize W and C matrices. W: Embedding of a word if it is target; C: Embedding of word if it is in context; In the end either W is taken as embedding matrix or (W+C)/2 can be taken as embedding matrix.
6) Iterate through each word in the text. Step 7 is implemented for each word in sequence.
7) Create positive and and negative samples for each target word. Update W and C matrices using skip-gram updation equations.
8) At the end, W is taken as the embedding matrix
9) To test the utility of algorithm: Input a word and print 5 words which have embeddings similar to the input word. It would be observed that the output words are similar to the input word. The results improve if the algorithm is trained on larger dataset.
10) Exercise 1: Change hyperparameters in step 3 and observe results.
11) Exercise 2: Change text file and observe the learning ability of the algorithm.
12) Exercise 3: Algorithm is slow as it is going through the complete file word by word. Training on large text file takes time. Try to improve speed of the algorithm by changing the for loop logic. 
