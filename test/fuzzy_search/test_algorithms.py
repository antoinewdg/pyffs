from pyffs.fuzzy_search.algorithms import find_all_words_within_tolerance
from pyffs.automaton_management import generate_automaton_to_file
from test.utils import clean_generated_dir


def test_find_all_words_within_tolerance():
    generate_automaton_to_file(0)
    generate_automaton_to_file(1)
    generate_automaton_to_file(2)

    dictionary = [
        'car',
        'rat',
        'bat',
        'carp',
        'caterpillar',
        'kangaroo',
        'camel',
        'dog',
        'hog',
        'snake',
        'crow',
        'raven',
        'mate'
    ]

    result = find_all_words_within_tolerance('dog', dictionary, 0)
    assert set(result) == {'dog'}

    result = find_all_words_within_tolerance('dog', dictionary, 1)
    assert set(result) == {'dog', 'hog'}

    result = find_all_words_within_tolerance('dog', dictionary, 1)
    assert set(result) == {'dog', 'hog'}

    result = find_all_words_within_tolerance('dog', dictionary, 2)
    assert set(result) == {'dog', 'hog'}

    result = find_all_words_within_tolerance('cat', dictionary, 0)
    assert set(result) == set()

    result = find_all_words_within_tolerance('cat', dictionary, 1)
    assert set(result) == {'car', 'rat', 'bat'}

    result = find_all_words_within_tolerance('cat', dictionary, 2)
    assert set(result) == {'car', 'rat', 'bat', 'carp', 'mate'}

    clean_generated_dir()
