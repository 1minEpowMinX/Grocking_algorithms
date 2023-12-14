"Chapter 4.1"


def sum_of_elements(arr: list) -> int:
    if arr == []:
        return 0

    return arr[0] + sum_of_elements(arr[1:])


def main() -> None:
    print(sum_of_elements([2, 4, 6]))


if __name__ == '__main__':
    main()
