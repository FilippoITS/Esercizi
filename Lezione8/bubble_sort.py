def bubble_sort(x:list):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp


def bubble_sort_optimized(x:list):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp


def bubble_sort_optimized1(x:list):
    ho_fatto_swap = False
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                ho_fatto_swap = True
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if not ho_fatto_swap:
            break
