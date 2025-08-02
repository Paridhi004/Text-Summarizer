import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import string

def nltk_summarizer(raw_text):
    stopWords = set(stopwords.words("english"))
    word_frequencies = {}

    for word in nltk.word_tokenize(raw_text):
        word_lower = word.lower()
        if word_lower not in stopWords and word_lower not in string.punctuation:
            if word_lower not in word_frequencies:
                word_frequencies[word_lower] = 1
            else:
                word_frequencies[word_lower] += 1

    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= maximum_frequency

    sentence_list = sent_tokenize(raw_text)
    sentence_scores = {}

    for sent in sentence_list:
        word_count = len(sent.split())
        if 5 < word_count < 30:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies:
                    if sent not in sentence_scores:
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)  # You can adjust 3 here
    summary_sentences = sorted(summary_sentences, key=sentence_list.index)  # Keep original order
    summary = ' '.join(summary_sentences)
    return summary

if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines,
    in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": any
    device that perceives its environment and takes actions that maximize its 
    chance of achieving its goals. Colloquially, the term "artificial intelligence"
    is often used to describe machines that mimic "cognitive" functions such as
    "learning" and "problem solving". 
    As machines become increasingly capable, tasks considered to require 
    "intelligence" are often removed from the definition of AI, a phenomenon 
    known as the AI effect. For instance, optical character recognition is
    frequently excluded from things considered to be AI, having become a
    routine technology. 
    AI applications include advanced web search engines (e.g., Google), 
    recommendation systems (used by YouTube, Amazon, and Netflix), understanding 
    human speech (such as Siri and Alexa), self-driving cars (e.g., Tesla), 
    automated decision-making, and competing at the highest level in strategic
      game systems (such as chess and Go).
    """

    summary = nltk_summarizer(sample_text)
    print("Summary:\n", summary)
