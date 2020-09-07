import random


class Win_Calc:

    def is_player_good(self, winlist):


        if winlist < 0.33:
            trash = ['DIS MANE STINKS', 'run while you can', 'I repeat, YOU ARE NOT WINNING THIS', 'I predict a fat L', 'Have fun trying to carry this person', 'He is a walking trash can', 'He needs to find a new game', 'BAD LUCK!!!']
            return (random.choice(trash))

        elif winlist > 0.33 and winlist <= 0.5:
            notgood = ['Losing a bit', 'Not very good', 'He needs lots of help', 'Your back might hurt a little', 'Does not win much']
            return (random.choice(notgood))

        elif winlist > 0.5 and winlist <= 0.65:
            ight = ['He is ight', 'He can win a lil', 'You guys have a decent chance to win', 'Serviceable', 'Should be a dub']
            return (random.choice(ight))

        elif winlist > 0.65:
            good = ['DUB!', 'You getting carried', 'His back gonna hurt a bit', 'winner winner chicken dinner', 'Dude wins TOO MUCH', 'You aint even gotta try', 'GODLIKE']
            return (random.choice(good))


