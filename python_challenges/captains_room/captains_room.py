#start
from collections import Counter

k = int(input())
room_numbers = list(map(int, input().split()))
rooms = Counter(room_numbers)
captains_room = [c for c in rooms.keys() if not rooms[c] == k]
print(captains_room[0])
#end