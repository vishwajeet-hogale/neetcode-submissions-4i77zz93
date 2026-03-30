import torch
import torch.nn.functional as F

class Solution:
    def reshape(self, to_reshape):
        M, N = to_reshape.shape
        return torch.reshape(to_reshape, (M * N // 2, 2))

    def average(self, to_avg):
        return torch.mean(to_avg, dim=0)

    def concatenate(self, cat_one, cat_two):
        return torch.cat((cat_one, cat_two), dim=1)

    def get_loss(self, prediction, target):
        loss = F.mse_loss(prediction, target)
        return torch.round(loss, decimals=4)
