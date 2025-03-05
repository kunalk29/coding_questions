from typing import List, Set, Tuple

class WordProcessorV1:
    words: Set[str] = {'so', 'som', 'some', 'what', 'me', 'civ', 'civilization', 'meat', 'lion', 'fire', 'house', 'hose'}

    def __init__(self) -> None:
        pass

    def process(self, stack: List[Tuple[Set[str], str]], temp: Set[str], remainder: str) -> Set[str]:
        matching_words = [x for x in self.find_matching_words(letter=remainder[0]) if remainder[:len(x)] == x]
        return_value = set()
        for y in matching_words:
            if y == remainder:
                return_value = temp.union({y})
            else:
                stack.append(
                    (
                        temp.union({y}),
                        remainder[len(y):]
                    )
                )
        return return_value

    def find_matching_words(self, letter: str) -> List[str]:
        return [x for x in self.words if x[0] == letter]

    def runner(self, primary: str) -> Set[str]:
        results = set()
        stack = [(set(), primary)]
        while stack:
            temp, remainder = stack.pop()
            new_words = self.process(stack=stack, temp=temp, remainder=remainder)
            results = results.union(new_words)

        return results


if __name__ == '__main__':
    word_processor = WordProcessorV1()
    inputs = ('somewhat', )
    output = word_processor.runner(*inputs)
    print(f"Inputs: {inputs}")
    print(f"Output: {output}")

    inputs = ('firehose',)
    output = word_processor.runner(*inputs)
    print(f"Inputs: {inputs}")
    print(f"Output: {output}")