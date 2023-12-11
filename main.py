import time

list = []

start = time.perf_counter()
for i in range(1000):
    list.append(i)
end = time.perf_counter()

print(end-start)
