"""
Magic 8 ball implementation
"""

import random

MESSAGE_GREETING = 'Hi, World! I am Magic 8 Ball and I know the answer on any question'
MESSAGE_ANOTHER_QUESTION = 'Do you have an another question? Y/N: '
MESSAGE_NOT_UNDERSTAND = 'I do not understand your question. Please, ask your question correctly...'


class Magic8Ball:

    def __init__(self):
        self.new_magic8ball()

    def is_question(self, question):
        return len(question) >= 2 and (any(ch.isupper() for ch in question) or any(ch.islower() for ch in question))

    def new_magic8ball(self):
        answers = [
            'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes — definitely', 'You may rely on it',
            'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Yes',
            'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
            'Concentrate and ask again',
            'Don’t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
        ]
        print(MESSAGE_GREETING)
        print("What's your name? ", end='')
        name = input()

        while True:
            print(f'Hi, {name}. Please, ask your question...')
            if self.is_question(input()):
                print(random.choice(answers))
                print(MESSAGE_ANOTHER_QUESTION, end='')
                if not input().upper() == 'Y':
                    print(f'See you soon, {name}!')
                    exit()
            else:
                print(MESSAGE_NOT_UNDERSTAND)


if __name__ == '__main__':
    new_magic_ball = Magic8Ball()
