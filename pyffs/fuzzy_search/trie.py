from collections import deque


class Trie:
    def __init__(self, words, alphabet=set()):
        self._children_maps = []
        self._is_final = []

        for word in words:
            self._add_word(word, alphabet)

    def _add_word(self, word, alphabet):

        if not word:
            return

        if not self._children_maps:
            self._children_maps.append({})
            self._is_final.append(False)

        n_id = 0
        for s in word:
            alphabet.add(s)
            if s not in self._children_maps[n_id]:
                next_id = len(self._children_maps)
                self._children_maps.append({})
                self._is_final.append(False)
                self._children_maps[n_id][s] = next_id
                n_id = next_id
            else:
                n_id = self._children_maps[n_id][s]

        self._is_final[n_id] = True

    def get_all_words(self):
        if not self._children_maps:
            return []

        stack = deque([(0, '')])
        all_words = []

        while stack:
            n_id, current_word = stack.pop()
            if self._is_final[n_id]:
                all_words.append(current_word)

            for s, c_id in self._children_maps[n_id].items():
                stack.append((c_id, current_word + s))

        return all_words

    def is_final(self, node_id):
        return self._is_final[node_id]

    def get_children_symbols(self, node_id):
        return self._children_maps[node_id].keys()

    def get_child(self, node_id, symbol):
        return self._children_maps[node_id][symbol]

    @property
    def root(self):
        if not self._children_maps:
            raise Exception("Trying to access root of empty trie.")
        return 0
