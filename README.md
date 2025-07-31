
# MetaGPT: Modular Multi-Agent System

## Project Background

**MetaGPT** is based on the research paper ["MetaGPT: Meta Programming for Multi-Agent Collaborative Framework"](https://arxiv.org/abs/2308.00352v7). The paper demonstrates that software development can be automated and scaled by organizing Large Language Models (LLMs) into structured, role-based multi-agent teams. Inspired by real-world software teams, metaGPT agents each take on a professional role (e.g., Product Manager, Project Manager, Architect, Engineer, QA Engineer) and collaborate in a workflow that mirrors enterprise software engineering.

This implementation adapts the metaGPT research framework to a command-line tool, using the latest **Groq LLMs** (for example, `llama-3.3-70b-versatile`). The design is modular—agents, pipeline, LLM interface, and CLI are clearly separated—making it extensible and easy to experiment with orchestration or alternative LLMs.

## Repository Structure

```csharp
metaGPT/
│
├── agents/
│   ├── base_agent.py
│   ├── product_manager.py
│   ├── project_manager.py
│   ├── architect.py
│   ├── engineer.py
│   ├── qa_engineer.py
│   └── __init__.py
│
├── llm/
│   ├── base_llm.py
│   └── groq_llm.py
│
├── core/
│   ├── pipeline.py
│   ├── task.py
│   └── utils.py
│
├── cli/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_agents.py
│
├── requirements.txt
├── .env
└── README.md

```

## Component Responsibilities

|Folder/File|Purpose|
|---|---|
|`agents/`|Agent role classes: Product Manager, Project Manager, Architect, Engineer, QA Engineer (all based on `BaseAgent`).|
|`llm/`|LLM abstraction and Groq API integration.|
|`core/`|Pipeline orchestration, task structure, and utilities.|
|`cli/`|User-facing command-line entry point.|
|`tests/`|Pytest-based tests for key components.|
|`requirements.txt`|Python dependencies.|
|`.env`|Groq API key and sensitive configuration.|
|`README.md`|Project overview and instructions (what you're reading now).|

## MetaGPT as a CLI Solution: Implementation Journey

The original MetaGPT research explores agent-based workflow, but presents it as a conceptual orchestration (not as a package/repo). This CLI implementation makes the following enhancements:
- **Modular Codebase**: Each professional role is a class, and all share a unified `BaseAgent`.
- **Groq LLM Integration**: Uses up-to-date supported Groq models (e.g., `llama-3.3-70b-versatile`) with a switchable LLM backend.
- **Pipeline Orchestration**: Agent outputs are piped in sequence, matching the metaGPT paper’s workflow—requirements → work breakdown → architecture → code → QA.
- **Command-Line Interface**: The entire process is controlled through a CLI (with Typer), allowing real-time input and output.
- **Testing**: Includes unit and integration tests using pytest to ensure extensibility and reliability.

## Setup and Usage Instructions

1. Clone the Repository
```bash
git clone <your-repo-url>  # Replace with your repository URL
cd metaGPT
```

2. Create and Activate a Virtual Environment (recommended)
```bash
python -m venv venv
source venv/bin/activate         # On Windows: venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure the Groq API Key
	1. Register for a Groq LLM account (if you don’t have one) to obtain an API key.
	2. Create a `.env` file in the project directory and add the API key, like this:
```env
GROQ_API_KEY=your-groq-api-key-here
```

5. Update the model name (if required)
	In `llm/groq_llm.py`, ensure that the `model` value is set to a currently supported Groq model, e.g.
```python
"model": "llama-3.3-70b-versatile",
```
Check Groq documentation or dashboard for the latest recommended model names.

6. Run the CLI
```bash
python -m cli.main
```
**Tip:** Instead of `python cli/main.py`, using `-m` resolves imports correctly.

7. Using the CLI
- On launch, you’ll see a welcome prompt and be asked to enter a project idea.
- The CLI will orchestrate the agent team:
    1. **Product Manager** — requirements, user scenarios, user stories (displayed under “Product Requirements”).
    2. **Project Manager** — task breakdown, schedule, assignment, progress table (displayed under “Project Plan”).
    3. **Architect** — system architecture and module decomposition.
    4. **Engineer** — code or pseudocode implementation of modules.
    5. **QA Engineer** — test cases, validation strategies, and bug report template.
- Each section will be printed after completion.


8. Example Run
	Please feel free to look at `SampleOutputs` for some examples.

9. Run tests using `pytest`
