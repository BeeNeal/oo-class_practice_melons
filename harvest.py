############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairings):
        """Add a food pairing to the instance's pairings list."""

        # you can extend with a tuple! passing a tuple as the single argument
        # 'extends' the list
        self.pairings.extend(pairings)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    # still a bit of a mess here
    all_melon_types = []

    m = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    m.add_pairing(['mint'])
    all_melon_types.append(m)

    m = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    m.add_pairing(['stawberries', 'mint'])
    all_melon_types.append(m)

    m = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    m.add_pairing(["proscuitto"])
    all_melon_types.append(m)

    m = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")
    m.add_pairing(['ice cream'])
    all_melon_types.append(m)

    # all_melon_types = [melon1, m2, m3, m4]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # name pairs with \n - pairings
    for melon in melon_types:
        print "{name} pairs with".format(name=melon.name)

        for pairing in melon.pairings:
            print "- {}".format(pairing)

        print

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    #is_sellable methods
    def __init__(self, num, m_type, shape_rating, color_rating, field, harvester):
        """Initialize a harvested melon."""

        print "initializing dis melon"

        self.num = num
        self.m_type = m_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
        #self.is_sellable = None
        self.is_sellable = self.is_sellable_x()

    def is_sellable_x(self):
        """This logic might change over time. Currently, a melon is able to be sold
        if both its shape and color ratings are greater than 5, and it didn’t
        come from field 3, which was found to have poisonous fertilizer planted
        by a competing melon farm."""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            self.is_sellable = True
        else:
            self.is_sellable = False

        return self.is_sellable


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # kind of a mess
    melon_1 = Melon(1, 'yw', 8, 7, 2, "Sheila")
    melon_2 = Melon(2, 'yw', 3, 4, 2, "Sheila")
    melon_3 = Melon(3, 'yw', 9, 8, 3, "Sheila")
    melon_4 = Melon(4, 'cas', 10, 6, 35, "Sheila")
    melon_5 = Melon(5, 'cren', 8, 9, 35, "Michael")
    melon_6 = Melon(6, 'cren', 8, 2, 35, "Michael")
    melon_7 = Melon(7, 'cren', 2, 3, 4, "Michael")
    melon_8 = Melon(8, 'musk', 6, 7, 4, "Michael")
    melon_9 = Melon(9, 'yw', 7, 10, 3, "Sheila")

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7,
              melon_8, melon_9]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest



# x = Melon(9, 'cas', 9, 8, 2, "Sheila")