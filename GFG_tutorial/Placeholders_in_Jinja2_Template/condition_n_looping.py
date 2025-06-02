from jinja2 import Environment, FileSystemLoader
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'condition_n_looping')

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

# Load the template
template = env.get_template('index_template.html')

# Variables to pass
name = 'Manan'
email = 'Manan@example.com'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Render the template
rendered_form = template.render(pl_name=name, pl_email=email, numbers=numbers)

# Write the output
output_path = os.path.join(current_dir, 'index.html')  # Saves in main directory
with open(output_path, 'w') as output:
    output.write(rendered_form)

print(f"Template rendered successfully to {output_path}")