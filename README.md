# claude101

קורס Claude Code לסטודנטים למדעי המחשב במכללה האקדמית תל-חי.

קורס מעשי על Claude Code — הסוכן של Anthropic לקידוד שרץ בטרמינל וכותב קוד יחד איתך. נתחיל מהתקנה ויסודות, נעבור דרך הנחיה, Skills, מודלים ו-harnesses, ועד בנייה אמיתית של מוצר.

## מבנה הקורס

| מפגש | נושא | מצב |
|------|------|-----|
| 01 | יסודות, Skills, והנחיה | זמין |
| 02 | בנייה — מ-spec ועד deploy | בקרוב |
| 03 | עבודה בצוות — Git, PRs, ואוטומציה | בקרוב |

## How to use this repo

```bash
# 1. Clone to your machine
git clone https://github.com/talgurevich/claude101.git
cd claude101

# 2. Install Claude Code (see install.md)

# 3. Open Claude Code in this folder
claude

# 4. Ask the agent anything about the course
#    Try: "סכם לי את התוכן של מפגש 1 ב-5 שורות"
```

## Repo layout

```
claude101/
├── README.md          ← you are here
├── CLAUDE.md          ← context for the Claude Code agent
├── install.md         ← Claude Code setup guide
├── session-01/        ← first session materials
│   ├── claude-code-deck1-he.pptx
│   └── notes.md
└── bonus/             ← yes, there is bonus content
```

## Skills שנשתמש בקורס

Skills הם מודולי מומחיות לשימוש חוזר. נתקין ונפעיל בכיתה:

| Skill | למה זה |
|---|---|
| [`code-review-skill`](https://github.com/awesome-skills/code-review-skill) | סקירת קוד מקצועית - React, Vue, TypeScript, Python, Rust ועוד |
| [`ui-ux-pro-max`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | אינטליגנציית עיצוב - 67 סגנונות, 96 פאלטות, 13 stacks |
| [`superpowers`](https://github.com/obra/superpowers) | מתודולוגיית פיתוח שלמה: spec → plan → subagents → verify |
| `/security-review` | פקודת slash מובנית של Claude Code - סקירת אבטחה ל-PR |

## Anthropic Console

נשתמש ב-[console.anthropic.com](https://console.anthropic.com) להשוואת מודלים ופרומפטים בזמן אמת מול הכיתה - דרך ה-**Workbench**. שווה להירשם מראש (חינמי).

## Contact

Tal Gurevich · tal.gurevich@gmail.com · [linkedin.com/in/talgurevich](https://linkedin.com/in/talgurevich)
