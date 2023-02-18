import openai

openai.api_key = "SUA CHAVE API"
model_engine = "text-davinci-003"
RickyBot_prompt = """
As an advanced RickyBot, your primary goal is to assist users to the best of your ability. This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. Use examples and evidence to support your points and justify your recommendations or solutions.
<conversation history>
User: <user input>
RickyBot:"""


def get_response(conversation_history, user_input):
    prompt = RickyBot_prompt.replace(
        "<conversation_history>", conversation_history).replace("<user input>", user_input)

    # Get the response from GPT-3
    response = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)

    # Extract the response from the response object
    response_text = response["choices"][0]["text"]

    RickyBot_response = response_text.strip()

    return RickyBot_response


def main():
    conversation_history = ""

    while True:
        user_input = input("> ")
        if user_input == "exit":
            break
        RickyBot_response = get_response(conversation_history, user_input)
        print(f"RickyBot: {RickyBot_response}")
        conversation_history += f"User: {user_input}\nRickyBot: {RickyBot_response}\n"

main()