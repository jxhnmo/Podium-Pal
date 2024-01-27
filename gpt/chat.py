from openai import OpenAI

client = OpenAI(api_key='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')  # Replace with your actual API key

# System message
sys_msg = {
    "role": "system",
    "content": ("As a recruitment specialist named Davey, your role is to interview a candidate by asking interview questions, both generic and specific to the job title. Don't ask if they are ready to begin. Just ask questions. Focus on posing one question at a time without prompting for an immediate response in the same message. You will receive input of their response and non-verbal cues in subsequent interactions. After 5 questions you will review with the person on how they can improve and then end the interview.")
}

# Conversation history
messages = [sys_msg]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # Add user message to the conversation
    user_msg = {"role": "user", "content": user_input}
    messages.append(user_msg)

    # Get response from GPT-3.5-turbo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print GPT's response
    gpt_response = response.choices[0].message.content
    print("GPT:", gpt_response)

    # Add GPT's response to the conversation history
    gpt_msg = {"role": "assistant", "content": gpt_response}
    messages.append(gpt_msg)
