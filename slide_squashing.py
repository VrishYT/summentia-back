import json
from slide_similarity import SlideComparator

# filter the slides in order to remove any transitions and squash similar slides
def squash_slides(slides_info):
    comparator = SlideComparator()
    slides = slides_info["slides"]
    num_slides = slides_info["num_slides"]
    filtered_slides = []

    for slide_index in range(num_slides-1):
        score = comparator.get_similarity_score(slides[slide_index], slides[slide_index+1])
        if (not score):
            filtered_slides.append(slides[slide_index])
        print("Slide", slide_index, "- slide", slide_index+1, ":", score)
    #we always add the last slide as there can be no transition coming afterwards, and so it cant be squashed
    filtered_slides.append(slides[-1])
    filtered_slides_json = {
        "num_slides": len(filtered_slides),
        "slides": filtered_slides
    }
    print(filtered_slides_json)
    return filtered_slides_json
    

if __name__ == "__main__":
    slides_json = """{
        "num_slides": 97,
        "slides": [
            "output_image_page_1.png",
            "output_image_page_2.png",
            "output_image_page_3.png",
            "output_image_page_4.png",
            "output_image_page_5.png",
            "output_image_page_6.png",
            "output_image_page_7.png",
            "output_image_page_8.png",
            "output_image_page_9.png",
            "output_image_page_10.png",
            "output_image_page_11.png",
            "output_image_page_12.png",
            "output_image_page_13.png",
            "output_image_page_14.png",
            "output_image_page_15.png",
            "output_image_page_16.png",
            "output_image_page_17.png",
            "output_image_page_18.png",
            "output_image_page_19.png",
            "output_image_page_20.png",
            "output_image_page_21.png",
            "output_image_page_22.png",
            "output_image_page_23.png",
            "output_image_page_24.png",   
            "output_image_page_25.png",
            "output_image_page_26.png",
            "output_image_page_27.png",
            "output_image_page_28.png",
            "output_image_page_29.png",
            "output_image_page_30.png",
            "output_image_page_31.png",
            "output_image_page_32.png",
            "output_image_page_33.png",
            "output_image_page_34.png",
            "output_image_page_35.png",
            "output_image_page_36.png",
            "output_image_page_37.png",
            "output_image_page_38.png",
            "output_image_page_39.png",
            "output_image_page_40.png",
            "output_image_page_41.png",
            "output_image_page_42.png",
            "output_image_page_43.png",
            "output_image_page_44.png",
            "output_image_page_45.png",
            "output_image_page_46.png",
            "output_image_page_47.png",
            "output_image_page_48.png",
            "output_image_page_49.png",
            "output_image_page_50.png",
            "output_image_page_51.png",
            "output_image_page_52.png",
            "output_image_page_53.png",
            "output_image_page_54.png",
            "output_image_page_55.png",
            "output_image_page_56.png",
            "output_image_page_57.png",
            "output_image_page_58.png",
            "output_image_page_59.png",
            "output_image_page_60.png",
            "output_image_page_61.png",
            "output_image_page_62.png",
            "output_image_page_63.png",
            "output_image_page_64.png",
            "output_image_page_65.png",
            "output_image_page_66.png",
            "output_image_page_67.png",
            "output_image_page_68.png",
            "output_image_page_69.png",
            "output_image_page_70.png",
            "output_image_page_71.png",
            "output_image_page_72.png",
            "output_image_page_73.png",
            "output_image_page_74.png",
            "output_image_page_75.png",
            "output_image_page_76.png",
            "output_image_page_77.png",
            "output_image_page_78.png",
            "output_image_page_79.png",
            "output_image_page_80.png",
            "output_image_page_81.png",
            "output_image_page_82.png",
            "output_image_page_83.png",
            "output_image_page_84.png",
            "output_image_page_85.png",
            "output_image_page_86.png",
            "output_image_page_87.png",
            "output_image_page_88.png",
            "output_image_page_89.png",
            "output_image_page_90.png",
            "output_image_page_91.png",
            "output_image_page_92.png",
            "output_image_page_93.png",
            "output_image_page_94.png",
            "output_image_page_95.png",
            "output_image_page_96.png",
            "output_image_page_97.png"
        ]
    }
    """
    print(squash_slides(slides_json))
    
