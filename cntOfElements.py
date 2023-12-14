"Chapter 4.2"


def cnt_of_elements(arr: list) -> int:
    if arr == []:
        return 0

    return 1 + cnt_of_elements(arr[1:])


def main() -> None:
    print(cnt_of_elements([2, 4, 6]))


if __name__ == '__main__':
    main()
