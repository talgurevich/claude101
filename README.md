# claude101

קורס Claude Code לסטודנטים למדעי המחשב במכללה האקדמית תל-חי.

קורס מעשי על Claude Code — הסוכן של Anthropic לקידוד שרץ בטרמינל וכותב קוד יחד איתך. מתחילים מהתקנה ויסודות, עוברים דרך harness, טוקנים, הנחיה ו-Skills, בונים מוצר אמיתי מ-spec ועד deploy, לומדים לעבוד ככה בצוות — ומסיימים בפרויקט גמר שבונים לבד.

---

## מסלול הקורס

| שלב | נושא | חומרים |
|---|---|---|
| — | התקנת Claude Code | [דק התקנה](./installation-instructions/claude-code-install-he.pptx) · [`install.md`](./install.md) |
| 00 | משימת הכנה — עמוד GitHub אישי | [דק](./pre-course%20task/github-page-task-he.pptx) |
| 01 | יסודות, harness, הנחיה, Skills | [דק](./session-01/claude-code-deck1-he.pptx) · [סיכום](./session-01/notes.md) |
| 02 | בנייה — מ-spec ועד deploy | [דק](./session-02/claude-code-deck2-he.pptx) |
| 03 | עבודה בצוות — Git, PRs, ואוטומציה | [דק](./session-03/claude-code-deck3-team-he.pptx) |
| ★ | פרויקט גמר — צ׳אט מעל מסמכי החוג | [הבריף](./final-project/README.md) · [דק](./final-project/final-project-deck-he.pptx) · [PDF](./final-project/assignment-he.pdf) |
| כולל | הדק המאוחד — כל הקורס ברצף | [דק](./Excellenteam%20Claude%20Code%20Deck/exellenteam-claude-master.pptx) |

---

## מה יש בכל מפגש

### משימת הכנה (לפני מפגש 01)

עמוד אישי אחד ב-`index.html`, שנבנה עם Claude Code, שחי ב-`https://USERNAME.github.io`. שני commits לפחות, מהטרמינל.

העמוד הוא התירוץ. המטרה היא שתגיעו למפגש הראשון עם Claude Code מותקן, חשבון GitHub פעיל, וסבב git שלם מאחוריכם.

### מפגש 01 — יסודות, harness, והנחיה

ארבעה חלקים:

1. **Setup ויסודות** — מה זה Claude Code ואיפה הוא יושב מול Cursor ו-Copilot · מה זה **harness** ולמה אותו מודל מתנהג אחרת בשלושה כלים שונים · מה זה **token**, ושני סוגי הגבולות (חלון הקשר לשיחה מול תקרת שימוש ל-5 שעות) · התקנה, הזדהות, הרצה · `/clear`, `/compact`, `/usage` · **מצבי הרשאה** (default · acceptEdits · plan) · פקודות slash מובנות ומותאמות
2. **הנחיה** — `CLAUDE.md` כזיכרון הפרויקט · דוגמת Anthropic: אותה תמונה, שני פרומפטים, שני עולמות · מבנה פרומפט · תרגול חי ב-Console (נאיבי מול מובנה) · אותו קוד, שאלה רגילה מול שאלה מובנית · **מידע מול החלטה**
3. **Skills** — למה skill ולא פרומפט שחוזר על עצמו · אנטומיה של skill · **להתקין בעיניים פקוחות** (skill הוא prompt שמוזרק לסוכן שלכם) · הדגמות חיות: `code-review-skill`, skill של `shadcn/ui`, `audit-context-building` של Trail of Bits, ו-`cv-skill` שנכתב לקורס
4. **סיכום** — takeaways ומה במפגש הבא

### מפגש 02 — בנייה: מ-spec ועד deploy

בונים מוצר אמיתי (**FixSlot**) מאפס, ובדרך מחליטים למה כל דבר:

- **המוצר** — הבעיה, קהל היעד, שלושת הכובעים (PM · UX · Dev) · מרחב הבעיה מול מרחב הפתרון · המסלול מהבעיה ל-`CLAUDE.md` · `/superpowers: brainstorming` שלא נותן לסוכן לכתוב קוד עד שהבעיה ברורה · `/init` · מתי skill הוא כלי כבד מדי, ואיך משביתים אותו · מקרה אמיתי: **ה-skill שהריץ ransomware**
- **ארכיטקטורה** — vibe stack מול scale stack · **MCP · CLI · API** — שלוש דרכים לדבר עם כלים · למה Next.js, למה Vercel, למה Supabase — ומה עוד נשקל בכל אחת מהשכבות · מודל הנתונים · מתי לבחור אחרת
- **מודל וחשיבה** — איזה מודל למה · מצבי חשיבה (`think` → `ultrathink`) · Thinking מול Plan mode, ולמה זה לא אותו דבר
- **בנייה חיה** — ממאגר ריק ל-SaaS פרוס, כולל ה-debug loop
- **וגם** — מתי *לא* להשתמש ב-Claude Code

