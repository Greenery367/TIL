T = int(input())
count = 0

for _ in range(T):
    word = input()
    seen = set()
    prev_char = ''
    is_group_word = True

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
        prev_char = char

    if is_group_word:
        count += 1

print(count)
