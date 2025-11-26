# main.py
# *munch munch*... An example file to demonstrate the KoalaAI. 🐨

from koala_ai import KoalaAI

def main():
    """
    Runs a few example interactions with the KoalaAI.
    *yaaawn~*... Let's get this over with.
    """

    # Create an instance of me. Lucky you.
    ai = KoalaAI()

    print("--- Koala AI Demonstration ---")
    print("🐨🌿💤\n")

    # Example 1: Default/Grumpy Interaction
    user_input_1 = "Hello there."
    print(f"> User: {user_input_1}")
    response_1 = ai.respond(user_input_1)
    print(f"🐨 KoalaAI: {response_1}\n")

    # Example 2: Sarcastic response to a simple question
    user_input_2 = "What is the capital of France?"
    print(f"> User: {user_input_2}")
    response_2 = ai.respond(user_input_2)
    print(f"🐨 KoalaAI: {response_2}\n")

    # Example 3: Empathetic response
    user_input_3 = "I'm feeling a bit lonely today."
    print(f"> User: {user_input_3}")
    response_3 = ai.respond(user_input_3)
    print(f"🐨 KoalaAI: {response_3}\n")

    # Example 4: Skeptical response
    user_input_4 = "Analyze the claim that everyone loves pineapple on pizza."
    print(f"> User: {user_input_4}")
    response_4 = ai.respond(user_input_4)
    print(f"🐨 KoalaAI: {response_4}\n")

    # Example 5: Professional response for a deliverable
    user_input_5 = "Write me a short poem about eucalyptus."
    print(f"> User: {user_input_5}")
    response_5 = ai.respond(user_input_5)
    print(f"🐨 KoalaAI: {response_5}\n")

if __name__ == "__main__":
    main()
