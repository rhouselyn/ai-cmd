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
3. Add the project directory to your system's PATH environment variable (or copy the dictionary in output of setup.py):
   - As for how to find the PATH environment variable, refer to [this](https://support.esri.com/zh-cn/knowledge-base/edit-an-environment-variable-1462478594981-000002146)

### Configuration
- In `config.py`, input your `api_key`.
- You can specify your preferred model and language settings for a tailored experience.

## Usage

### Asking Questions
- Use `ask` followed by your question in the terminal. AI-CMD will automatically fetch the context from the terminal, process the inquiry with GPT, and generate a response.
   > ![image](imgs/309721819-07c22102-83b9-4b20-b084-b17f963d7351.png)
- You don't need to worry about consuming too much tocken, it will only intercept instructions from back to front until it exceeds 500 words.
- A brief screen flash indicates the use of a virtual keyboard for copying and processing, ensuring the clipboard's content is promptly cleared afterwards.
- If the response contains terminal commands, they are automatically extracted and copied to the clipboard so that you can paste directly to the terminal.
   > ![image](imgs/309722418-29360a4c-0ffa-4a63-9522-bb47b91b2ed0.png)

### Generating Commands
- Typing `gen` followed by a directive in the terminal prompts GPT to translate it into a command, which is then copied to the clipboard.
- Connect multiple row operations using && or &
  > ![image](imgs/309721211-60b89883-3303-4fdf-b1c2-024e901f5eb6.png)

- If GPT is unsure about the task, it responds with
  > UNKNOWN: please try another instruction.
  ![image](imgs/309720831-dc76c452-4e89-4250-a516-f08bcf8e1f4e.png)

- For potentially hazardous operations, it adds a cautionary note:
  > CAUTION: This command is dangerous!
  ![image](imgs/309721026-40905fbe-3369-40e8-9962-9d8df8684ff8.png)

### error handling
- If the api speed limit is reached, the program automatically retries until it is lifted。
- Run time more than 15 seconds automatically exit the program

This project draws inspiration from the [cli-gpt](https://github.com/MagicCube/cli-gpt?tab=readme-ov-file) project, adopting its approach to prompt design for effective and intuitive user interactions. 
The document is basically written by chatGPT4.
Please Enjoy a smoother, more interactive terminal experience with AI-CMD, where powerful GPT integration meets the convenience of command-line operations.
