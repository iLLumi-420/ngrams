from ngrams import generate_ngrams
import pytest

def test_generate_ngrams():

    assert generate_ngrams('This is an example text for test', 1) == ['This', 'example', 'text', 'test']

    assert generate_ngrams('This is an example text for test', 2) ==['This example', 'example text', 'text test']

    assert generate_ngrams('This is an example text for test', 3) == ['This example text', 'example text test']


if __name__ == '__main__':
    print('Running generate_ngrams test')
    test_generate_ngrams()