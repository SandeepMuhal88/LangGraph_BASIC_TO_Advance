from langgraph.graph import StateGraph,START,END
from typing import TypedDict



class BMIState(TypedDict):
    weight_kg:float
    height_m:float
    bmi: float


# Define your function
def calculate_BMI(state:BMIState)->BMIState:
    weight_kg=state['weight_kg']
    height_m= state['height_m']
    bmi= weight_kg/(height_m**2)

    state['bmi']=round(bmi,2)

    return state


#define you graph 

graph.StateGraph(BMIState)
graph.add_node("calculatore_bmi",calculate_BMI)

graph.add_edge(START,'calculate_bmi')
graph.add_edge('calculate_bmi',END)

workflows=graph.compile()

initial_state={'weight_kg':80,'height_m':1.73}

final_state=workflows.invoke(initial_state)

print(final_state)