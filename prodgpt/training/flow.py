import torch.nn.functional as F
from accelerate import Accelerator
from metaflow import FlowSpec, Parameter, step
from torch import optim

from .utils import load_model, load_tokenized_dataset, load_tokenizer


class SuperviseFinetuningFlow(FlowSpec):
    num_epochs = Parameter(
        'num_epochs',
        default=1, type=int,
        help='Number of epochs to train for'
    )
    lr = Parameter('lr', default=1e-4, type=float, help='Learning rate')

    @step
    def start(self):
        self.accelerator = Accelerator()
        self.device = self.accelerator.device

        model = load_model()
        optimizer = optim.Adam(model.parameters(), lr=self.lr)
        dataset = load_tokenized_dataset()
        self.model, self.optimizer, self.dataset = self.accelerator.prepare(
            model,
            optimizer,
            dataset
        )
        self.tokenizer = load_tokenizer()
        self.next(self.train)

    @step
    def train(self):
        for epoch in range(self.num_epochs):
            for source, target in self.dataset:
                pred = self.model(source)
                loss = F.cross_entropy(pred, target)

                self.optimizer.zero_grad()
                self.accelerator.backward(loss)
                self.optimizer.step()

        self.next(self.end)

    @step
    def end(self):
        pass
