# python3


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        swaps = sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        swaps = sift_down(min_index, data, swaps)
    return swaps



def main():
    # Add prompt for input type
    input_type = input()
    
    # Keyboard input
    if input_type == "I":
        n = int(input().strip())
        data = list(map(int, input().split()))

        # Add checks
        assert len(data) == n
        assert 1 <= n <= 10 ** 5 and all(0 <= x <= 10 ** 9 for x in data)

        swaps = build_heap(data)

        # Add check
        assert len(swaps) <= 4 * n

        # Output result
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

    # File input
    elif input_type == "F":
        filename = input()
        with open(filename, "r") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))

            # Add checks
            assert len(data) == n
            assert 1 <= n <= 10 ** 5 and all(0 <= x <= 10 ** 9 for x in data)

            swaps = build_heap(data)

            # Add check
            assert len(swaps) <= 4 * n

            # Output result
            print(len(swaps))
            for i, j in swaps:
                print(i, j)

if __name__ == "__main__":
    main()
