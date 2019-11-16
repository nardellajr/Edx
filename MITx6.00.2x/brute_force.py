
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuples of the toal value of a solution to the 0/1 Knapsack problem and the
    items of the solution"""

    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    return result


def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits, 'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


if __name__ == '__main__':
    names = ['Wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = buildMenu(names, values, calories)

    testMaxVal(foods, 750)
