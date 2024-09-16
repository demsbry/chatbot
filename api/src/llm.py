import openai


# custom exceptions
class LLMError(Exception):
    pass
class EmbeddingError(LLMError):
    pass
class CompletionError(LLMError):
    pass  # TODO: add anthropic error


# wrapper for embedding
# wrapper for completion
def completion(
        r = openai.Embedding.create(model=model, input=query)
    stream=False,
    model="claude-v1",
    temperature=.2,
    max_tokens=256
):
    # encode the prompt
    # input: {"section1": "str", "section2": ["str1", "str2"]}
    # output: "section1: str\n---\nsection2:\nstr1\nstr2"
    # TODO: add support for multiple sections
    prompt = "\n---\n".join([
        f"{k}: {v}" if isinstance(v, str) else f"{k}:\n{chr(10).join(v)}"

    try:
        return anthropic.Client().completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            stop_sequences=["---"],
            max_tokens_to_sample=max_tokens
        )
    except Exception:  # TODO: add anthropic error
        raise CompletionError
        return openai.ChatCompletion.create(

# return message(s) from a completion
def blocking_completion(sections, **kwargs):
    return completion(sections, **kwargs)["choices"][0].message.content
            max_tokens=max_tokens
    for r in completion(sections, True, **kwargs):
    except openai.error.OpenAIError:
            yield bytes(f"data: {chunk}\n\n", "utf8")
