# Installing Claude Code

This is the short guide. The full version — system requirements, every install
method per OS, login options, and a troubleshooting table — is the course deck:
[`installation-instructions/claude-code-install-he.pptx`](./installation-instructions).

Official docs (always the source of truth): [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup)

## Before you start

| | |
|---|---|
| **OS** | macOS 13+ · Windows 10 1809+ · Ubuntu 20.04+ · Debian 10+ · Alpine 3.19+ |
| **Hardware** | 4GB RAM+ · x64 or ARM64 · working internet from a supported country |
| **Account** | Pro · Max · Team · Enterprise · or a Console account |
| **Terminal** | Bash · Zsh · PowerShell · CMD (ripgrep ships with Claude Code) |

> The free Claude.ai plan does **not** include Claude Code. If login fails, check this first.

## macOS / Linux

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

This is the native installer and it updates itself in the background. Homebrew
(`brew install --cask claude-code`) also works but does not auto-update.

## Windows

```powershell
# PowerShell
irm https://claude.ai/install.ps1 | iex
```

```bat
:: CMD
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

These are two different commands. If your prompt starts with `PS C:\` you are in
PowerShell. On WSL, use the Linux command above.

Install [Git for Windows](https://gitforwindows.org) so Claude Code can use Bash —
without it, it falls back to PowerShell.

## Verify it worked

```bash
claude --version   # prints a version number, e.g. 2.1.211 (Claude Code)
claude doctor      # read-only diagnosis: install health, config errors, fixes
claude             # starts a session; first run opens a browser to log in
```

`claude` runs in the directory you are standing in. Always `cd` into your project
first — that folder is what it can see.

## Logging in

Two ways, and you pick one on first run:

- **Claude.ai subscription** (Pro / Max / Team / Enterprise) — log in with your
  normal claude.ai account. Flat monthly cost. This is what most students use.
- **Claude Console** — usage-based billing against the API. Your org admin has to
  invite you first.

Useful commands: `/login` (switch account) · `/logout` · `/status` (who am I).

> **Common trap:** if `ANTHROPIC_API_KEY` is set in your environment, it overrides
> your subscription and you get billed per token. To go back: `unset ANTHROPIC_API_KEY`,
> then `/status` to confirm.

## First real test (in this repo)

```bash
git clone https://github.com/talgurevich/claude101.git
cd claude101
claude
```

Then ask:

```
סכם לי את התוכן של מפגש 1 ב-5 שורות
```

The agent reads `CLAUDE.md`, finds the session files, and gives you a real summary.
If it does, your install is working.

## Common errors

**`command not found: claude`**
PATH wasn't updated in the terminal you have open. Open a new window, or
`source ~/.zshrc` (Mac) / `source ~/.bashrc` (Linux).

**`403`, or `syntax error near unexpected token '<'`**
`curl` got an error page instead of the script. Check your network or proxy, then
use an alternative install method from
[troubleshoot-install](https://code.claude.com/docs/en/troubleshoot-install).

**`The token '&&' is not a valid statement separator`**
You ran the CMD command inside PowerShell. They are different commands — check
whether your prompt starts with `PS C:\`.

**Hebrew renders as `???` or boxes**
Your terminal font has no Hebrew coverage. On Mac: Terminal → Settings → Profiles
→ Text, pick Menlo or SF Mono.

> **Never `sudo npm install -g`.** It creates permission problems, it's a security
> risk, and it's a common cause of a broken install.

## More

| | |
|---|---|
| Full install docs | [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup) |
| Quickstart — your first session | [code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart) |
| Install & login troubleshooting | [code.claude.com/docs/en/troubleshoot-install](https://code.claude.com/docs/en/troubleshoot-install) |
| Terminal guide — if you're new to the terminal | [code.claude.com/docs/en/terminal-guide](https://code.claude.com/docs/en/terminal-guide) |
| Auth, including Bedrock and Vertex | [code.claude.com/docs/en/authentication](https://code.claude.com/docs/en/authentication) |

## Stuck?

Bring the error to class, or message me. Don't lose an hour to setup — that's not
the point of the course.
