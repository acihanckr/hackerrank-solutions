#start
input()
arr = list(map(float, input().split()))
weights = list(map(float, input().split()))
print(round(sum([i*j for i,j in zip(arr,weights)])/sum(weights),1))
#end
