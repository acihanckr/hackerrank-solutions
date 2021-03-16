#start
k = int(input())
for _ in range(k):
    input()
    cubes = list(map(int, input().split()))
    ordered_cubes = list()
    for _ in range(len(cubes)):
        if cubes[0]>=cubes[-1]:
            ordered_cubes.append(cubes.pop(0))
        else:
            ordered_cubes.append(cubes.pop(-1))
    ans = 'Yes' if ordered_cubes == sorted(ordered_cubes, reverse = True) else 'No'
    print(ans)
#end