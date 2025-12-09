import gradio as gr
import random
import pandas as pd

# ============================ BINARY SEARCH ============================

# create sorted lists for binary search to use
def generate_sorted_list(size=15):
    list_size = int(size)
    
    LOWER_BOUND = 1
    UPPER_BOUND = 200 

    if list_size > (UPPER_BOUND - LOWER_BOUND + 1): # this case is unreachable because the user cannot change size, but be aware if you wish to modify the code.
        raise ValueError("Cannot generate list size with unique numbers in the defined range.")
    
    random_list = random.sample(range(LOWER_BOUND, UPPER_BOUND + 1), list_size)
    
    # sort list
    return sorted(random_list)

# binary search, code related to steps and explanation can be ignored in understanding the algorithm.
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    steps = []
    # we start the found_index at -1 so we can check to see if it's still that by the end (meaning we didn't find the target)
    found_index = -1

    step_count = 1

    while left <= right:
        # calculate middle index
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        # create a visual representation of the current range being explored
        current_range = sorted_list[left : right + 1]
        range_str = str(current_range)

        if mid_value == target:
            explanation = f"The target ({target}) is equal to the middle value ({mid_value})."   
            steps.append([step_count, left, right, mid, mid_value, range_str, explanation])

            found_index = mid
            break
        elif target < mid_value:

            explanation = f"Target ({target}) is smaller than {mid_value}. Moving Right Index to {mid - 1}."
            steps.append([step_count, left, right, mid, mid_value, range_str, explanation])
            
            right = mid - 1
        else: # target > mid_value
            explanation = f"Target ({target}) is larger than {mid_value}. Moving Left Index to {mid + 1}."
            steps.append([step_count, left, right, mid, mid_value, range_str, explanation])
    
            left = mid + 1
            
        step_count += 1

    if found_index == -1: # we never found it
        steps.append([step_count, left, right, "-", "-", "[]", "Left index crossed Right index. Target not found."])

    return found_index, steps

# ============================ GRADIO HELPER FUNCTIONS ============================

def update_search(target, current_list):
    """
    Bridge function between the UI inputs and the binary search logic.
    """
    if not current_list:
        return "Please generate a list first!", pd.DataFrame()
    
    if target is None:
        return "Please enter a valid number.", pd.DataFrame()

    try:
        target = int(target)
    except ValueError:
        return "Please enter a valid integer target.", pd.DataFrame()

    index, steps_log = binary_search(current_list, target)
    
    # Format the result message
    if index != -1:
        result_msg = f"### ✅ Success! Target found at index {index}."
    else:
        result_msg = f"### ❌ Target {target} is not in the list."

    # Convert steps to a nice DataFrame for display
    headers = ["Step", "Left Idx", "Right Idx", "Mid Idx", "Mid Value", "Current Search Range", "Decision"]
    df = pd.DataFrame(steps_log, columns=headers)
    
    return result_msg, df

def create_new_list_ui():
    """Generates a new list and updates the display"""
    new_list = generate_sorted_list()
    return new_list, f"**Current Sorted List:** {new_list}"

# ============================ GRADIO UI ============================

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # Visualizing Binary Search
    Binary search is an efficient algorithm for finding an item from a sorted list of items. 
    It works by continually cutting down a range over which the target could not be.
    """)

    # --- State Management (Stores the list in memory) ---
    list_state = gr.State([])

    # --- Section 1: Data Generation ---
    with gr.Row():
        with gr.Column(scale=1):
            generate_btn = gr.Button("1. Generate New Random List", variant="primary")
        with gr.Column(scale=3):
            list_display = gr.Markdown("**Current List:** (Click generate to start)")

    gr.HTML("<hr>") # Visual separator

    # --- Section 2: Search Controls ---
    with gr.Row():
        with gr.Column(scale=1):
            target_input = gr.Number(label="2. Set Target Number", precision=0)
            search_btn = gr.Button("3. Find Target", variant="secondary")
        
        with gr.Column(scale=3):
            result_output = gr.Markdown("### Ready to search...")

    # --- Section 3: Visualization ---
    gr.Markdown("### Step-by-Step Execution Log")
    steps_output = gr.Dataframe(
        headers=["Step", "Left Idx", "Right Idx", "Mid Idx", "Mid Value", "Current Search Range", "Decision"],
        datatype=["number", "number", "number", "number", "number", "str", "str"],
        interactive=False,
        wrap=True
    )

    # --- Event Listeners ---
    # When "Generate" is clicked -> Run create_new_list_ui -> Update state and display
    generate_btn.click(
        fn=create_new_list_ui, 
        inputs=None, 
        outputs=[list_state, list_display]
    )

    # When "Find" is clicked -> Run update_search -> Update result text and dataframe
    search_btn.click(
        fn=update_search,
        inputs=[target_input, list_state],
        outputs=[result_output, steps_output]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()