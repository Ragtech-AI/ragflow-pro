# Contributing to RAGFlow Pro

Welcome to RAGTech Solutions! This guide will help you get started as a contributing developer.

## Development Workflow

1. **Pick an Issue**: Browse [GitHub Issues](https://github.com/ramansrivastava/ragflow-pro/issues) and pick one that matches your skill level
2. **Create Branch**: `git checkout -b feature/issue-#-short-description`
3. **Develop**: Implement your solution following our coding standards
4. **Test**: Write tests and ensure all tests pass
5. **Pull Request**: Submit a PR with clear description
6. **Code Review**: Address feedback from maintainers
7. **Merge**: After approval, your code will be merged

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### Setup Development Environment
```bash
# Clone and setup backend
git clone https://github.com/ramansrivastava/ragflow-pro.git
cd ragflow-pro
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Setup frontend
npm install

# Run tests
pytest backend/tests/
npm test
```

## Coding Standards

### Python (Backend)
- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for classes and functions
- Maximum line length: 100 characters
- Use Black for code formatting: `black backend/`

### TypeScript (Frontend)
- Use TypeScript for all new files
- Follow React best practices
- Use functional components with hooks
- Use ESLint and Prettier for formatting

### Git Commit Messages
- Use conventional commits: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Example: `feat(api): add semantic search scoring`

## Testing Requirements

### Backend Tests
- Write unit tests for all new functions
- Aim for >80% test coverage
- Use pytest fixtures for setup
- Mock external dependencies

### Frontend Tests
- Write unit tests for components
- Test user interactions with React Testing Library
- Snapshot tests for UI components

## Issue Labels

- 🐛 `bug` - Something isn't working
- ✨ `enhancement` - New feature or request
- 📚 `documentation` - Improvements to docs
- 🚀 `performance` - Performance improvements
- 🧪 `testing` - Adding missing tests
- 🔧 `maintenance` - Code maintenance

## Priority Levels
- 🔴 **High**: Critical bugs, security issues
- 🟡 **Medium**: Features, enhancements
- 🟢 **Low**: Nice-to-have features, refactoring

## Questions?
Feel free to comment on issues or reach out to the maintainers!