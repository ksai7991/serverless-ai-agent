import openai
from flask_assistants import FlaskAssistants

def main(args):
      name = args.get("name", "stranger")
      greeting = "Thanks for the update, " + name + "!"
      print(greeting)
      return {"body": greeting}