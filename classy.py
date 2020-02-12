"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


'''class Classy(object):
    def __init__(self):
        self.items = []
        self.sum = 0

    def addItem(self, classiness):
        self.items.append(classiness)

    def getClassiness(self):
        for item in self.items:
            if item == "tophat":
                self.sum += 2
            elif item == "bowtie":
                self.sum += 4
            elif item == "monocle":
                self.sum += 5
            else:
                self.sum += 0
        return self.items'''

"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, classiness):
        self.items.append(classiness)

    def getClassiness(self):
        for i in range(len(self.items)):
            if self.items[i] == "tophat":
                self.items[i] = 2
            elif self.items[i] == "bowtie":
                self.items[i] = 4
            elif self.items[i] == "monocle":
                self.items[i] = 5
            else:
               continue
        return sum(filter(lambda i: isinstance(i, int), self.items))


# Test cases
me = Classy()

# Should be 0
print (me.getClassiness())

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())