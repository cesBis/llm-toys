import os
import time
from google import genai

image_dir = os.path.join(os.getcwd(), "images")
image_names = sorted(os.listdir(image_dir))
image_paths = [os.path.join(image_dir, name) for name in image_names]

client = genai.Client()  # GEMINI_API_KEY already defined

for image_path in image_paths:
    # see https://ai.google.dev/gemini-api/docs/image-understanding#inline-image
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()

    print("submitting " + image_path)

    attempts = 1
    while attempts > 0:
        print("attempt " + str(attempts))
        try:
            response = client.models.generate_content(
                model="gemma-4-31b-it",
                contents=[
                    genai.types.Part.from_bytes(
                        data=image_data, mime_type="image/jpeg"
                    ),
                    """
                    extract the table from this image into markdown format.
                    there might be two tables.
                    only produce text that is verbatim from within the table.

                    here's an example of the sort of output I want.


        **Domain:** English/Language Arts  
        **Learning Outcome:** Early learners develop foundational skills in understanding alphabetic awareness, phonological awareness, concepts of print, and comprehension.  
        **Standard:** ELA 2.2: Demonstrate phonological awareness

        | Developmental Continuum from birth to prekindergarten | Infant | Younger Toddler | Older Toddler | Younger Preschool | Older Preschool | Kindergarten Standard |
        | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
        | **Indicators: Competencies that indicate a child is progressing toward kindergarten readiness.** | Orient to sounds in the learning environment | Begin to engage in word and sound play with adults | | Demonstrate basic knowledge of letter-sound correspondence | | K.RF.4 Identify and produce rhyming words. |
        | | Discriminate sounds in the learning environment | Repeat words that contain similar-sounding phonemes (pig-dig, cat-mat) | Distinguish between words that contain similar-sounding phonemes (pig-dig, cat-mat) | Engage in rhyming games and songs; can recognize a familiar rhyme | | K.RF.5 Orally pronounce, blend, and segment words into syllables. |
        | | | | | Identify rhyming words in spoken language | Make rhymes to simple words | K.RF.6 Indentify and produce the beginning, middle (medial), and final sounds in three and four phoneme words. |
        | | | | | Orally blend and segment familiar compound words, with modeling and support | Blend and segment syllables in spoken words with modeling and support | |
        | | | | | Demonstrate awareness of sounds as separate units | Isolate the initial sound in some words | |

        **Domain:** English/Language Arts  
        **Learning Outcome:** Early learners develop foundational skills in understanding alphabetic awareness, phonological awareness, concepts of print, and comprehension.  
        **Standard:** ELA 2.3: Demonstrate awareness and understanding of concepts of print

        | Developmental Continuum from birth to prekindergarten | Infant | Younger Toddler | Older Toddler | Younger Preschool | Older Preschool | Kindergarten Standard |
        | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
        | **Indicators: Competencies that indicate a child is progressing toward kindergarten readiness.** | Look at books while an adult holds and manipulates the book | Bring book to adult to read | Recognize familiar books by cover | Begin to understand that books are comprised of written words | Understand that print carries meaning | K.RF.1 Demonstrate understanding that print moves from left to right across the page and from top to bottom. |
        | | Begin to hold and manipulate a book with adult support | Hold and manipulate a book independently | Recite parts of well-known stories, rhymes, songs | Respond to and interact with read-alouds of literary and informational text | Track words in a book from left to right, top to bottom, and page to page with adult support | K.RF.2 Recognize that written words are made up of sequences of letters. |
        | | Respond to songs | Pretend to read familiar books | Hold books with two hands and turn pages | Hold books right side up and turn pages left to right | | K.RF.9 Orally read decodable texts with appropriate accuracy and automaticity. |
        | | Listen to repetition of familiar words, songs, signs, rhymes, and stories | Attend to pictures and text for several minutes | | | | |


                    """,
                ],
            )
            attempts = 0
        except:
            attempts += 1
            time.sleep(5)

    print("writing output")

    with open("out.md", "a") as f:
        if response.text:
            f.write(response.text)

    print("cooling down...")
    time.sleep(4)

client.close()
