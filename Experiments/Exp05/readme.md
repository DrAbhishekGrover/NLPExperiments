This experiment demonstrates the utiltiy of Transformers based models for Next token Prediction. 
The algorithm is trained on Wikitext dataset. 
Once trained, if we give an input sentence then the algorithm would try to predict the next token.

1. Import necessary libraries: torch and torch.nn: For using PyTorch to build deep learning models; datasets: To use datasets available on HuggingFace; tokenizers: For generating tokens from text; torch.utils.data: To convert dataset into format compatible with Pytorch model training;
2. Choose hyperparameters. Vocabalary size can be assumed to be 10000. Batch size as 32. Context window size as 32. Embedding dimension as 128. Number of transformer layers is 6. Number of attention heads in each layer is 8. The number of epochs can be taken to be 3.
3. Load Wikitext dataset and store each sentence in a list.
4. Use BPE tokenizer to tokenize all sentences in above list. Store the generated token in a single list all_tokens. The dataset for model training is generated from this list.
5. Create a class PositionalEncoding. This is implemented so that the model understands position of tokens. A specific number is added to numeric representation of token. This number is position dependent. Sinusoidal encoding is used.
6. Create a class TextDataset. This class takes all_tokens list and generates training samples for transformer model. Transformer is a sequence-to- sequence model. It input consist of N tokens in sequence (i:i+N). The output is also a sequence of N tokens (i+1:i+N+1). During training each transformer stream is trying to predict next token. During inference the output of last unit is taken as the predicted token.
7. Create a class mytransformer which inherits functions from nn.Module. It has a constructor and forward function. The constructor define various layers of the model. The forward function decribes the order in which operations are implemented on the input variable. The architecture consists of an embedding layer, positional encoding and 6 transformer layers in a single stream.
8. The loss function to be used is CrossEntropyLoss and optimizer to be used is Adam optimizer with a learning rate of 0.001. Next token prediction is a causal processing application where the past tokens are used to generate next token. Causal Masking is used to ensure that transformer gets only past inputs during training.
9. The training loop is as follows. Dataset generated in step 5 consists of batches. Each batch has 32 samples where input is sequence and output is also a sequence. The input is given to the model. Weights are updated using backpropagation, where the output sequence is taken as true label.
10. It is always a good practice to save model weights (using torch.save(mymod.state_dict(),"filename.pth") after training.
11. Inference stage: Input a sentence, pass it to the model. It will give an output sequence. Print the last token of the sequence. This the output.
12. Exercise: Try giving various strings to the input. The quality/correctness of the output may vary.  
