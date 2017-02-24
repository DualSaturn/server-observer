"""A simple markov chain text generator."""
import random
import requests

class MarkovGenerator():
    """Pass the input string into the constructor."""
    def __init__(self, string: str):
        self.words = string.split()
        self.number_of_words = len(self.words)
        self.word_cache = {}
        self.fill_cache()

    def threes_generator(self):
        """Generator that yields the words in the input string in threes."""
        if self.number_of_words < 3:
            return
        for index, word in enumerate(self.words[:-2]):
            yield (word, self.words[index+1], self.words[index+2])

    def fill_cache(self):
        """Method to fill cache dictionary with associated words."""
        for word1, word2, word3 in self.threes_generator():
            key = (word1, word2)
            if key in self.word_cache:
                self.word_cache[key].append(word3)
            else:
                self.word_cache[key] = [word3]

    def create_markov_chain_text(self, length=100):
        """Returns a string generated, with an optional parameter of length in words."""
        random_start_index = random.randint(0, self.number_of_words-3)
        word1, word2 = self.words[random_start_index], self.words[random_start_index+1]
        output = []
        for x in range(length):
            output.append(word1)
            try:
                word1, word2, = word2, random.choice(self.word_cache[(word1, word2)])
            except KeyError:
                return 'A KeyError occured.'
        return ' '.join(output)

if __name__ == '__main__':
	url = 'http://www.gutenberg.org/cache/epub/1661/pg1661.txt'
	response = requests.get(url)
	markgen = MarkovGenerator(response.text)
	false_sherlock = markgen.create_markov_chain_text(400)
	print('{}{}'.format(false_sherlock[0].upper(), false_sherlock[1:]))
