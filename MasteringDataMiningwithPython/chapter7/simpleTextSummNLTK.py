from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import OrderedDict
import pprint


with open('sampleText.txt', encoding='utf-8') as f:
    text = f.read()

summary_sentences = []
candidate_sentences = {}
candidate_sentence_counts = {}

striptext = text.replace('\n\n', ' ')
striptext = striptext.replace('\n', ' ')

words = word_tokenize(striptext)
lowercase_words = [word.lower() for word in words 
        if word not in stopwords.words() and word.isalpha()]

word_frequencies = FreqDist(lowercase_words)
most_frequent_words = FreqDist(lowercase_words).most_common(20)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(most_frequent_words)

sentences = sent_tokenize(striptext)
for sentence in sentences:
    candidate_sentences[sentence] = sentence.lower()

for long, short in candidate_sentences.items():
    count = 0
    for freq_word, frequency_score in most_frequent_words:
        if freq_word in short:
            count += frequency_score
            candidate_sentence_counts[long] = count

sorted_sentences = OrderedDict(sorted(
                                candidate_sentence_counts.items(),
                                key = lambda x: x[1],
                                reverse = True)[:4])
pp.pprint(sorted_sentences)
