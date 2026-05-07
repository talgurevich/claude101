# Installing Claude Code

This guide gets you from zero to running Claude Code on your machine.

## What you need

1. An Anthropic account — sign up at [claude.ai](https://claude.ai)
2. A terminal (Terminal.app on Mac, WSL on Windows, any terminal on Linux)
3. Node.js 18+ (most CS students already have this)

> Official guide (always up to date): [docs.claude.com/en/docs/claude-code/setup](https://docs.claude.com/en/docs/claude-code/setup)

## Mac / Linux

```bash
npm install -g @anthropic-ai/claude-code
```

Then start it:

```bash
claude
```

First run will prompt you to log in. Follow the link, sign in to Anthropic, paste the token back.

## Windows

Use WSL2 (Windows Subsystem for Linux):

1. Install WSL2 — [Microsoft guide](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Open Ubuntu (or your WSL distro)
3. Run the Linux command above

## Verify it works

```bash
cd ~/Desktop
mkdir test-claude && cd test-claude
claude
```

In the prompt, ask:

```
מה יש בתיקייה הזאת?
```

The agent should say the folder is empty. That's success.

## First real test (in this repo)

After cloning:

```bash
git clone https://github.com/talgurevich/claude101.git
cd claude101
claude
```

Then ask:

```
סכם לי את התוכן של מפגש 1 ב-5 שורות
```

The agent reads `CLAUDE.md` and the session files, then gives a real summary.

## Common errors

**`command not found: claude`**
The install didn't update your PATH. Open a new terminal window, or `source ~/.zshrc` (Mac) / `source ~/.bashrc` (Linux).

**Authentication / login token issues**
`claude logout` then `claude` again. Re-authenticate from scratch.

**Hebrew renders as `???` or boxes**
Your terminal font doesn't support Hebrew. On Mac: Terminal → Preferences → Profiles → Text → change to a font with Hebrew coverage (Menlo, Monaco, SF Mono).

## Stuck?

Bring the error to class, or message me. Don't lose an hour to setup — that's not the point.
