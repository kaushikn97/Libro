import pickle
from preproc import TrieNode, PostingsList, Node
import os
from bookClass import Book
if __name__ == "__main__":
    pickle_in = open(os.getcwd() + "/book_info.pickle","rb")
    books = pickle.load(pickle_in)

    pickle_in = open(os.getcwd() + "/trie_with_vectors.pickle","rb")
    trie = pickle.load(pickle_in)

    pickle_in = open(os.getcwd() + "/dictionary.pickle","rb")
    dictionary = pickle.load(pickle_in)

    vectors = []
    vectors.append([])

    for book in books:
        vectors.append([])
        print(book.index)
        vector_mag = 0
        for postings_list in dictionary:

            score = postings_list.find_book_score(book.index)
            vectors[int(book.get_index())].append(score)
            vector_mag = vector_mag + score*score

        for value in vectors[int(book.get_index())]:
            value = value/vector_mag

    pickle_out = open(os.getcwd() + "/doc_vectors.pickle","wb")
    pickle.dump(vectors, pickle_out)
    pickle_out.close()
