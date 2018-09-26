# encoding=utf-8
import json

from torch.utils.data import Dataset


class ChatbotDataset(Dataset):
    def __init__(self, split):
        self.split = split
        assert self.split in {'train', 'valid'}

        print('loading {} samples'.format(split))
        samples_path = 'data/samples.json'
        self.samples = json.load(open(samples_path, 'r'))

        if split == 'train':
            self.samples = self.samples[:100000]
        else:
            self.samples = self.samples[:100000]

        self.dataset_size = len(self.samples)

    def __getitem__(self, i):
        sample = self.samples[i]
        return sample['input'], sample['output']

    def __len__(self):
        return self.dataset_size
