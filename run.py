from cougarSound.cougarSound import make_sound as make_sound1
from snakeSound.snakeSound import make_sound as make_sound2
from dogSound.dogSound import make_sound as make_sound3

def main():
    sound1 = make_sound1()
    sound2 = make_sound2()
    sound3 = make_sound3()

    print(f"Cougar: {sound1}")
    print(f"Python: {sound2}")
    print(f"Dog: {sound3}")

if __name__ == "__main__":
    main()