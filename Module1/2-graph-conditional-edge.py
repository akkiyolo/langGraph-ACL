from langgraph.graph import StateGraph,START,END
from typing_extensions import TypedDict
from typing import Literal

class State(TypedDict):
  graph_str:str

def node1(state:State)->str:
  pass

def node2(state:State)->str:
  pass

def node3(state:State)->str:
  pass

