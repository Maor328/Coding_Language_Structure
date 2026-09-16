# a. Pure text processing functions
def spaces_clean(text):
    return text.strip()

def text_capitalize(text):
    return text.title()

def stars_add(text):
    return f"***{text}***"

# b. Pipeline management
def pipeline_create():
    # Returns the identity function
    return lambda x: x

def add_to_pipeline(pipeline_fn, new_fn):
    # Returns a new function composing both functions without loops or recursion
    return lambda x: new_fn(pipeline_fn(x))

# c. Main script to build and execute the pipeline
pipeline = pipeline_create()
pipeline = add_to_pipeline(pipeline, spaces_clean)
pipeline = add_to_pipeline(pipeline, text_capitalize)
pipeline = add_to_pipeline(pipeline, stars_add)

while True:
    user_text = input("enter text:\n")
    
    # Check for empty or spaces-only input
    if not user_text or user_text.isspace():
        print("invalid input")
        break  # Exit the loop when input is empty/invalid
    else:
        print(pipeline(user_text))