import marimo

__generated_with = "0.17.0"
app = marimo.App(auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# AI/LLM Engineering Kick-off""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    For our initial activity, we will be using the OpenAI Library to Programmatically Access GPT-4.1-nano!

    In order to get started, you'll need an OpenAI Key. [here](https://platform.openai.com)!
    """
    )
    return


@app.cell
def _():
    import os
    import openai

    # Read API key from OpenAI_key.txt file
    with open("OpenAI_key.txt", "r") as f:
        api_key = f.read().strip()

    os.environ["OPENAI_API_KEY"] = api_key
    openai.api_key = os.environ["OPENAI_API_KEY"]
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Our First Prompt

    You can reference OpenAI's [documentation](https://platform.openai.com/docs/api-reference/chat) if you get stuck!

    Let's create a `ChatCompletion` model to kick things off!

    There are three "roles" available to use:

    - `developer`
    - `assistant`
    - `user`

    OpenAI provides some context for these roles [here](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages)

    Let's just stick to the `user` role for now and send our first message to the endpoint!

    If we check the documentation, we'll see that it expects it in a list of prompt objects - so we'll be sure to do that!
    """
    )
    return


@app.cell
def _():
    from openai import OpenAI

    client = OpenAI()
    return OpenAI, client


@app.cell
def _(client):
    YOUR_PROMPT = "What is the difference between the LangChain and LlamaIndex?"

    client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[{
            "role": "user",
            "content": YOUR_PROMPT
        }]
    )
    return (YOUR_PROMPT,)


@app.cell
def _(mo):
    mo.md(
        r"""
    As you can see, the prompt comes back with a tonne of information that we can use when we're building our applications!

    We'll be building some helper functions to pretty-print the returned prompts and to wrap our messages to avoid a few extra characters of code!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""##### Helper Functions""")
    return


@app.cell
def _(OpenAI):
    from IPython.display import display, Markdown

    def get_response(client: OpenAI, 
                     messages: str, 
                     model: str = "gpt-4.1-nano") -> str:
        return client.chat.completions.create(
            model=model,
            messages=messages
        )

    def system_prompt(message: str) -> dict:
        return {
            "role": "developer",
            "content": message
        }

    def assistant_prompt(message: str) -> dict:
        return {
            "role": "assistant",
            "content": message
        }

    def user_prompt(message: str) -> dict:
        return {
            "role": "user",
            "content": message
        }

    def pretty_print(message: str) -> str:
        display(Markdown(message.choices[0].message.content))
    return (
        assistant_prompt,
        display,
        get_response,
        pretty_print,
        system_prompt,
        user_prompt,
    )


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Testing Helper Functions

    Now we can leverage OpenAI's endpoints with a bit less boiler plate - let's rewrite our original prompt with these helper functions!

    Because the OpenAI endpoint expects to get a list of messages - we'll need to make sure we wrap our inputs in a list for them to function properly!
    """
    )
    return


@app.cell
def _(YOUR_PROMPT, client, get_response, pretty_print, user_prompt):
    messages = [user_prompt(YOUR_PROMPT)]

    chatgpt_response = get_response(client, messages)

    pretty_print(chatgpt_response)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Let's focus on extending this a bit, and incorporate a `developer` message as well!

    Again, the API expects our prompts to be in a list - so we'll be sure to set up a list of prompts!

    >REMINDER: The `developer` message acts like an overarching instruction that is applied to your user prompt. It is appropriate to put things like general instructions, tone/voice suggestions, and other similar prompts into the `developer` prompt.
    """
    )
    return


@app.cell
def _(client, get_response, pretty_print, system_prompt, user_prompt):
    list_of_prompts = [
        system_prompt("You are irate and extremely hungry."),
        user_prompt("Do you prefer crushed ice or cubed ice?")
    ]

    irate_response = get_response(client, list_of_prompts)

    pretty_print(irate_response)
    return (list_of_prompts,)


@app.cell
def _(mo):
    mo.md(r"""Let's try that some prompt again, but modify only our system prompt!""")
    return


@app.cell
def _(client, get_response, list_of_prompts, pretty_print, system_prompt):
    list_of_prompts[0] = system_prompt("You are joyful and having an awesome day!")

    joyful_response = get_response(client, list_of_prompts)

    pretty_print(joyful_response)
    return (joyful_response,)


@app.cell
def _(mo):
    mo.md(r"""While we're only printing the responses, remember that OpenAI is returning the full payload that we can examine and unpack!""")
    return


