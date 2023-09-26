from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfacts():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain",
        "Wichita is the largest city in the state, but many would guess it is the Kansas city.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are ennoyed by wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfacts()
