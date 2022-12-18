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
  query = input("Ask a question or type 'help' for a list of commands: ")

  # Check if the user wants to see the list of commands
  if query == "help":
    print("Commands:")
    print("- help: show this list of commands")
    print("- quit: exit the program")
    continue

  # Check if the user
