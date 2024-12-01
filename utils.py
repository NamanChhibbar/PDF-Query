from openai import OpenAI
from pypdf import PdfReader


def extract_text(pdf_path: str) -> str:

    # Create a PdfReader object
    reader = PdfReader(pdf_path)

    # Extract text from each page and strip whitespaces
    texts = [page.extract_text().strip() for page in reader.pages]

    # Join the text from all pages
    return '\n\n'.join(texts)


class PDFQuery:

  def __init__(
    self,
    openai_key: str,
    openai_model: str,
    pdf_path: str,
    negative_output: str
  ) -> None:
    
    # Initialize the OpenAI client
    self.openai_client = OpenAI(api_key=openai_key)
    self.openai_model = openai_model

    # Extract text from the PDF and create system prompt
    pdf_text = extract_text(pdf_path)
    self.system_prompt = f'You will receive a some queries and text from a PDF. Your task is to answer the query based on the text. If the query cannot be answered, respond with "{negative_output}"\n\nText from the PDF is:\n\n{pdf_text}'

    # Initialize previous messages
    self.messages = [{'role': 'system', 'content': self.system_prompt}]
  
  def query(
    self,
    query: str
  ) -> str:
    
    self.messages.append({'role': 'user', 'content': query})

    content = self.openai_client.chat.completions.create(
      model=self.openai_model,
      messages=self.messages
    ).choices[0].message.content

    self.messages.append({'role': 'assistant', 'content': content})

    return content