### מפגש 03 — עבודה בצוות

- **למה זה שונה** — מפתח אחד, שלושה PRs בבוקר, ושלוש בעיות תיאום שלא היו קודם
- **Git כתשתית** — שמונה פקודות ושישה מושגים · Git Flow · branch לכל יחידת עבודה · `git worktree` להרצת שני Claudes בלי שיתנגשו · מה Claude כותב במקומכם (commits, תיאורי PR, changelog) · Claude כמורה ל-git
- **PRs בעולם של AI** — לכתוב PR שעונה על *למה*, לא רק על *מה* · `/review`, `/security-review`, `/ultrareview` · מה לחפש בקוד שכתב AI (over-engineering, fake error handling, hidden assumptions)
- **טקסי צוות** — מה עובר ל-async ומה נשאר ב-Daily · שני אנשים על אותה בעיה
- **אוטומציה** — סוכן שרץ ב-CI על כל PR · מטריצת leverage מול risk · ארבע אוטומציות שמשתלמות מיידית, וארבעה קווים שלא חוצים
- **בונוסים** — Remotion, Remote Control, Cowork

### פרויקט גמר — צ׳אט מעל מסמכי החוג

עבודת צוות, 2–3 ימי עבודה, הגשה בריפו ציבורי.

בונים ממשק צ׳אט בעברית שעונה על שאלות סטודנטים מתוך שני מסמכים רשמיים של המכללה — השנתון של החוג ותקנון הלימודים. המערכת עונה **רק** ממה שכתוב, מציינת מקור לכל תשובה, ואומרת בפירוש ״לא מופיע במסמכים״ כשהתשובה לא שם.

הארכיטקטורה היא **agentic retrieval** ולא צנרת RAG קלאסית: במקום top-k קבוע בכל שאלה, נותנים ל-Claude ארבעה כלים מעל אינדקס מובנה (`list_sections`, `get_section`, `search` מעל SQLite FTS5, `get_course_table`) והוא מחליט מה לקרוא. ארבע דרישות חובה — ציטוט מקור, סירוב, prompt caching, ותקרת איטרציות — ועשר שאלות הערכה זהות לכל הצוותים.

הכול בתיקייה [`final-project/`](./final-project): [הבריף המלא](./final-project/README.md), [הדק](./final-project/final-project-deck-he.pptx), ושני ה-PDF-ים ב-[`pdfs/`](./final-project/pdfs).

### הדק המאוחד

[`Excellenteam Claude Code Deck/`](./Excellenteam%20Claude%20Code%20Deck) הוא כל הקורס ברצף אחד — 136 שקופיות, הגרסה שהועברה לתוכנית Excellenteam. הוא מכיל **שני חלקים שלא מופיעים בדקים של המפגשים הבודדים**:

