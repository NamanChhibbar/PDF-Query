from configs import OPENAI_KEY, OPENAI_MODEL
from utils import PDFQuery

def main() -> None:

  print('Press Ctrl-D to exit the program at any moment. Enter "CHANGE PATH" to change the PDF.', end='\n\n')

  try:
    while True:

      pdf_path = input('Enter the path to the PDF file: ')

      try:
        pdf_query = PDFQuery(
          openai_key=OPENAI_KEY,
          openai_model=OPENAI_MODEL,
          pdf_path=pdf_path
        )
      except:
        print('Invalid path. Please try again.', end='\n\n')
        continue

      print('PDF loaded!', end='\n\n')

      while True:
          
        query = input('Enter your query: ')
        print()

        if query == 'CHANGE PATH':
          break

        response = pdf_query.query(query)
        print(response, end='\n\n')
  
  except EOFError:
    print('\n\nExiting the program...', end='\n\n')

main()
