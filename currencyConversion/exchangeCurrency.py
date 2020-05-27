import getCurrencyRates
import sys

nameDict = {
    1:"Mirror of Kalandra",
    2:"Mirror Shard",
    3:"Awakener's Orb",
    4:"Hunter's Exalted Orb",
    5:"Crusader's Exalted Orb",
    6:"Warlord's Exalted Orb",
    7:"Redeemer's Exalted Orb",
    8:"Exalted Orb",
    9:"Divine Orb",
    10:"Blessing of Chayula",
    11:"Ancient Orb",
    12:"Exalted Shard",
    13:"Orb of Annulment",
    14:"Fertile Catalyst",
    15:"Harbinger's Orb",
    16:"Stacked Deck",
    17:"Prismatic Catalyst",
    18:"Awakened Sextant",
    19:"Vaal Orb",
    20:"Blessing of Xoph",
    21:"Blessing of Esh",
    22:"Blessing of Uul-Netol",
    23:"Annulment Shard",
    24:"Splinter of Chayula",
    25:"Tempering Catalyst",
    26:"Gemcutter's Prism",
    27:"Blessing of Tul",
    28:"Orb of Scouring",
    29:"Prime Sextant",
    30:"Orb of Regret",
    31:"Splinter of Uul-Netol",
    32:"Cartographer's Chisel",
    33:"Orb of Alteration",
    34:"Glassblower's Bauble",
    35:"Turbulent Catalyst",
    36:"Orb of Horizons",
    37:"Orb of Fusing",
    38:"Regal Orb",
    39:"Chromatic Orb",
    40:"Simple Sextant",
    41:"Orb of Chance",
    42:"Abrasive Catalyst",
    43:"Splinter of Xoph",
    44:"Orb of Alchemy",
    45:"Splinter of Tul",
    46:"Splinter of Esh",
    47:"Intrinsic Catalyst",
    48:"Orb of Augmentation",
    49:"Portal Scroll",
    50:"Blacksmith's Whetstone",
    51:"Armourer's Scrap",
    52:"Engineer's Orb",
    53:"Imbued Catalyst",
    54:"Jeweller's Orb",
    55:"Orb of Transmutation",
    56:"Orb of Binding",
    57:"Silver Coin",
    58:"Blessed Orb",
    59:"Scroll of Wisdom",
    60:"Perandus Coin",
    61:"Chaos Orb",
}

def convert(source,target,amount,currencyList):
    #takes in the source currency, the currency you want to convert to, 
    # the amount of the currency you want to convert to, and the currency information list
    sourceCurr =  None
    targetCurr = None
    for i in currencyList:
        if i.name == source:
            sourceCurr = i
            break
    for i in currencyList:
        if i.name == target:
            targetCurr = i
            break

    targetChaosEquiv = targetCurr.value * float(amount)
    return sourceCurr.value * targetChaosEquiv


def main():
    currencyList = getCurrencyRates.getCurrencyRates()
    #print(currencyList)
    print("""
    Select the curency you have (would like to convert from)
    1)Mirror of Kalandra
    2)Mirror Shard
    3)Awakener's Orb
    4)Hunter's Exalted Orb
    5)Crusader's Exalted Orb
    6)Warlord's Exalted Orb
    7)Redeemer's Exalted Orb
    8)Exalted Orb
    9)Divine Orb
    10)Blessing of Chayula
    11)Ancient Orb
    12)Exalted Shard
    13)Orb of Annulment
    14)Fertile Catalyst
    15)Harbinger's Orb
    16)Stacked Deck
    17)Prismatic Catalyst
    18)Awakened Sextant
    19)Vaal Orb
    20)Blessing of Xoph
    21)Blessing of Esh
    22)Blessing of Uul-Netol
    23)Annulment Shard
    24)Splinter of Chayula
    25)Tempering Catalyst
    26)Gemcutter's Prism
    27)Blessing of Tul
    28)Orb of Scouring
    29)Prime Sextant
    30)Orb of Regret
    31)Splinter of Uul-Netol
    32)Cartographer's Chisel
    33)Orb of Alteration
    34)Glassblower's Bauble
    35)Turbulent Catalyst
    36)Orb of Horizons
    37)Orb of Fusing
    38)Regal Orb
    39)Chromatic Orb
    40)Simple Sextant
    41)Orb of Chance
    42)Abrasive Catalyst
    43)Splinter of Xoph
    44)Orb of Alchemy
    45)Splinter of Tul
    46)Splinter of Esh
    47)Intrinsic Catalyst
    48)Orb of Augmentation
    49)Portal Scroll
    50)Blacksmith's Whetstone
    51)Armourer's Scrap
    52)Engineer's Orb
    53)Imbued Catalyst
    54)Jeweller's Orb
    55)Orb of Transmutation
    56)Orb of Binding
    57)Silver Coin
    58)Blessed Orb
    59)Scroll of Wisdom
    60)Perandus Coin
    61)Chaos Orb
    """)

    source = nameDict[int(input())]

    print("""
    Select the currency that you would like to convert to
    1)Mirror of Kalandra
    2)Mirror Shard
    3)Awakener's Orb
    4)Hunter's Exalted Orb
    5)Crusader's Exalted Orb
    6)Warlord's Exalted Orb
    7)Redeemer's Exalted Orb
    8)Exalted Orb
    9)Divine Orb
    10)Blessing of Chayula
    11)Ancient Orb
    12)Exalted Shard
    13)Orb of Annulment
    14)Fertile Catalyst
    15)Harbinger's Orb
    16)Stacked Deck
    17)Prismatic Catalyst
    18)Awakened Sextant
    19)Vaal Orb
    20)Blessing of Xoph
    21)Blessing of Esh
    22)Blessing of Uul-Netol
    23)Annulment Shard
    24)Splinter of Chayula
    25)Tempering Catalyst
    26)Gemcutter's Prism
    27)Blessing of Tul
    28)Orb of Scouring
    29)Prime Sextant
    30)Orb of Regret
    31)Splinter of Uul-Netol
    32)Cartographer's Chisel
    33)Orb of Alteration
    34)Glassblower's Bauble
    35)Turbulent Catalyst
    36)Orb of Horizons
    37)Orb of Fusing
    38)Regal Orb
    39)Chromatic Orb
    40)Simple Sextant
    41)Orb of Chance
    42)Abrasive Catalyst
    43)Splinter of Xoph
    44)Orb of Alchemy
    45)Splinter of Tul
    46)Splinter of Esh
    47)Intrinsic Catalyst
    48)Orb of Augmentation
    49)Portal Scroll
    50)Blacksmith's Whetstone
    51)Armourer's Scrap
    52)Engineer's Orb
    53)Imbued Catalyst
    54)Jeweller's Orb
    55)Orb of Transmutation
    56)Orb of Binding
    57)Silver Coin
    58)Blessed Orb
    59)Scroll of Wisdom
    60)Perandus Coin
    61)Chaos Orb
    """)

    target = nameDict[int(input())]

    print("Enter the amount of " + target)

    amount = int(input())
    ##if len(sys.argv) > 1:
    ##    amount = sys.argv[2]
    ##    target = sys.argv[3]
    ##    source = sys.argv[1]

    print(str(amount) + " " + target + " is equivilant to " + str(convert(source,target,amount,currencyList))+ " " + source)

if __name__ == '__main__':
    main()