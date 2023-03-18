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
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_type = input()


    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

        assert len(data) == n

        swaps = build_heap(data)

        assert len(swaps) <=4 * len(data)

        if len(swaps) == 0:
            print(len(swaps))
            print("The input array is already a heap, because it is sorted in increasing order.")
        else:
            print(len(swaps))
            for i, j in swaps:
                print(i, j)

    # Handle file input
    elif input_type == "F":
        filename = input("Enter the filename: ")
        with open(filename, "r") as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))

            assert len(data) == n

            swaps = build_heap(data)

            assert len(swaps) <=4 * len(data)

            if len(swaps) == 0:
                print(len(swaps))
                print("The input array is already a heap, because it is sorted in increasing order.")
            else:
                print(len(swaps))
                for i, j in swaps:
                    print(i, j)

if __name__ == "__main__":
    main()
