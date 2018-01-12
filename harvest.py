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


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # you can extend with a tuple! passing a tuple as the single argument
        # 'extends' the list
        self.pairings.extend(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    # all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing(['mint'])

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing(['stawberries', 'mint'])

    cren = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    cren.add_pairing(["proscuitto"])

    yw = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")
    yw.add_pairing(['ice cream'])

    all_melon_types = [musk, cas, cren, yw]

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
        # self.is_sellable = None
        self.is_sellable = is_sellable(self)


    def is_sellable(self):
        """This logic might change over time. Currently, a melon is able to be sold
        if both its shape and color ratings are greater than 5, and it didn’t
        come from field 3, which was found to have poisonous fertilizer planted
        by a competing melon farm."""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            sell_this_melon = True
        else:
            sell_this_melon = False

        return self_this_melon


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest



# x = Melon(9, 'cas', 9, 8, 2, "Sheila")