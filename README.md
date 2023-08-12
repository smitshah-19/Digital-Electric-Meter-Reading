# Digital Electric-meter Reading

In the era of advance technology, everything is shifting towards automation through the usage of AI, ML, Computer Vision etc. This project is solely realted to the field of computer vision and how with the help of computer vision, the meaningful information from digital images, videos or other visual inputs can be extracted using Python and other tools of python. This file will breif you about how meaningful information like readings from a digital electric meter can be extracted using OCR (Optical Character Recognition). 

### Optical Character Recognition (OCR)
Optical character recognition (OCR) refers to the use of technological methods in order to differentiate printed or handwritten textual characters inside digital representations of physical documents, such as scanned paper documents. The fundamental procedure of Optical Character Recognition (OCR) is the analysis of textual content inside a document and the subsequent conversion of characters into a coded format suitable for data manipulation and analysis.

#### How OCR works?
**1. Image Acquisition:** The process begins with acquiring an image containing the text you want to extract. This image can be a scanned document, a photograph, or any other type of image with visible text.

**2. Preprocessing:** The acquired image might contain various imperfections like noise, distortion, or uneven lighting that can affect OCR accuracy. Preprocessing steps include tasks like noise reduction, image enhancement, rotation correction, and binarization (converting the image to black and white).

**3. Segmentation:** The image is analyzed to identify individual characters, words, and lines of text. This process is known as segmentation, where the software tries to isolate different components of the text.

**4. Feature Extraction:** For each segmented character or word, the OCR software extracts features that help distinguish different characters or symbols. These features might include information about strokes, edges, curves, and more.

**5. Character Recognition:** Using the extracted features, the OCR software compares the character or word segments against a database of known characters. This database can include various fonts, styles, and languages. Pattern recognition algorithms are used to match the extracted features with the characters in the database.

**6. Language Modeling:** In cases where the OCR software needs to recognize whole words or sentences, language modeling techniques are applied. This involves considering the likelihood of certain words or combinations of words appearing in the given language.

**7. Post-processing:** After the characters or words are recognized, post-processing steps are performed to correct errors and enhance accuracy. This can include tasks like spell-checking, grammar correction, and context-based correction.

**8. Output:** The final output of the OCR process is machine-readable text that can be further processed, indexed, searched, or manipulated using various software applications.

Here is an example how the meter readings from the image is extracted using OCR. 
