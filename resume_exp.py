import neptune.new as neptune
import argparse
import torch
import os

parser = argparse.ArgumentParser(description="PyTorch CIFAR10 Training")
parser.add_argument("--lr", default=0.1, type=float)
parser.add_argument("--optimizer", default='adamW', type=str)
parser.add_argument("--lambda1", default=1., type=float)
parser.add_argument("--lambda2", default=1., type=float)
parser.add_argument("--lambda3", default=1., type=float)
parser.add_argument("--lambda4", default=1., type=float)
parser.add_argument("--id", default=1., type=float)
args = parser.parse_args()

run = neptune.init(
    project="tutorial-cifar10/CIFAR10",
    api_token=os.environ.get('NEPTUNE_API_TOKEN'),
    run=args.id,
)  # your credentials

# save arguments
for key, value in vars(args).items():
    run['args/'+key] = value

for epoch in range(10):
    run["train/accuracy"].log(1 - 0.9 ** epoch)
    run["train/loss"].log(0.9 ** epoch)

run["eval/test_acc"].log(torch.rand((1,)))

run.stop()