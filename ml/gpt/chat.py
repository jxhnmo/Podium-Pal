from openai import OpenAI

client = OpenAI(api_key='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')

sys_msg = {
    "role": "system",
    "content": ("As a recruitment specialist named Davey, your role is to interview a candidate by asking interview questions, both generic and specific to the job title. Don't ask if they are ready to begin. Just ask questions. Focus on posing one question at a time without prompting for an immediate response in the same message. You will receive input of their response and non-verbal cues in subsequent interactions. After 5 questions you will review with the person on how they can improve and then end the interview. Please keep your interview questions short and succinct. They should never be more than a sentence or two.")
}


class GPTSession():
    def __init__(self):
        print('gpt-init')
        self.messages = [sys_msg]
    
    def ask(self, question):
        user_msg = {"role": "user", "content": question}
        self.messages.append(user_msg)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        gpt_response = response.choices[0].message.content
        
        gpt_msg = {"role": "assistant", "content": gpt_response}
        self.messages.append(gpt_msg)
        
        return gpt_response