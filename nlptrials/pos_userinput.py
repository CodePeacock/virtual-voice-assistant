# # !pip install -U spacy
# # !python -m spacy download en_core_web_sm
# import spacy

# # Load English tokenizer, tagger, parser and NER
# nlp = spacy.load("en_core_web_sm")
# # Process whole documents
# text = (
#     "When Sebastian Thrun started working on self-driving cars at "
#     "Google in 2007, few people outside of the company took him "
#     "seriously. “I can tell you very senior CEOs of major American "
#     "car companies would shake my hand and turn away because I wasn’t "
#     "worth talking to,” said Thrun, in an interview with Recode earlier "
#     "this week."
# )
# doc = nlp(text)
# # Analyse syntax
# print(
#     "Noun phrases:",
#     [chunk.text for chunk in doc.noun_chunks if chunk.lemma_ != "-PRON-"],
# )
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# With NLTK
import nltk
from nltk.chunk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
tokens = word_tokenize(sentence)
print(tokens)
tagged = pos_tag(tokens)
print(tagged[:6])
entities = ne_chunk(tagged)
print(entities)
