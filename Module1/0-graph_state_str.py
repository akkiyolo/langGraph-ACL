# importing libraries

from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()


# node
def greeting(state: str) -> str:
    """This function greets people to AI Career Lab."""
    return state + " Welcome to AI Career Lab!"


# create graph
builder = StateGraph(str)

# add node
builder.add_node("greeting", greeting)

# add edges
builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

# compile graph
graph = builder.compile()


# test the graph with a string
result = graph.invoke("Hey I am new!")

print(result)