import nltk 
from nltk.stem.porter import PorterStemmer
from torch.utils.data import Dataset,DataLoader
import torch.nn as nn
import json
from Features.Extra import DownloadYtVideos
import torch
import numpy as np 
import random
from Features.Open import OpenExe
from Features.Close import CloseExe
from Features.Extra import PlayOnYt
from Body.Speak import Speak
from Body.Listen import MicExecution as TakeCommand
# from Whatsapp import WhatsappSender

def TrainTasks():

    class NeuralNet(nn.Module):

        def __init__(self,input_size,hidden_size,num_classes):
            super(NeuralNet,self).__init__()
            self.l1 = nn.Linear(input_size,hidden_size)
            self.l2 = nn.Linear(hidden_size,hidden_size)
            self.l3 = nn.Linear(hidden_size,num_classes)
            self.relu = nn.ReLU()

        def forward(self,x):
            out = self.l1(x)
            out = self.relu(out)
            out = self.l2(out)
            out = self.relu(out)
            out = self.l3(out)
            return out

    Stemmer = PorterStemmer()

    def tokenize(sentence):
        return nltk.word_tokenize(sentence)

    def stem(word):
        return Stemmer.stem(word.lower())

    def bag_of_words(tokenized_sentence,words):
        sentence_word = [stem(word) for word in tokenized_sentence]
        bag = np.zeros(len(words),dtype=np.float32)

        for idx , w in enumerate(words):
            if w in sentence_word:
                bag[idx] = 1

        return bag

    with open("Data\\Tasks.json",'r') as f:
        intents = json.load(f)

    all_words = []
    tags = []
    xy = []

    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)

        for pattern in intent['patterns']:
            w = tokenize(pattern)
            all_words.extend(w)
            xy.append((w,tag))

    ignore_words = [',','?','/','.','!']
    all_words = [stem(w) for w in all_words if w not in ignore_words]
    all_words = sorted(set(all_words))
    tags = sorted(set(tags))

    x_train = []
    y_train = []

    for (pattern_sentence,tag) in xy:
        bag = bag_of_words(pattern_sentence,all_words)
        x_train.append(bag)

        label = tags.index(tag)
        y_train.append(label)

    x_train = np.array(x_train)
    y_train = np.array(y_train)

    num_epochs = 1000
    batch_size = 8
    learning_rate = 0.001
    input_size = len(x_train[0])
    hidden_size = 8
    output_size = len(tags)

    print(">> Training The TasksExecution :- Working ")

    class ChatDataset(Dataset):

        def __init__(self):
            self.n_samples = len(x_train)
            self.x_data = x_train
            self.y_data = y_train

        def __getitem__(self,index):
            return self.x_data[index],self.y_data[index]

        def __len__(self):
            return self.n_samples
        
    dataset = ChatDataset()

    train_loader = DataLoader(dataset=dataset,
                                batch_size=batch_size,
                                shuffle=True,
                                num_workers=0)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = NeuralNet(input_size,hidden_size,output_size).to(device=device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)

    for epoch in range(num_epochs):
        for (words,labels)  in train_loader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)
            outputs = model(words)
            loss = criterion(outputs,labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch+1) % 100 ==0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    print(f'Final Loss : {loss.item():.4f}')

    data = {
    "model_state":model.state_dict(),
    "input_size":input_size,
    "hidden_size":hidden_size,
    "output_size":output_size,
    "all_words":all_words,
    "tags":tags
    }

    FILE = "DataBase\\Tasks.pth"
    torch.save(data,FILE)

    print(f"Training Complete, File Saved To {FILE}")
    print("             ")

TrainTasks()

def TasksExecutor(query):

    class NeuralNet(nn.Module):

        def __init__(self,input_size,hidden_size,num_classes):
            super(NeuralNet,self).__init__()
            self.l1 = nn.Linear(input_size,hidden_size)
            self.l2 = nn.Linear(hidden_size,hidden_size)
            self.l3 = nn.Linear(hidden_size,num_classes)
            self.relu = nn.ReLU()

        def forward(self,x):
            out = self.l1(x)
            out = self.relu(out)
            out = self.l2(out)
            out = self.relu(out)
            out = self.l3(out)
            return out

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('Data\\Tasks.json','r') as json_data:
        intents = json.load(json_data)

    FILE = "DataBase\\Tasks.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = NeuralNet(input_size,hidden_size,output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    Stemmer = PorterStemmer()

    def tokenize(sentence):
        return nltk.word_tokenize(sentence)

    def stem(word):
        return Stemmer.stem(word.lower())

    def bag_of_words(tokenized_sentence,words):
        sentence_word = [stem(word) for word in tokenized_sentence]
        bag = np.zeros(len(words),dtype=np.float32)

        for idx , w in enumerate(words):
            if w in sentence_word:
                bag[idx] = 1

        return bag

    sentence = str(query)

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:

        for intent in intents['intents']:

            if tag == intent["tag"]:

                reply = random.choice(intent["responses"])
                
                return reply

def make_api_call():
    # Make API call
    # Check for API usage limit
    # If limit is reached, add a delay and try again
    # If limit is still reached, raise an exception

# Main program loop

    while True:
        try:
            # Make API call
            make_api_call()
            
            # If API call is successful, break out of the loop
            break
        except Exception as e:
            # If API limit is reached, restart the program after a delay
            print(f"Error: {e}")
            print("Restarting program...")
            

def MainTaskExecution(Query):
    Task = str(Query).lower()
    TaskNew = str(Query).lower()
    ReturnData = TasksExecutor(Task)

    try:
        if "open" in ReturnData:
            Value = OpenExe(TaskNew)
            return Value
        

        elif "play on youtube" in ReturnData:
            Value = PlayOnYt(TaskNew)
            return Value

        elif "close" in ReturnData:
            Value = CloseExe(TaskNew)
            return Value

        
        # elif "whatsapp" in ReturnData:
        #     Namen = str(TaskNew).replace("send ","")
        #     Namen = str(Namen).replace("whatsapp ","")
        #     Namen = str(Namen).replace("message ","")
        #     Namen = str(Namen).replace("to ","")
        #     WhatsappSender(Namen)
        #     return True
    except:
        pass
    