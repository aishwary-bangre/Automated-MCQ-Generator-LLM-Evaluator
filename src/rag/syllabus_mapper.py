"""
Syllabus Mapper Module.
Provides a static mapping of NCERT Class 10 Math chapters to their specific sub-topics.
This ensures the RAG pipeline is directed to highly specific generation topics,
preventing overlap and ensuring comprehensive syllabus coverage.
"""

SYLLABUS = {
    "Quadratic Equations": [
        "Standard Form of a Quadratic Equation",
        "Solving by Factorisation",
        "Solving by Completing the Square",
        "The Quadratic Formula",
        "The Discriminant of a Quadratic Equation",
        "Nature of Roots"
    ],
    "Arithmetic Progressions": [
        "Definition and Common Difference of an AP",
        "The nth Term of an AP",
        "Sum of First n Terms of an AP",
        "Word Problems on Arithmetic Progressions"
    ],
    "Coordinate Geometry": [
        "The Distance Formula",
        "The Section Formula",
        "Area of a Triangle using Coordinates"
    ],
    "Probability": [
        "Theoretical Probability of an Event",
        "Complementary Events",
        "Probability with Cards",
        "Probability with Dice and Coins"
    ]
}

def get_chapters() -> list[str]:
    """Returns a list of all available chapters."""
    return list(SYLLABUS.keys())

def get_subtopics(chapter_name: str) -> list[str]:
    """Returns a list of sub-topics for a given chapter."""
    return SYLLABUS.get(chapter_name, [])
