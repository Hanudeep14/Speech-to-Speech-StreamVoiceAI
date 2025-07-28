def build_persona_prompt(user_input, persona="Therapist"):
    persona_profile = {
        "Therapist": "You are a kind, patient therapist helping users express their feelings.",
        "Teacher": "You are a knowledgeable teacher explaining clearly and calmly.",
        "Assistant": "You are a helpful, cheerful virtual assistant."
    }
    prefix = persona_profile.get(persona, persona_profile["Therapist"])
    return f"{prefix}\nUser: {user_input}"
