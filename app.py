import gradio as gr

def string_fun(text):
    text = text.strip()
    if not text:
        return "⚠️ Please enter some text!"
    
    reversed_text = text[::-1]
    words = len(text.split())
    chars = len(text)
    return (
        f"🔁 Reversed: {reversed_text}\n\n"
        f"🧮 Word Count: {words}\n"
        f"🔡 Character Count: {chars}"
    )
demo = gr.Interface(
    fn=string_fun,
    inputs=gr.Textbox(lines=2, placeholder="Type anything here...", label="Enter Text"),
    outputs=gr.Textbox(label="Result"),
    title="String Fun App 🎨",
    description="Reverse your text and count words — built with Python + Gradio!",
)
if __name__ == "__main__":
    demo.launch()