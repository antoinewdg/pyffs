import pytest

from pyffs.fuzzy_search.trie import Trie


class TestTrie:
    def test_trie_is_correctly_built(self):
        alphabet = set()
        trie = Trie(['cat', 'd', 'b', 'car', 'cart'], alphabet)

        assert alphabet == set('abcdrt')

        node_ = trie.root
        edges = set(trie.get_children_symbols(node_))
        assert edges == {'c', 'd', 'b'}

        node_c = trie.get_child(node_, 'c')
        edges = set(trie.get_children_symbols(node_c))
        assert edges == {'a'}

        node_d = trie.get_child(node_, 'd')
        edges = set(trie.get_children_symbols(node_d))
        assert edges == set()
        assert trie.is_final(node_d)

        node_b = trie.get_child(node_, 'b')
        edges = set(trie.get_children_symbols(node_b))
        assert edges == set()
        assert trie.is_final(node_b)

        node_ca = trie.get_child(node_c, 'a')
        edges = set(trie.get_children_symbols(node_ca))
        assert edges == {'r', 't'}

        node_cat = trie.get_child(node_ca, 't')
        edges = set(trie.get_children_symbols(node_cat))
        assert edges == set()
        assert trie.is_final(node_cat)

        node_car = trie.get_child(node_ca, 'r')
        edges = set(trie.get_children_symbols(node_car))
        assert edges == {'t'}
        assert trie.is_final(node_car)

        node_cart = trie.get_child(node_car, 't')
        edges = set(trie.get_children_symbols(node_cart))
        assert edges == set()
        assert trie.is_final(node_cart)

    def test_get_all_words(self):
        words = {'arc', 'art', 'artwork', 'bar', 'car', 'star', 'cat', 'attack'}
        trie = Trie(words)
        assert set(trie.get_all_words()) == words

    def test_empty_trie_raises_exception_when_accessing_root(self):
        trie = Trie([])
        with pytest.raises(Exception):
            a = trie.root
