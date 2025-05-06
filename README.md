# Murder Mystery Workshop

Welcome to the Murder Mystery Workshop! This interactive workshop combines the excitement of solving a murder mystery with the power of AI and programming. You'll be working with Jupyter notebooks to solve puzzles, analyze clues, and interact with AI agents to crack the case.

## 🎯 Workshop Overview

In this workshop, you'll:
- Work with AI agents to solve a murder mystery
- Learn about AI agent interactions and problem-solving
- Practice your Python programming skills
- Experience the power of AI-assisted development

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Poetry (Python package manager)
- Git

### Installing Poetry

Install Poetry using pip:
```bash
pip install poetry
```

Verify the installation:
```bash
poetry --version
```

### Environment Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/tokentek/moe-workshop.git
   cd moe-workshop
   ```

2. **Install dependencies using Poetry**
   ```bash
   poetry install --no-root
   ```

3. **Set up your environment variables**
   - Copy `.env.example` to `.env`
   - Fill in your API keys:
     ```
     API_KEY_OAI=<your-openai-api-key>
     ENDPOINT_GPT4O=<your-endpoint>
     ```

4. **Open the project in Cursor/VS Code**
   - Open Cursor/VS Code
   - Open the `moe-workshop` folder
   - Make sure you have the Jupyter extension installed

5. **Verify your setup**
   - Open `moe_nb.ipynb` in Cursor/VS Code
   - Run all cells to verify that your environment is set up correctly
   - If all cells execute without errors, you're ready to start the workshop!

   > **Note:** If you can't find the correct Poetry kernel in your notebook:
   > ```bash
   > poetry run python -m ipykernel install --user --name moe-workshop --display-name "Python (moe-workshop)"
   > ```
   > After running this command, restart your IDE and try again.

6. **Begin the workshop**
   - Open `murder_mystery.ipynb`
   - Follow the instructions in the notebook to begin your investigation

## 📚 Workshop Structure

The workshop is organized into several sections:
1. Introduction to the case
2. Setting up your investigation tools
3. Interacting with AI agents
4. Solving puzzles and collecting evidence
5. Drawing conclusions and solving the mystery

## 🛠️ Tools and Technologies

This workshop uses:
- Python 3.12+
- Jupyter Notebooks
- OpenAI API
- AutoGen framework

## 💡 Tips for Success

- Read each cell carefully before executing
- Take notes as you progress
- Don't hesitate to experiment with different approaches
- Use the AI agents as your investigative partners
- Save your work regularly


Happy investigating! 🕵️‍♂️




