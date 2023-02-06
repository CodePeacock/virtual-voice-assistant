from nltk import chunk, tag, tokenize

PARA = "I want you to create a card named Demo 1 in the list demolist and board of the list is it project"
sents = tokenize.sent_tokenize(PARA)
print("\nsentence tokenization\n===================\n", sents)
# word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
# POS Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
    print("\nPOS Tagging\n===========\n", tagged_words)
# chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
    print("\nchunking\n========\n")
    print(tree)

# Output:
# sentence tokenization
