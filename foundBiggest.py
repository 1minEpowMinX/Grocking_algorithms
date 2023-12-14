"Chapter 4.3"


def findBiggest(arr: list) -> int:  # ? странная реализация от автора
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def main() -> None:
    print(findBiggest([2, 8, 4, 6, 7, 10, 11]))


if __name__ == '__main__':
    main()
