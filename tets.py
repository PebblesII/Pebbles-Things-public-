import time
print("=" * 30)

print("░██████╗        ████████╗        ░█████╗░        ██████╗░        ████████╗")
print("██╔════╝        ╚══██╔══╝        ██╔══██╗        ██╔══██╗        ╚══██╔══╝")
print("╚█████╗░          ░██║░░░        ███████║        ██████╔╝          ░██║░░░")
print("░╚═══██╗          ░██║░░░        ██╔══██║        ██╔══██╗          ░██║░░░")
print("██████╔╝          ░██║░░░        ██║░░██║        ██║░░██║          ░██║░░░")
print("╚═════╝░          ░╚═╝░░░        ╚═╝░░╚═╝        ╚═╝░░╚═╝          ░╚═╝░░░")

Time = 0
Answer = input("Y or N = ")
Symbol = "%"

if Answer == "Y":
    while Time <= 100:
        print("-" * 30, "{}{}".format(Time, Symbol))

        Time = Time + 1

        time.sleep(1)

        print("-" * 30, "{}{}".format(Time, Symbol))

        Time = Time + 1