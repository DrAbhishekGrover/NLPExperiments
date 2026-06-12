Next token prediction is an important application in Natural Language Processing. 
All chatbots are based on this technique of next token prediction using deep learning model.
This experiment demonstrates the utiltiy of Recurrent Neural Networks for Next token Prediction.
The algorithm is trained on Wikitext dataset.
Once trained, if we give an input sentence then the algorithm would try to predict the next token.

1) Import necessary libraries: torch and torch.nn: For using PyTorch to build deep learning models; datasets: To use datasets available on HuggingFace; tokenizers: For generating tokens from text; torch.utils.data: To convert dataset into format compatible with Pytorch model training;
2) Choose hyperparameters. Vocabalary size can be assumed to be 10000. Batch size as 32. Context window size as 32. Embedding dimension as 128. Hidden state dimension in RNN model can be taken as 128. The number of epochs can be taken to be 3.
3) Load Wikitext dataset and store each sentence in a list.
4) Use BPE tokenizer to tokenize all sentences in above list. Store the generated token in a single list all_tokens. The dataset for model training is generated from this list.
5) Create a class TextDataset. This class takes all_tokens list and generates training samples for RNN model. RNN is a sequence-to- sequence model. It input consist of N tokens in sequence (i:i+N). The output is also a sequence of N tokens (i+1:i+N+1). During training each RNN unit is trying to predict next token. During inference the output of last unit is taken as the predicted token.
6) Create a class myRNN which inherits functions from nn.Module. It has a constructor and forward function. The constructor define various layers of the model. The forward function decribes the order in which operations are implemented on the input variable. The architecture consists of an embedding layer, two LSTM layers followed by fully connected layer.
7) The loss function to be used is CrossEntropyLoss and optimizer to be used is Adam optimizer with a learning rate of 0.001.
8) The training loop is as follows. Dataset generated in step 5 consists of batches. Each batch has 32 samples where input is sequence and output is also a sequence. The input is given to the model. Weights are updated using backpropagation, where the output sequence is taken as true label.
9) It is always a good practice to save model weights (using torch.save(mymod.state_dict(),"filename.pth") after training.
10) Inference stage: Input a sentence, pass it to the model. It will give an output sequence. Print the last token of the sequence. This the output.
11) Exercise 1: Try giving various strings to the input. The quality/correctness of the output may vary.
12) Exercise 2: Vary hyperparameters, plot loss function during training and observe the output.
13) Exercise 3: Replace all LSTM units with basic RNN cell. Compare the outputs.
