class MinhaLista(list):
    def __sub__(self, outra):
        diferenças = []
        for i in range(len(self)):
            diferenças.append(self[i] - outra[i])
        return diferenças


l1 = MinhaLista([1, 2, 3])
l2 = MinhaLista([5, 4, 3])

print(l1 - l2)
