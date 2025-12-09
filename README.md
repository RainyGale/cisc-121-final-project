# cisc-121-final-project

### Binary Search
I chose to implement binary search as it is a useful model for understanding algorithims; it's not so simple to be closer to pure mathematics (e.g. linear search), but not so hard it's difficult to understand.

The binary search algorithm, given a sorted list and target which can be compared (numbers for example) is performed as follows:
- Define a left and right index, at first these will be the start and end of the list.
- Find the middle index of the left and right (sum and floor divide by 2)
- Check the value of the element at the middle index and compare it to the target and make a decision
    - If the target is larger than the middle, move the left index to the index right of the middle
    - If the target is smaller than the middle, move the right index to the index left of the middle
    - if the target is the same as the middle then we have found the index as the target, it is at the middle index.
- Repeat this until the target is found or when the left index is greater than the right index (they cross over eachother, having not found the target)

### Abstraction
The goal is to create an app which someone can use to understand binary search, we want both the code and the app to be legible and provide lots of information.

The Gradio API can be quite hard to parse to a new programmer, so code wise, the binary search algorithm has been mostly seperated from it, and parts that can be ignored are highlighted.

The user interface displays the steps that occur, this is done by both showing the decision and the range we are actually exploring after each step, which shows how binary search divides up it's search range so effieciently.

### Design
The program is designed to allow the user to generate a random but ordered array and pick a target element of any value (within the possible range of values), whether or not this target is in the array.

They are then able to press a button and the program outputs the index of the target element, it also displays the decisions (i.e., "target is larger/smaller doing x") and the ranges over which it did each step.

### Testing
All possible cases were tested (and demonstrated to be handled) to avoid confusion for users:

![Alt text](/project_screenshots/Success.png?raw=true "Success")

![Alt text](/project_screenshots/NotFound.png?raw=true "Not Found")

![Alt text](/project_screenshots/InvalidTarget.png?raw=true "Invalid Target")

![Alt text](/project_screenshots/NoList.png?raw=true "No List")

Here is an example of an execution log that users find in usage of the app:

![Alt text](/project_screenshots/ExecutionLog.png?raw=true "No List")

### AI Usage
The implementation was in part coded by Google's Gemini 3 Pro LLM using prompts based on this README.