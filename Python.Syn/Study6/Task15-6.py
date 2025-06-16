import math

print(f'Enter how much weight can it take boat:')
boat_m = int(input())
print(f'Enter the number of fishermen:')
fishermen = int(input())
print(f'Enter the weight of each fisherman (in the line)')
fisher_m = list(map(int,input().split()))
zero_unit = []
approved = []
boat = 0


if 1 <= boat_m <= 1000000:
    if 1 <= fishermen <= 100:
        if (len(fisher_m)) == fishermen:
            for i in fisher_m:
                if i <= boat_m:
                    approved.append(i)
                    boat = sum(approved) / boat_m

                elif i > boat_m:
                    zero_unit.append(i)
            print(f'{math.ceil(boat)} boats are needed')
        else:
            print(f'More masses are indicated than there are fishermen')

    else:
        print(f'Fishermen more than 100 or less than 1')


else:
    print(f'There are no such boats - its already a ship or a raft =)')


if not zero_unit:
    pass
else:
    print(f'There is a fisherman(s) who cant get across - {zero_unit}')

