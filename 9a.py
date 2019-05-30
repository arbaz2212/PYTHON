class time:
    def __init__(self, hour, minute, second):
        self.h = hour
        self.m = minute
        self.s = second

    def totalSeconds(self):
        print("Total seconds = ", self.h * 60 * 60 + self.m * 60 + self.s)


a, b, c = map(int, input("Enter hh   mm   ss : ").split())
t = time(a, b, c)
t.totalSeconds()
