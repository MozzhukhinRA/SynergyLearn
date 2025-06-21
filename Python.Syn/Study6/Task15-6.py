print(f'Enter how much weight can it take boat:')
boat_m = int(input())
print(f'Enter the number of fishermen:')
fishermen = int(input())
print(f'Enter the weight of each fisherman (in the line)')
fisher_m = list(map(int,input().split()))

fisher_m = [w for w in fisher_m if w <= boat_m]

fisher_m.sort()
fisher_left = 0
fisher_right = len(fisher_m) - 1
boats = 0

if 1 <= boat_m <= 1000000:
    if 1 <= fishermen <= 100:
        if (len(fisher_m)) == fishermen:
            while fisher_left <= fisher_right:
                if fisher_m[fisher_right] + fisher_m[fisher_left] <= boat_m:
                    fisher_left += 1
                    fisher_right -= 1
                else:
                    fisher_right -= 1
                boats += 1


print(boats)