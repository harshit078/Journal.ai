import torch as pt
import pytorch_lightning as pl
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
import pandas as pd
import torch.distributed

try:
    from torch.hub import load_state_dict_from_url
except ImportError:
    from torch.utils.model_zoo import load_url as load_state_dict_from_url

model_urls = dict(
    params='https://github.com/better-me-team/better.me/releases/download/model_params/model.pt',
)


class SuicideDataset():
    def __init__(self, dataset):
        self.dataset = dataset

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return {'input_ids': self.dataset.iloc[idx][0], 'label': self.dataset.iloc[idx][1]}


class SuicideDetectionClassifier(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = BertForSequenceClassification.from_pretrained('bert-base-cased')
        self.loss = pt.nn.CrossEntropyLoss()

    def forward(self, x):
        mask = (x != 0).float()
        logits = self.model(x, mask)['logits']
        return logits

    def training_step(self, batch, batch_idx):
        y, x = batch['label'], batch['input_ids']
        y_hat = self.forward(x)
        loss = self.loss(y_hat, y)
        return {'loss': loss, 'log': {'train_loss': loss}}


    def configure_optimizers(self):
        optimizer = pt.optim.Adam(self.parameters(), lr=1e-5)
        return optimizer


def load_model(path=model_urls["params"], progress=True):
    model = pt.load("./model.pt", map_location=pt.device("cpu"))
    return model


def pred(text: str, model):
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    x = tokenizer.encode(text,
                         max_length=256,
                         return_tensors='pt',
                         padding='max_length',
                         truncation=True)
    return np.argmax(pt.nn.Softmax()(model(x)).view(-1).detach().numpy())
