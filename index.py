import gradio as gr
import openai
from gradio.components import Textbox

openai.api_key = "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"

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, " \
         "and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by Julius. How can I help you " \
         "today?\nHuman:"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


# noinspection PyPep8
def create_prompt(prompt):
    # noinspection PyPep8
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[restart_sequence, start_sequence]
    )

    message = response.choices[0].text
    return message


def conversation_history(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = create_prompt(inp)
    history.append((input, output))
    return history, history


def chat_ui():
    history = []

    def send_message(inp):
        if inp:
            history.append(("You", inp))
            output = create_prompt('\n'.join([start_sequence] + [h[1] for h in history]))
            history.append(("AI", output))
        else:
            output = "Please type a message"
        return output, history

    input_field = Textbox(lines=2, placeholder="Type your message here...", label=None)   # input field
    output_field = Textbox(lines=2, label=None)       # output field

    chat_interface = gr.Interface(
        fn=send_message,
        inputs=input_field,
        outputs=output_field,
        title="Personal Bot",
        description="Talk to an AI created by Julius",
        theme="default",
        examples=[["Hi!"], ["What's the weather like?"], ["Tell me a joke"]]
    )
    return chat_interface


if __name__ == "__main__":
    chat_ui().launch(debug=True)

