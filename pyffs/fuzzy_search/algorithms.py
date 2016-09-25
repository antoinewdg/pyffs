from collections import deque

from .trie import Trie
from .levenshtein_automaton import LevenshteinAutomaton


def trie_automaton_intersection(automaton, trie, include_error):
    results = []
    if trie.root == -1:
        return []

    stack = deque([(trie.root, automaton.get_initial_state(), '')])
    while stack:
        trie_node, state, current_word = stack.pop()

        if trie.is_final(trie_node) and automaton.is_final(state):
            if include_error:
                results.append((automaton.get_error(state), current_word))
            else:
                results.append(current_word)

        for symbol in trie.get_children_symbols(trie_node):
            next_state = automaton.transition(state, symbol)
            if automaton.is_empty_state(next_state):
                continue
            stack.append((
                trie.get_child(trie_node, symbol),
                next_state,
                current_word + symbol,
            ))

    return results


def find_all_words_within_tolerance(query, words, tolerance, include_error=False):
    alphabet = set()
    trie = Trie(words, alphabet)
    automaton = LevenshteinAutomaton(tolerance, query, alphabet)

    return trie_automaton_intersection(automaton, trie, include_error)
