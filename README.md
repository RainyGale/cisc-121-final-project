# cisc-121-final-project

# Binary Search

<video src="project_screenshots/DemoVideo.mp4" width="320" height="240" controls></video>

I chose to implement binary search as it is a useful model for understanding algorithims; it's not so simple to be closer to pure mathematics (e.g. linear search), but not so hard it's difficult to understand.

The binary search algorithm, given a sorted list and target which can be compared (numbers for example) is performed as follows:
- Define a left and right index, at first these will be the start and end of the list.
- Find the middle index of the left and right (sum and floor divide by 2)
- Check the value of the element at the middle index and compare it to the target and make a decision
    - If the target is larger than the middle, move the left index to the index right of the middle
    - If the target is smaller than the middle, move the right index to the index left of the middle
    - if the target is the same as the middle then we have found the index as the target, it is at the middle index.
- Repeat this until the target is found or when the left index is greater than the right index (they cross over eachother, having not found the target)

## Abstraction
The goal is to create an app which someone can use to understand binary search, we want both the code and the app to be legible and provide lots of information.

The Gradio API can be quite hard to parse to a new programmer, so code wise, the binary search algorithm has been mostly seperated from it, and parts that can be ignored are highlighted.

The user interface displays the steps that occur, this is done by both showing the decision and the range we are actually exploring after each step, which shows how binary search divides up it's search range so effieciently.

## Design
The program is designed to allow the user to generate a random but ordered array and pick a target element of any value (within the possible range of values), whether or not this target is in the array.

They are then able to press a button and the program outputs the index of the target element, it also displays the decisions (i.e., "target is larger/smaller doing x") and the ranges over which it did each step.

# Problem Breakdown
We need a sorted input array of some length with some range of elements. The length will be forced to 15 to reduce complexity for the user. Any target input will be permitted and edge cases will be handled so the user can explore invalid inputs to the algorithm. We will use python's sample function to avoid duplicate elements of the array, reducing complexity further.

We need to return the target element of the array using binary search. This has already been explored in the description for the algorithm. In python this algorithm is quite easy to implement.

## Testing
- All possible cases were tested (and demonstrated to be handled) to avoid confusion for users:

    - A valid target in the array:

    ![Alt text](/project_screenshots/Success.png?raw=true "Success")

    - A valid target not in the array:

    ![Alt text](/project_screenshots/NotFound.png?raw=true "Not Found")

    - An invalid target:

    ![Alt text](/project_screenshots/InvalidTarget.png?raw=true "Invalid Target")

    - No array:

    ![Alt text](/project_screenshots/NoList.png?raw=true "No List")

- Here is an example of an execution log that users find in usage of the app:
![Alt text](/project_screenshots/ExecutionLog.png?raw=true "No List")

## How to run
### Clone the repository and install gradio using pip with:
```
pip install gradio
```
or 
```
python -m pip install gradio
```
Then run 
```
python app.py
``` 
in the repository and follow the localhost link provided.

### Alternatively:
Follow the hugging face link to access the app: https://huggingface.co/spaces/rainygale/cisc-121-final-project

## Acknowledgement
The implementation was in part coded by Google's Gemini 3 Pro LLM using prompts based on this README.