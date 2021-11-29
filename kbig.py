def kbig(nums, k):
    for i in nums:
        count_more = 0          # xbckj vjvtynjd
        for j in nums:
            if i < j:
                count_more += 1
        if count_more == k-1:   #Данное значения равняется i 
            return i


while True:
    print("Ввод (введите значения определенного списка который вам требуется через пробел): ")
    nums = [int(i) for i in input('nums = ').split()]
    k = int(input('Введите k = '))
    print("Вывод: ", kbig(nums, k))
