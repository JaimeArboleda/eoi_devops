import dice
from time import sleep


def roll(amount:int, sides:int):
    return dice.roll(f'{amount}d{sides}')

for idx, result in enumerate(roll(5,6)):
    print(f'El lanzamiento es: {idx+1}, y el número obtenido es: {result}')
    sleep(5)