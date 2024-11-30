from openai import OpenAI
from pypdf import PdfReader


def extract_text(pdf_path: str) -> str:

    # Create a PdfReader object
    reader = PdfReader(pdf_path)

    text = '-' * 100
    for page in reader.pages:

      # Extract text from the page
      page_text = page.extract_text()
      page_text = page_text.strip()

      # Append the text to the final text
      text = f'{text}\n\n{page_text}'

    return text


class PDFQuery:

  SYSTEM_MESSAGE = 'You will reeceive a query and text from a PDF. The query is followed by the text extracted from the PDF and is separated by multiple dashes ("-"). Your task is to answer the query based on the text. If the query cannot be answered, respond with "Sorry, I didn’t understand your question. Do you want to connect with a live agent?"'

  def __init__(
    self,
    openai_key: str,
    openai_model: str
  ) -> None:
    
    self.openai_client = OpenAI(api_key=openai_key)
    self.openai_model = openai_model
  
  def query(
    self,
    query: str,
    pdf_path: str
  ) -> str:

    pdf_text = extract_text(pdf_path)

    prompt = f'{query}\n\n{pdf_text}'

    completion = self.openai_client.chat.completions.create(
      model=self.openai_model,
      messages=[
        {'role': 'system', 'content': PDFQuery.SYSTEM_MESSAGE},
        {'role': 'user', 'content': prompt}
      ]
    )

    return completion.choices[0].message.content
