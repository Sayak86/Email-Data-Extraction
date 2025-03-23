import os,json

PROMPT_DIR = "Prompts"
file_path = os.path.join("..",PROMPT_DIR, "PromptSelector.json")
def get_prompt_file(prompt_name):
    # read the file PromptSelector.json
    with open(file_path) as f:
        data = json.load(f)
    # get the prompt file name from the alias
    prompt_file = data[prompt_name] 
    return prompt_file

def load_prompt(prompt_file):
    """Load a prompt from a file in the prompts directory."""
    file_path = os.path.join("..",PROMPT_DIR, f"{prompt_file}")
    if not os.path.exists(file_path):
        return f"Error: Prompt file {prompt_file} not found."

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
def format_prompt(prompt_name, variables):
    """Load and format a prompt with dynamic variables."""
    prompt_file = get_prompt_file(prompt_name)
    prompt_template = load_prompt(prompt_file)
    return prompt_template.format(**variables)

