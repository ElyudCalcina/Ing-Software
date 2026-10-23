class BubbleSorter:
    """Ordena una lista de enteros usando el algoritmo Bubble Sort."""

    @staticmethod
    def sort(values: list[int]) -> list[int]:
        result = values.copy()
        size = len(result)

        for end in range(size - 1, 0, -1):
            for index in range(end):
                if result[index] > result[index + 1]:
                    result[index], result[index + 1] = (
                        result[index + 1], result[index]
                    )
        return result
