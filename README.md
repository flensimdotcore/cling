# CLI Commands Typing Trainer `Cling`

## Overview
Cling is an interactive tool designed to help users improve their proficiency in typing common command-line interface (CLI) commands. This trainer is useful for beginners learning terminal commands, as well as experienced users looking to keep their skill on point.

## Features
- Practice typing CLI commands for Git, Linux and other common platforms and tools
- Customizable command sets for personalized training.
- (in future) Progress tracking and performance statistics.

## Installation
To install the Cling, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/flensimdotcore/cling.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cling
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start a training session, run:
```bash
python3 cling/main.py
```

### Available Options
#### Options with multiple choices
- `--difficulty [easy|medium|hard]` - Choose difficulty levels.
- `--bank [linux|git|docker]` - Select specific command banks.
- `--category [developer]` - Select sets of banks based on their implications.

#### Options with single choice
- `--language [en|ru]` - Select an interface language

Example:
```bash
python3 cling/main.py --difficulty easy --bank git
```

```bash
Question: How to show changes in repository in Git?
Enter your command: git show changes
Wrong! Correct answers: git status
```

```bash
Question: How to show changes in repository in Git?
Enter your command: git status
Correct!
```

## Contributing
We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to your fork (`git push origin feature-name`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or suggestions, feel free to open an issue or contact flensim.core@yandex.ru.
