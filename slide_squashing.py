from slide_similarity import SlideComparator


# filter the slides in order to remove any transitions and squash similar slides
def squash_slides(slides_info):
    comparator = SlideComparator()
    slides = slides_info["slides"]
    num_slides = slides_info["num_slides"]
    squash_slides = []

    for slide_index in range(num_slides - 1):
        is_similar = comparator.is_similar(slides[slide_index], slides[slide_index + 1])
        new_slide_object = {}

        if (not is_similar):
            new_slide_object = {
                "path": slides[slide_index],
                "squashed": False,
            }
        else:
            new_slide_object = {
                "path": slides[slide_index],
                "squashed": True,
            }
        squash_slides.append(new_slide_object)
        print("Slide", slide_index, "- slide", slide_index + 1, ":", is_similar)

    # we always add the last slide as there can be no transition coming afterwards, and so it cant be squashed
    new_slide_object = {
        "path": slides[-1],
        "squashed": False,
    }
    squash_slides.append(new_slide_object)

    final_slides_json = {
        "num_slides": num_slides,
        "slides": squash_slides
    }

    # print(final_slides_json)
    return final_slides_json
