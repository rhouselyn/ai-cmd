# AI-CMD: Integrate GPT with Windows Terminal

**AI-CMD** is an innovative project designed to seamlessly integrate GPT capabilities with the Windows terminal, enabling users to directly ask questions and generate command-line code using natural language. By leveraging an OpenAI proxy, AI-CMD offers accessibility without the need for a VPN, simplifying the process of tackling terminal-related queries and automating command generation.

## Getting Started

### Installation
1. Clone the project from GitHub:
   ```
   git clone https://github.com/rhouselyn/ai-cmd
   ```
2. Navigate to the project directory and run the setup:
   ```
   cd ai-cmd
   python setup.py
   ```
3. Add the project directory to your system's PATH environment variable:
   - On Windows, search for "Edit the system environment variables" > Environment Variables > System Variables > PATH > Add the project path.

### Configuration
- In `config.py`, input your `api_key`.
- You can specify your preferred model and language settings for a tailored experience.

## Usage

### Asking Questions
- Use `ask` followed by your question in the terminal. AI-CMD will automatically fetch the context from the terminal, process the inquiry with GPT, and generate a response. If the response contains terminal commands, they are automatically extracted and copied to the clipboard. A brief screen flash indicates the use of a virtual keyboard for copying and processing, ensuring the clipboard's content is promptly cleared afterwards.

### Generating Commands
- Typing `gen` followed by a directive in the terminal prompts GPT to translate it into a command, which is then copied to the clipboard. If GPT is unsure about the task, it responds with "UNKNOWN: please try another instruction." For potentially hazardous operations, it adds a cautionary note: "CAUTION: This command is dangerous!"

This project draws inspiration from the [cli-gpt](https://github.com/MagicCube/cli-gpt?tab=readme-ov-file) project, adopting its approach to prompt design for effective and intuitive user interactions. Enjoy a smoother, more interactive terminal experience with AI-CMD, where powerful GPT integration meets the convenience of command-line operations.
