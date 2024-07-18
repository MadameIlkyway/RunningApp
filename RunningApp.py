import time

print()
print("Intervall Running App")
print("____________________")

run = float(input("Wie viele Sekunden willst du laufen? "))
walk = float(input("Wie viele Sekunden willst du gehen? "))
interval = int(input("Anzahl der Intervalle: "))

length = (run + walk) * interval

print("Die Dauer beträgt", length, "Sekunden.")
half = length/2
timer = 0

#if timer >= half:
#    print("Great, you are half way through. Keep going.")

print("What a great day for running.")
print("Start your warm up")
time.sleep(3)
for i in range(interval) :
    print("You are on run", i+1, "of", interval)
    print("Start running for", run, "seconds.")
    time.sleep(run)
    timer = timer + run
    print("Start walking for", walk, "seconds. ")
    time.sleep(walk)
    timer = timer + walk
    print("Already", timer, "seconds done. Keep going.")
print("Well done. Start your cool down.")
time.sleep(3)
print("Great. Be proud of yourself.")