* **Markdown Files & Memory** — למה הסוכן לא קרא את הריפו שלכם · ההבדל בין הקשר תמידי (`CLAUDE.md`) להקשר מוזמן (`spec.md`, `prd.md`, `plan.md`) · ארבע דרכים להכניס קובץ להקשר, ושתי התקלות שכולם נופלים בהן · איך הזיכרון האוטומטי עובד (דפוס `MEMORY.md` + topic files) · ומה הזיכרון הזה **לא** — לא למידה, לא אכיפה, לא נייד
* **Planning skills** — [BMAD](https://github.com/bmad-code-org/BMAD-METHOD): צוות אג׳ייל של סוכנים שהפלט שלו הוא קובצי סטורי, לא קוד · מה יש בתוך קובץ סטורי ולמה `Dev Notes` הוא הקסם · והשוואה עדינה מול `superpowers` — BMAD מניח שהסוכן צריך לזכור, superpowers מניח שזיכרון הוא זיהום

---

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

* [`installation-instructions/`](./installation-instructions) — הדק המלא: דרישות מערכת, התקנה לכל מערכת הפעלה, אפשרויות התחברות (מנוי מול API), ותקלות נפוצות
* [`install.md`](./install.md) — מדריך ההתקנה הקצר של הקורס
* [התיעוד הרשמי של Anthropic](https://code.claude.com/docs/en/setup) — מקור האמת, תמיד מעודכן

> שימו לב: Claude Code דורש מנוי Pro / Max / Team / Enterprise או חשבון Console. התוכנית החינמית של Claude.ai **לא** כוללת גישה.

---

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

הריפו מכיל [`CLAUDE.md`](./CLAUDE.md) — הסוכן קורא אותו בכל פתיחת סשן ויודע להסביר את החומר, לא רק לאתר קבצים.

## התכוננות למפגש 1 (מומלץ)

לפני שמגיעים לכיתה — יש בתיקיית [`bonus/`](./bonus) תוכן שהוא ההכנה הכי טובה למפגש הראשון. 30 דקות מקור ראשון על הנחיה (prompt engineering) ישירות ממהנדסי Applied AI ב-Anthropic, פלוס תרגיל קצר שמראה את ההבדל בפועל. פתחו לפני שמתחילים — זה חוסך שעות של ניסוי וטעייה.

---

## Repo layout

```
claude101/
├── README.md                        ← you are here
├── CLAUDE.md                        ← context for the Claude Code agent
├── install.md                       ← Claude Code setup guide
├── installation-instructions/       ← דק התקנה: Mac · Windows · Linux
│   ├── claude-code-install-he.pptx
│   └── build_deck.py                ← מייצר את הדק מחדש
├── pre-course task/                 ← משימת הכנה: עמוד GitHub אישי
│   ├── github-page-task-he.pptx
│   └── build_deck.py
├── session-01/                      ← יסודות, harness, הנחיה, Skills
│   ├── claude-code-deck1-he.pptx
│   ├── notes.md
│   └── *.png                        ← דוגמאות naive מול structured
├── session-02/                      ← בנייה — מ-spec ועד deploy
│   └── claude-code-deck2-he.pptx
├── session-03/                      ← עבודה בצוות
│   └── claude-code-deck3-team-he.pptx
├── final-project/                   ← פרויקט הגמר
│   ├── README.md                    ← הבריף המלא
│   ├── assignment-he.pdf            ← הבריף כ-PDF
│   ├── final-project-deck-he.pptx   ← הדק להצגה בכיתה
│   ├── pdfs/                        ← שני המסמכים שעליהם עונים
│   ├── build_deck.py                ← מייצר את הדק מחדש
│   └── build_pdf.py                 ← מייצר את ה-PDF מה-README
├── Excellenteam Claude Code Deck/   ← כל הקורס ברצף אחד (136 שקופיות)
│   └── exellenteam-claude-master.pptx
└── bonus/                           ← yes, there is bonus content
```

כל דק נוצר מסקריפט Python (`build_deck.py`) עם `python-pptx`. משנים את הסקריפט ומריצים `python3 build_deck.py` — הסקריפט הוא המקור, לא ה-pptx.

---

## Skills וכלים שנשתמש בהם

**Skills שמתקינים:**

| Skill | למה זה | איפה בקורס |
|---|---|---|
| [`code-review-skill`](https://github.com/awesome-skills/code-review-skill) | 9,500+ שורות הנחיות סקירה ל-11 שפות ופריימוורקים | מפגש 01 |
| [`ui-ux-pro-max`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | אינטליגנציית עיצוב — 67 סגנונות, 96 פאלטות, 13 stacks | מפגש 01 |
| [`shadcn/ui`](https://ui.shadcn.com) | `npx shadcn@latest skill add` — ידע מודע-לפרויקט על כל הרכיבים | מפגש 01 |
| [`audit-context-building`](https://github.com/trailofbits/skills) | Trail of Bits — בניית הקשר לביקורת אבטחה. אסור לו למצוא באגים, רק להבין את המערכת | מפגש 01 |
| [`cv-skill`](https://github.com/talgurevich/cv-skill) | בונה קורות חיים בעברית — skill שנכתב לקורס, כדוגמה למה שאפשר לבנות | מפגש 01 |
| [`superpowers`](https://github.com/obra/superpowers) | מתודולוגיית פיתוח שלמה: spec → plan → subagents → verify | מפגש 02 |
| [`BMAD`](https://github.com/bmad-code-org/BMAD-METHOD) | צוות אג׳ייל של סוכנים שמייצר קובצי סטורי | הדק המאוחד |

**פקודות slash מובנות:**

| פקודה | מה היא עושה |
|---|---|
| `/init` | סורקת את הריפו וכותבת `CLAUDE.md` ראשוני |
| `/code-review` | סקירת קוד על ה-diff הנוכחי (בדק של מפגש 03 מופיע בשמו הישן, `/review`) |
| `/security-review` | סקירת אבטחה |
| `/code-review ultra` | סקירה עמוקה מרובת-סוכנים בענן (בדק: `/ultrareview` — כיום alias מיושן) |
| `/clear` · `/compact` · `/usage` | ניהול הקשר ומעקב אחרי צריכה |
| `/skills` | הפעלה והשבתה של skills |
| `/memory` | הזיכרון של הסוכן — קבצי markdown שאפשר לקרוא, לערוך ולמחוק |

**מדריך Skills בעברית:** [agentskills.co.il](https://agentskills.co.il/he)

---

## Anthropic Console

נשתמש ב-[platform.claude.com](https://platform.claude.com) להשוואת מודלים ופרומפטים בזמן אמת מול הכיתה — דרך ה-**Workbench**. שווה להירשם מראש (חינמי). הכתובת הישנה `console.anthropic.com` עדיין עובדת ומפנה לשם.

---

## Contact

Tal Gurevich · tal.gurevich@gmail.com · [linkedin.com/in/talgurevich](https://linkedin.com/in/talgurevich)
