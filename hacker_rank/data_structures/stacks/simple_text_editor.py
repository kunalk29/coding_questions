from typing import List

def simple_text_editor(n: int, operations: List[str]) -> None:
    one_two_operations = []
    current_word = []
    operations.reverse()
    while operations:
        total = operations.pop()
        split_total = total.split(' ')
        oper_type = int(split_total[0])
        val = None
        if len(split_total) == 2:
            val = split_total[1]
        if oper_type == 1:
            # Creating new words each time is O(n) move, since a new string and set of pointers must be generated.
            for x in val:
                current_word.append(x)
            one_two_operations.append(f'2 {len(val)}')
        if oper_type == 2:
            del_word = []
            letters_to_delete = int(val)
            for x in range(letters_to_delete):
                letter = current_word.pop()
                del_word.append(letter)
            del_word.reverse()
            del_word = ''.join(del_word)
            one_two_operations.append(f'1 {del_word}')
        if oper_type == 3:
            print(current_word[int(val) - 1])
        if oper_type == 4:
            undo_total = one_two_operations.pop()
            split_total = undo_total.split(' ')
            oper_type = int(split_total[0])
            val = split_total[1]
            if oper_type == 1:
                for x in val:
                    current_word.append(x)
            elif oper_type == 2:
                letters_to_delete = int(val)
                for x in range(letters_to_delete):
                    _ = current_word.pop()


if __name__ == '__main__':
    num_operations = 8
    operations = [
        '1 abc',
        '3 3',
        '2 3',
        '1 xy',
        '3 2',
        '4',
        '4',
        '3 1'
    ]
    simple_text_editor(n=num_operations, operations=operations)