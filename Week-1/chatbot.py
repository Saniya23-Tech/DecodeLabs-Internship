# Predefined rules (Used dictionary to store the rules)
# It is case-insensitive, partial match is allowed
rules = {
    "How are you?": "I'm doing well, thank you! How about you?",
    "who are you": "I am a simple chatbot created by predefined rules.",
    "What is AI": "AI stands for artificial intelligence, which refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
    "what is your name": "I am a pre-defined rule based chatbot",
    "Are you Intelligent": "No, I have no intelligence nor a learning capability.",
    "who made you": "A Saniya Developer created me by using Python programming using the logics",
    "sorry": "No problem! It's okay. How can I assist you today?",
    "Mood Off": "Why are you feeling down? Is there anything you can share with me?",
    "Tell me a joke": "You know developers code at night because bugs are attracted to light!",
}

# Predefined greetings list
greetings = ["hi", "hello", "hey", "listen", "good morning", "good afternoon", "good evening", "good night", "what's up"]

# Predefined exit commands list
exit_commands = ["exit", "quit", "bye", "good bye", "see you later"]


def get_clean_input():
    """Get user input and clean it by converting to lowercase and stripping whitespace."""
    raw = input("You: ")
    return raw.strip().lower()


def chatbot_response(user_input):
    """Generate a response based on user input using the if-else rules."""
    # Check for greetings
    if user_input in [g.lower() for g in greetings]:
        return "Hello! What about you?"

    # Check for exit commands
    if user_input in [e.lower() for e in exit_commands]:
        return "EXIT__SIGNAL"

    # Check for predefined rules (hashmap + partial match)
    for key, value in rules.items():
        if key.lower() in user_input:  # partial match
            return value

    # Default response if no rule matched
    return "I'm sorry, I can't assist with that. Have a great day!"


def main():
    """Main loop is the heartbeat of the chatbot"""
    print('Chatbot started. Say "hello" to interact with me or type "exit" to quit.')

    while True:
        user_input = get_clean_input()
        response = chatbot_response(user_input)  # decision logic

        if response == "EXIT__SIGNAL":
            print("BOT: Goodbye! Exiting now.")
            break
        else:
            print(f"BOT: {response}\n")


if __name__ == "__main__":
    main()
