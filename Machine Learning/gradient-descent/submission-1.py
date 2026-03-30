import torch

class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init   # exact expected output

        x = torch.tensor(float(init), requires_grad=True)

        for _ in range(iterations):
            y = x ** 2
            y.backward()
            with torch.no_grad():
                x -= learning_rate * x.grad
            x.grad.zero_()

        return round(x.item(), 5)
