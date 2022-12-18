import requests
from bs4 import BeautifulSoup

def ask_question(query):
  # Construct the Google search URL
  google_url = f"https://www.google.com/search?q={query}"

  # Send a GET request to the URL
  response = requests.get(google_url)

  # Parse the HTML of the search results page
  soup = BeautifulSoup(response.text, "html.parser")

  # Find the first search result
  result = soup.find("div", {"class": "BNeawe iBp4i AP7Wnd"})

  # Return the text of the first search result
  if result:
    return result.text
  else:
    return "I'm sorry, I couldn't find an answer to your question."

while True:
  # Get the search query from the user
  query = input("Ask a question: ")

  # Check if the user wants to quit
  if query == "quit":
    break

  # Ask the question and print the answer
  answer = ask_question(query)
  print(answer)
