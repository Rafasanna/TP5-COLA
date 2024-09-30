# HEAP
# 5. hundir(montículo, índice). Hunde el dato almacenado en el montículo desde el índice indicado
# hasta que cumpla la propiedad de orden
def hundir(self, i):
        n = len(self.heap)
        while i * 2 <= n - 1:
            j = self.heap[i * 2]
            if i * 2 + 1 < n and self.heap[i * 2 + 1] > j:
                j = self.heap[i * 2 + 1]
            if self.heap[i] < j:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]