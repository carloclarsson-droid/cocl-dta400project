# Retrieve latency values from a file and list them in order. 
# Read from a file 'xxxxx.txt' in the same directory.
# s = line of file; i = index of line.
# Read only from lines with 'time=' or 'time<' and exclude all but the number. 
# Output as list of numbers representing latency of each ping. 

fileName = input('Write the name of the file including type: ')

pingFile = open(fileName, 'r')

# count = 0

latencyHolder = ''

for s in pingFile:
    if 'time=' in s or 'time<' in s:
        for i in range(0, len(s)):
            if s[i-4:i+1:1] == 'time=':
                latencyHolder = s[i+1::]
                latencyHolder = latencyHolder.strip()
                latencyHolder = latencyHolder.rstrip('ms')
                latencyHolder = latencyHolder.strip()
                print(latencyHolder)
            if s[i-4:i+1:1] == 'time<':
                latencyHolder = s[i::]
                latencyHolder = latencyHolder.strip()
                latencyHolder = latencyHolder.rstrip('ms')
                latencyHolder = latencyHolder.strip()
                print(latencyHolder)
        # count += 1
# print(count)
                


            

