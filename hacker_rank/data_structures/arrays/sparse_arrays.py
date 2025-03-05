from typing import List

def matchingStrings(stringList: List[str], queries: List[str]) -> List[int]:
    # The point here is to work with arrays, not introduce a dictionary
    words = []
    for i in stringList:
        ind = 0
        found = False
        while ind < len(words):
            if i == words[ind][0]:
                words[ind][1] += 1
                found = True
            ind += 1
        if not found:
            words.append([i, 1])
    answers = []
    for j in queries:
        found = False
        ind = 0
        while ind < len(words):
            if j == words[ind][0]:
                answers.append(words[ind][1])
                found = True
            ind += 1
        if not found:
            answers.append(0)
    return answers

if __name__ == '__main__':
    inputs = (
        ['def', 'de', 'fgh'],
        ['de', 'lmn', 'fgh']
    )
    output = matchingStrings(*inputs)
    print(f"output: {output}, inputs: {inputs}")