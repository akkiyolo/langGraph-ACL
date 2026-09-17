from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()


class State(TypedDict):
    message: str


def greeting(state: State) -> State:
    """this function greets people to ACL"""

    return {
        "message": state["message"] + " Welcome to AI Carrier Lab!"
    }


builder = StateGraph(State)

builder.add_node("greeting", greeting)

builder.add_edge(START, "greeting")
builder.add_edge("greeting", END)

graph = builder.compile()