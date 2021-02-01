def next_bigger(num):
    digits = list(str(num))

    nd = len(digits)
    try:
        pivot = next(i for i in reversed(range(nd-1)) if digits[i] < digits[i+1])
        swap = next(i for i in reversed(range(nd)) if digits[pivot] < digits[i])

        digits[pivot], digits[swap] = digits[swap], digits[pivot]
        digits[pivot+1:] = reversed(digits[pivot+1:])

        return int(''.join(d for d in digits))
    except StopIteration:
        return -1
