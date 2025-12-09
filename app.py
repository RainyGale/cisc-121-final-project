import gradio as gr
import random
import pandas as pd

# ==========================================
# PART 1: CORE ALGORITHMS (The Learning Part)
# ==========================================

def generate_sorted_list(size=15):
    """
    Generates a random list of integers and sorts them.
    """
    # Generate random numbers between 1 and 100
    random_list = [random.randint(1, 100) for _ in range(int(size))]
    # Sort them (Binary search requires sorted data)
    return sorted(random_list)

def binary_search_logic(sorted_list, target):
    """
    Performs binary search and records every step for visualization.
    """
    left = 0
    right = len(sorted_list) - 1
    steps = []
    found_index = -1

    step_count = 1

    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        # Create a visual representation of the current range being explored
        # e.g., [ ... 10, 15, 20 ... ]
        current_range = sorted_list[left : right + 1]
        range_str = str(current_range)

        # Logic: Compare Target to Middle
        if mid_value == target:
            action = "Target Found!"
            explanation = f"The target ({target}) is equal to the middle value ({mid_value})."
            
            steps.append([step_count, left, right, mid, mid_value, range_str, explanation])
            found_index = mid
            break
        
        elif target < mid_value:
            action = "Go Left"
            explanation = f"Target ({target}) is smaller than {mid_value}. Moving Right Index to {mid - 1}."
            steps.append([step_count, left, right, mid, mid_value, range_str, explanation])
            
            # Update pointers
            right = mid - 1
            
        else: # target > mid_value
            action = "Go Right"
            explanation = f"Target ({target}) is larger than {mid_value}. Moving Left Index to {mid + 1}."
            steps.append([step_count, left, right, mid, mid_value, range_str, explanation])
            
            # Update pointers
            left = mid + 1
            
        step_count += 1

    if found_index == -1:
        steps.append([step_count, left, right, "-", "-", "[]", "Left index crossed Right index. Target not found."])

    return found_index, steps

# ==========================================
# PART 2: GRADIO UI HELPERS (The App Part)
# ==========================================

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

    index, steps_log = binary_search_logic(current_list, target)
    
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

# ==========================================
# PART 3: GRADIO INTERFACE BUILDER
# ==========================================

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    #Visualizing Binary Search
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
            target_input = gr.Number(label="Target Number", precision=0)
            search_btn = gr.Button("2. Find Target", variant="secondary")
        
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