from slide_similarity import SlideComparator

comparator = SlideComparator()

def test_squashing_1():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-04.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-05.png')
    assert not result

def test_squashing_2():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-05.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-06.png')
    assert not result

def test_squashing_3():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-27.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-28.png')
    assert result

def test_squashing_4():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-29.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-30.png')
    assert result

def test_squashing_6():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-31.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-32.png')
    assert result

def test_squashing_7():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-32.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-33.png')
    assert result

def test_squashing_8():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-34.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-35.png')
    assert result

def test_squashing_9():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-38.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-39.png')
    assert result

def test_squashing_10():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-38.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-39.png')
    assert result

def test_squashing_11():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-44.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-45.png')
    assert result

def test_squashing_12():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-53.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-54.png')
    assert result

def test_squashing_13():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-54.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-55.png')
    assert result

def test_squashing_14():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-55.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-56.png')
    assert result

def test_squashing_15():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-58.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-59.png')
    assert result

def test_squashing_16():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-59.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-60.png')
    assert result

def test_squashing_17():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-74.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-75.png')
    assert result

def test_squashing_18():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-75.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-76.png')
    assert result

def test_squashing_19():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-77.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-78.png')
    assert result

def test_squashing_20():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-78.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-79.png')
    assert result

def test_squashing_21():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-79.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-80.png')
    assert result

def test_squashing_22():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-80.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-81.png')
    assert result

def test_squashing_22():
    result = comparator.get_similarity_score('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-92.png', 
                                             'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-93.png')
    assert result