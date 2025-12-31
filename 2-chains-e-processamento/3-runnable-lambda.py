from langchain_core.runnables import RunnableLambda

# This helpful when you can't change the existing functions by adding @chain decorator

def parse_number(text: str) -> int:
    return int(text.strip())

parse_runnable = RunnableLambda(parse_number)

number = parse_runnable.invoke("10")

print(number + 5)