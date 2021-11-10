import sys

number = int(sys.stdin.readline().rstrip())
lowest_time = 9999999999
final_line = str()

for i in range(number):
    current_line = str(sys.stdin.readline().rstrip())
    current_line2 = list(map(int, current_line.rstrip().split(":")))
    total_seconds = current_line2[0] * 3600 + current_line2[1] * 60 + current_line2[2]
    if total_seconds < lowest_time:
        lowest_time = total_seconds
        final_line = current_line
    else:
        continue
print(final_line)
