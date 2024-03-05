from slide_similarity import SlideComparator

comparator = SlideComparator()


# HARD MATCH

# def test_matching_1():
#     result = comparator.is_similar('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-04.png', 
#                                              'frames/cropped_frame4.png')
#     result = comparator.is_similar('Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-04.png', 
#                                              'frames/cropped_frame5.png')
#     assert result

def test_matching_2():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-25.png',
        'frames/cropped_frame6.png', slide_slide_comp=False)
    assert result


def test_matching_3():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-26.png',
        'frames/cropped_frame59.png', slide_slide_comp=False)
    assert result


def test_matching_4():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-28.png',
        'frames/cropped_frame88.png', slide_slide_comp=False)
    assert result


# TRANSITIONS
def test_matching_5():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-28.png',
        'frames/cropped_frame89.png', slide_slide_comp=False)
    assert result


def test_matching_6():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-33.png',
        'frames/cropped_frame114.png', slide_slide_comp=False)
    assert result


def test_matching_7():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-33.png',
        'frames/cropped_frame114.png', slide_slide_comp=False)
    assert result


def test_matching_8():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-34.png',
        'frames/cropped_frame132.png', slide_slide_comp=False)
    assert result


# ANNOTATIONS MATCH
def test_matching_9():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-27.png',
        'frames/cropped_frame82.png', slide_slide_comp=False)
    assert result


def test_matching_10():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-25.png',
        'frames/cropped_frame10.png', slide_slide_comp=False)
    assert result


def test_matching_11():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-43.png',
        'frames/cropped_frame181.png', slide_slide_comp=False)
    assert result


def test_matching_12():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-43.png',
        'frames/cropped_frame189.png', slide_slide_comp=False)
    assert result


def test_matching_13():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-43.png',
        'frames/cropped_frame197.png', slide_slide_comp=False)
    assert result


def test_matching_14():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-43.png',
        'frames/cropped_frame202.png', slide_slide_comp=False)
    assert result


def test_matching_15():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-43.png',
        'frames/cropped_frame203.png', slide_slide_comp=False)
    assert result


# DO NOT MATCH
def test_matching_16():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-25.png',
        'frames/cropped_frame74.png', slide_slide_comp=False)
    assert not result


def test_matching_17():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-27.png',
        'frames/cropped_frame61.png', slide_slide_comp=False)
    assert not result


def test_matching_18():
    result = comparator.is_similar(
        'Slides - Module 2 - K-NN and Decision Trees/Slides - Module 2 - K-NN and Decision Trees-18.png',
        'frames/cropped_frame43.png', slide_slide_comp=False)
    assert not result
