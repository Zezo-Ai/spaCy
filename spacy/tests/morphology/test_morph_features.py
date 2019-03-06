from __future__ import unicode_literals
import pytest

from ...morphology import Morphology
from ...strings import StringStore
from ...lemmatizer import Lemmatizer
from ...morphology import *

@pytest.fixture
def morphology():
    return Morphology(StringStore(), {}, Lemmatizer())

def test_init(morphology):
    pass

def test_add_morphology_with_string_names(morphology):
    morphology.add({"Case_gen", "Number_sing"})

def test_add_morphology_with_int_ids(morphology):
    morphology.add({Case_gen, Number_sing})

def test_add_morphology_with_mix_strings_and_ints(morphology):
    morphology.add({PunctSide_ini, 'VerbType_aux'})


def test_morphology_tags_hash_distinctly(morphology):
    tag1 = morphology.add({PunctSide_ini, 'VerbType_aux'})
    tag2 = morphology.add({"Case_gen", 'Number_sing'})
    assert tag1 != tag2

def test_morphology_tags_hash_independent_of_order(morphology):
    tag1 = morphology.add({"Case_gen", 'Number_sing'})
    tag2 = morphology.add({"Number_sing", "Case_gen"}) 
    assert tag1 == tag2

def test_update_morphology_tag(morphology):
    tag1 = morphology.add({"Case_gen"})
    tag2 = morphology.update(tag1, {"Number_sing"})
    assert tag1 != tag2
    tag3 = morphology.add({"Number_sing", "Case_gen"}) 
    assert tag2 == tag3