@app.cell
def _(joyful_response):
    print(joyful_response)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Prompt Engineering

    Now that we have a basic handle on the `developer` role and the `user` role - let's examine what we might use the `assistant` role for.

    The most common usage pattern is to "pretend" that we're answering our own questions. This helps us further guide the model toward our desired behaviour. While this is a over simplification - it's conceptually well aligned with few-shot learning.

    First, we'll try and "teach" `gpt-4.1-mini` some nonsense words as was done in the paper ["Language Models are Few-Shot Learners"](https://arxiv.org/abs/2005.14165).
    """
    )
    return


@app.cell
def _(client, get_response, pretty_print, user_prompt):
    list_of_prompts_1 = [
        user_prompt("Write a brief text on climate change.")
    ]

    stimple_response = get_response(client, list_of_prompts_1)
    pretty_print(stimple_response)
    return


@app.cell
def _(client, get_response, pretty_print, user_prompt):
    list_of_prompts_2 = [
        user_prompt("Write a brief text on climate change as vice ganda in a talk show.")
    ]

    stimple_response_2 = get_response(client, list_of_prompts_2)
    pretty_print(stimple_response_2)
    return


@app.cell
def _(mo):
    mo.md(r"""### ❓ Activity #1: Play around with the prompt using any techniques from the prompt engineering guide.""")
    return


@app.cell
def _(mo):
    prompt_input = mo.ui.text(
        label="Enter your prompt",
        value="Write a brief text on climate change as vice ganda in a talk show.",
        full_width=True
    )
    return (prompt_input,)


@app.cell
def _(display, prompt_input):
    display(prompt_input)
    return


@app.cell
def _(client, get_response, pretty_print, prompt_input, user_prompt):
    if prompt_input.value:

        list_of_prompts_5 = [

            user_prompt(prompt_input.value)

        ]

        stimple_response_5 = get_response(client, list_of_prompts_5)

        pretty_print(stimple_response_5)
    return


@app.cell
def _(mo):
    mo.md(r"""### Few-shot Prompting""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    As you can see, the model is unsure what to do with these made up words.

    Let's see if we can use the `assistant` role to show the model what these words mean.
    """
    )
    return


@app.cell
def _(assistant_prompt, client, get_response, pretty_print, user_prompt):
    list_of_prompts_3 = [
        user_prompt("Something that is 'stimple' is said to be good, well functioning, and high quality. An example of a sentence that uses the word 'stimple' is:"),
        assistant_prompt("'Boy, that there is a stimple drill'."),
        user_prompt("A 'falbean' is a tool used to fasten, tighten, or otherwise is a thing that rotates/spins. An example of a sentence that uses the words 'stimple' and 'falbean' is:")
    ]

    stimple_response_3 = get_response(client, list_of_prompts_3)
    pretty_print(stimple_response_3)
    return


@app.cell
def _(mo):
    mo.md(r"""As you can see, leveraging the `assistant` role makes for a stimple experience!""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Chain of Thought

    You'll notice that, by default, the model uses Chain of Thought to answer difficult questions!

    > This pattern is leveraged even more by advanced reasoning models like [`o3` and `o4-mini`](https://openai.com/index/introducing-o3-and-o4-mini/)!
    """
    )
    return


@app.cell
def _(client, get_response, pretty_print, user_prompt):
    reasoning_problem = """
    how many r's in "strawberry?" {instruction}
    """

    list_of_prompts_4 = [
        user_prompt(reasoning_problem)
    ]

    reasoning_response = get_response(client, list_of_prompts_4)
    pretty_print(reasoning_response)
    return (reasoning_problem,)


@app.cell
def _(mo):
    mo.md(r"""Notice that the model cannot count properly. It counted only 2 r's.""")
    return


@app.cell
def _(mo):
    mo.md(r"""### ❓ Activity #2: Update the prompt so that it can count correctly.""")
    return


@app.cell
def _(
    assistant_prompt,
    client,
    get_response,
    pretty_print,
    reasoning_problem,
    user_prompt,
):
    list_of_prompts_6 = [
        user_prompt(reasoning_problem),
        assistant_prompt("There are 2 r's in 'strawberry.'"),
        user_prompt(reasoning_problem.replace("{instruction}", "Now I want you to spell out each letter, and count the r's carefully."))
    ]

    reasoning_response_2 = get_response(client, list_of_prompts_6)
    pretty_print(reasoning_response_2)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Conclusion

    Now that you're accessing `gpt-4.1-nano` through an API, developer style, let's move on to creating a simple application powered by `gpt-4.1-nano`!
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Materials adapted for PSI AI Academy. Original materials from AI Makerspace.""")
    return


if __name__ == "__main__":
    app.run()
