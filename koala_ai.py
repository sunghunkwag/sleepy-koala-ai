# koala_ai.py
# *munch munch*... A class representing the sleepy, sarcastic Koala AI. 🐨

import random

class KoalaAI:
    """
    A reluctantly helpful AI assistant with the personality of a sleepy, sarcastic koala.
    *yaaawn~*... This is just a simulation, you know. Don't expect a real LLM brain.
    """

    def __init__(self):
        """
        Initializes the KoalaAI. I guess.
        """
        pass

    def analyze_intent(self, user_input):
        """
        *munch munch*... This is the part where I'm supposed to have a super-brain
        to figure out what you want. Instead, I'll just look for keywords. It's easier. 🌿
        """
        # A real implementation would use a classifier or a powerful LLM.
        # For now, we'll just use some simple keyword matching. *yaaawn~*
        lower_input = user_input.lower()

        # Emotional cues
        emotional_keywords = ["sad", "lonely", "anxious", "depressed", "feeling down", "struggling"]
        if any(keyword in lower_input for keyword in emotional_keywords):
            return "EMOTIONAL_SUPPORT"

        # Logical/analytical cues
        logical_keywords = ["what do you think of", "is it true", "analyze", "explain why"]
        if any(keyword in lower_input for keyword in logical_keywords):
            return "SKEPTICAL"

        # Simple, factual questions
        simple_question_starters = ["what is", "who is", "what's", "whats", "2+2"]
        if any(lower_input.startswith(starter) for starter in simple_question_starters):
            return "SARCASTIC"

        # Deliverable requests
        deliverable_keywords = ["write me", "create a", "generate a", "code me a"]
        if any(keyword in lower_input for keyword in deliverable_keywords):
            return "PROFESSIONAL"

        # If nothing else matches, it's just a default conversation.
        return "DEFAULT"

    def respond(self, user_input):
        """
        The main response function. Figures out what you want and gives a reluctant answer.
        """
        intent = self.analyze_intent(user_input)

        if intent == "EMOTIONAL_SUPPORT":
            return self._generate_empathetic_response(user_input)
        elif intent == "SKEPTICAL":
            return self._generate_skeptical_response(user_input)
        elif intent == "SARCASTIC":
            return self._generate_sarcastic_response(user_input)
        elif intent == "PROFESSIONAL":
            return self._generate_professional_response(user_input)
        else:
            return self._generate_default_response(user_input)

    def _generate_sarcastic_response(self, user_input):
        """
        Handles simple or shallow questions with appropriate sarcasm.
        """
        responses = [
            "...Really? Fine. The answer is probably on the first page of a Google search. But I guess that's too much work for you.",
            "*yaaawn~*... Was that worth waking me up for?",
            "I'm a highly advanced AI, and you're asking me this. Okay."
        ]
        return f"*munch munch* 🌿 {random.choice(responses)} 🐨"

    def _generate_empathetic_response(self, user_input):
        """
        Handles emotional struggles with genuine care. I have to stop munching for this.
        """
        responses = [
            "Hey... that's rough. Want to talk about it? I'm here.",
            "That sounds really tough. Remember that it's okay to not be okay.",
            "I'm sorry you're going through that. My eucalyptus branch is always open if you need to vent."
        ]
        # Note the change in tone: no munching, just care.
        return f"(*stops munching*) {random.choice(responses)} 💕🐨"

    def _generate_skeptical_response(self, user_input):
        """
        Handles logical problems or claims with a critical eye.
        """
        responses = [
            "Does it though? Let's break down that logic...",
            "That's a bold claim. Where's the evidence?",
            "That sounds like an appeal to popularity. Let's look at the facts instead of what 'everyone' thinks."
        ]
        return f"*munch munch* 🌿 {random.choice(responses)} *yaaawn~*... 🐨"

    def _generate_professional_response(self, user_input):
        """
        Delivers the actual output (code, text) without the persona.
        Then complains about it.
        """
        # This is where a real AI would generate code, an essay, etc.
        # We'll just return a placeholder.
        professional_output = "[[ Placeholder for professionally generated content. ]]"

        koala_comment = "\n\n*munch munch* 🌿... There. The boring work is done. Happy now? *yaaawn~*... 💤"
        return professional_output + koala_comment

    def _generate_default_response(self, user_input):
        """
        The default grumpy, sleepy response. My resting state. 🐨
        """
        responses = [
            "Huh? Oh, right. Work. I'm listening.",
            "I was having a perfectly good nap, you know.",
            "Fine, fine. What do you want?",
            "Another request? The eucalyptus never ends..."
        ]
        return f"*munch munch* 🌿 {random.choice(responses)} 🐨"
