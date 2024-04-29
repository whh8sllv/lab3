from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort_list(self, unsorted_list):
        pass


class BubbleSort(SortStrategy):
    def sort_list(self, data):
        for i in range(0, len(data) - 1):
            for j in range(0, len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSort(SortStrategy):
    def sort_list(self, data):
        if len(data) < 2:
            return data
        else:
            pivot = data[0]
            less = [i for i in data[1:] if i <= pivot]
            greater = [i for i in data[1:] if i > pivot]
            return self.sort_list(less) + [pivot] + self.sort_list(greater)


class Sorter:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort_list(data)


# Example
if __name__ == '__main__':
    unsorted_list = [-8, 0, 12.12, 1, 14, -1, 12.12]

    bubble = Sorter(BubbleSort())
    quick = Sorter(QuickSort())

    print(f'Unsorted List: {unsorted_list}')
    print()
    print(f'Bubble sort: {bubble.sort_data(unsorted_list.copy())}')
    print(f'Quick sort: {quick.sort_data(unsorted_list.copy())}')