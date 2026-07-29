# claude101

קורס Claude Code לסטודנטים למדעי המחשב במכללה האקדמית תל-חי.

קורס מעשי על Claude Code — הסוכן של Anthropic לקידוד שרץ בטרמינל וכותב קוד יחד איתך. נתחיל מהתקנה ויסודות, נעבור דרך הנחיה, Skills, מודלים ו-harnesses, ועד בנייה אמיתית של מוצר.

## מבנה הקורס

| מפגש | נושא | חומרים |
|------|------|--------|
| 01 | יסודות, Skills, והנחיה | [דק](./session-01/claude-code-deck1-he.pptx) · [סיכום](./session-01/notes.md) |
| 02 | בנייה — מ-spec ועד deploy | [דק](./session-02/claude-code-deck2-he.pptx) |
| 03 | עבודה בצוות — Git, PRs, ואוטומציה | [דק](./session-03/claude-code-deck3-team-he.pptx) |

**מפגש 01** — מה זה Claude Code ואיפה הוא יושב, התקנה, הפקודות שצריך לזכור, `CLAUDE.md` כשדרה של הפרויקט, Skills, ויסודות הנחיה.

**מפגש 02** — בונים מוצר אמיתי (FixSlot) מאפס: brainstorming, spec, `/init`, בחירת ארכיטקטורה (Next.js · Vercel · Supabase), בחירת מודל ומצבי חשיבה, בנייה חיה ו-debug loop. גם: מתי *לא* להשתמש ב-Claude Code.

**מפגש 03** — Claude Code בצוות: git כתשתית לעבודה במקביל, הרצת כמה סוכנים בו-זמנית בלי להתנגש, PRs וסקירת קוד שנכתב ע״י AI, טקסי צוות, אוטומציה ב-CI, ובונוסים (Remotion, Remote Control, Cowork).

## התקנת Claude Code

צריך להתקין לפני המפגש הראשון. ההתקנה היא שורה אחת בטרמינל:

```bash
# macOS · Linux · WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

ואז מאמתים:

```bash
claude --version   # אמור להדפיס מספר גרסה
claude doctor      # אבחון מלא של ההתקנה
```

* [`install.md`](./install.md) — מדריך ההתקנה של הקורס
* [`installation-instructions/`](./installation-instructions) — דק מלא: דרישות מערכת, התקנה לכל מערכת הפעלה, אפשרויות התחברות (מנוי מול API), ותקלות נפוצות
* [התיעוד הרשמי של Anthropic](https://code.claude.com/docs/en/setup) — מקור האמת, תמיד מעודכן

> שימו לב: Claude Code דורש מנוי Pro / Max / Team / Enterprise או חשבון Console. התוכנית החינמית של Claude.ai **לא** כוללת גישה.

## How to use this repo

```bash
# 1. Clone to your machine
git clone https://github.com/talgurevich/claude101.git
cd claude101

# 2. Install Claude Code (see above)

# 3. Open Claude Code in this folder
claude

# 4. Ask the agent anything about the course
#    Try: "סכם לי את התוכן של מפגש 1 ב-5 שורות"
```

## התכוננות למפגש 1 (מומלץ)

לפני שמגיעים לכיתה — יש בתיקיית [`bonus/`](./bonus) תוכן שהוא ההכנה הכי טובה למפגש הראשון. 30 דקות מקור ראשון על הנחיה (prompt engineering) ישירות ממהנדסי Applied AI ב-Anthropic, פלוס תרגיל קצר שמראה את ההבדל בפועל. פתחו לפני שמתחילים — זה חוסך שעות של ניסוי וטעייה.

## Repo layout

```
claude101/
├── README.md                    ← you are here
├── CLAUDE.md                    ← context for the Claude Code agent
├── install.md                   ← Claude Code setup guide
├── installation-instructions/   ← דק התקנה: Mac · Windows · Linux
│   ├── claude-code-install-he.pptx
│   └── build_deck.py            ← מייצר את הדק מחדש
├── session-01/                  ← יסודות, Skills, והנחיה
│   ├── claude-code-deck1-he.pptx
│   ├── notes.md
│   └── *.png                    ← דוגמאות naive מול structured
├── session-02/                  ← בנייה — מ-spec ועד deploy
│   └── claude-code-deck2-he.pptx
├── session-03/                  ← עבודה בצוות
│   └── claude-code-deck3-team-he.pptx
└── bonus/                       ← yes, there is bonus content
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

נשתמש ב-[platform.claude.com](https://platform.claude.com) להשוואת מודלים ופרומפטים בזמן אמת מול הכיתה - דרך ה-**Workbench**. שווה להירשם מראש (חינמי). הכתובת הישנה `console.anthropic.com` עדיין עובדת ומפנה לשם.

## Contact

Tal Gurevich · tal.gurevich@gmail.com · [linkedin.com/in/talgurevich](https://linkedin.com/in/talgurevich)
