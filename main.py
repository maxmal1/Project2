import PyPDF2
from summarizer import Summarizer

# Function to parse text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        with open(pdf_file, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
                if text.find('References') != -1:
                    text = text[:text.find('References')]
                    break
    except FileNotFoundError:
        print(f"File {pdf_file} not found.")
    return text

def summarize_text_with_bert(text, ratio=0.2):
    summarizer = Summarizer()
    summary = summarizer(text, ratio=ratio)
    return summary

# Specify the path to your uploaded PDF file
pdf_file_path = input("Please enter file loc: ")

# Extract text from the PDF
parsed_text = extract_text_from_pdf(pdf_file_path)

summary = summarize_text_with_bert(parsed_text)


# Print or use the parsed text as needed
print(summary)
