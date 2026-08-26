# LinkedIn post — course completion

**Language:** English · **Angle:** what the students built · **Draft v1**

---

My students just shipped a Hebrew chat system that answers questions about our
college's academic regulations — and says "that isn't in the documents" when the
answer isn't there.

That last part is the whole assignment.

We wrapped the Claude Code course at Tel-Hai Academic College (CS department,
Excellenteam program). The final project: teams of 2–3, three days, two real PDFs
— the CS department yearbook and the undergraduate regulations. ~58 pages,
~233,000 characters of Hebrew.

A few things made it harder than it sounds:

**Naive PDF extraction breaks on Hebrew.** Everyone builds a beautiful retrieval
layer on top of text they never actually opened and read. Discovering that in
hour two, not day three, is a real engineering lesson.

**It's agentic retrieval, not a RAG pipeline.** Instead of pulling a fixed top-k
per question and hoping, we gave Claude four tools over a structured index —
`list_sections`, `get_section`, `search` (SQLite FTS5, BM25), and
`get_course_table` — and let the model decide what to read. Four hard
requirements: cite the source, refuse when the answer isn't there, use prompt
caching, cap the iterations.

**No vector database. On purpose.** At this corpus size, embeddings are
infrastructure you don't need — and semantic retrieval in Hebrew will eat a full
day out of three. The finished index is one SQLite file, a few hundred KB.
Knowing when infrastructure is the wrong answer is a skill.

The course got there in three sessions: foundations (harness, tokens, prompting,
Skills), building a real product from spec to deploy, and working as a team —
git, PRs, and CI automation in a world where one developer opens three pull
requests before lunch.

Everything is public — decks, briefs, and the CLAUDE.md that lets the repo
explain itself:
https://github.com/talgurevich/claude101

Proud of this group. They stopped asking "can it write the code" and started
asking "should it, and how would I know if it's wrong."

#ClaudeCode #AI #SoftwareEngineering #CSEducation #TelHai
