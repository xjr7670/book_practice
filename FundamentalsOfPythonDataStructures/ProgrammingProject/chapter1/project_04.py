# -*- coding:utf-8 -*-


def main():
    iteration_time = int(input("input a iteration time: "))
    flag = -1
    div4_result = 0
    denominator = 1

    while iteration_time > 0:
        div4_result -= 1 / denominator * flag
        iteration_time -= 1
        flag *= -1
        denominator += 2

    print('the result is %6.8f' % (div4_result * 4))


if __name__ == "__main__":
    main()