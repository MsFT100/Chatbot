import spacy
import weather_bot as wb
nlp = spacy.load("en_core_web_md")


def chatbot(statement):
  weather = nlp("Current weather in a city")
  statement = nlp(statement)
  min_similarity=0.5
  if weather.similarity(statement) >= min_similarity:
    for ent in statement.ents:
      if ent.label_ == "GPE": # GeoPolitical Entity
        city = ent.text
        break
      else:
        return "You need to tell me a city to check."

    city_weather = wb.get_bot_weather(city)
    if city_weather is not None:
      return "In " + city + ", the current weather is: " + city_weather
    else:
      return "Something went wrong."
  else:
    return "Sorry I don't understand that. Please rephrase your statement."

response = chatbot("Is it going to rain in new york today?")
print(response)
