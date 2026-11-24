# Portfolio Modernization

A standalone modernized rebuild of Sai Suhas Kodumuru's personal
portfolio — glassmorphism UI, an interactive skills explorer, and a
responsive layout. It is a demo of the portfolio itself, built as
Project 3 of the portfolio. It is not the live portfolio: the live
site is https://saisuhaskodumuru.github.io and this demo does not
touch it.

## What it does

- Presents Sai's real profile: Senior Java Full Stack Developer,
  open to remote Senior Java Full Stack roles from Cincinnati, OH.
- Hero, About, an Experience timeline (Ohio Department of Job and
  Family Services, Verizon, Truist, Northern Trust, SS&C Health),
  six Projects, an interactive Skills Explorer, Certifications, and
  Contact.
- Skills explorer: filter 24 skills by category (Languages,
  Frameworks, Cloud/AI, Tools), search by name, and click a skill to
  see where it was used.
- Glassmorphism UI: frosted-glass cards over a deep gradient, with
  dark text on light glass for contrast.
- Responsive layout: full layout on desktop, stacked cards and
  full-width buttons below 768px, navbar collapse below 992px.
- Accessibility: skip link, semantic HTML, keyboard-focusable
  filters with `aria-pressed`, live regions for the skills count
  and detail panel, visible focus outlines.

## Projects on the page — personal vs work

The four portfolio projects are **personal projects**, with no
employer labels and no work dates:

- AI-Powered Fraud Detection Dashboard — personal project, code and
  case study on GitHub
- Enterprise RAG AI Chatbot — personal project, code and case study
  on GitHub
- Portfolio Modernization — personal project (this demo)
- Java ML Inference Engine — personal project

The other two projects are work projects and keep their employer
and dates:

- Ohio Job and Family Services: HCL Volt MX Iris to Angular
  Migration — Ohio Department of Job and Family Services,
  Jun 2026 – Present
- Verizon: Fraud Detection and LLM Customer Support Microservices —
  Verizon, Feb 2024 – May 2026

The two GitHub repos are personal projects too. Their links:

- https://github.com/saisuhaskodumuru/ai-fraud-detection-dashboard
  (case study at
  /blob/main/docs/CASE_STUDY.md)
- https://github.com/saisuhaskodumuru/enterprise-rag-ai-chatbot
  (case study at
  /blob/main/docs/CASE_STUDY.md)

The Portfolio Modernization and Java ML Inference Engine projects
have no repository yet, so they link to the LinkedIn profile
(https://www.linkedin.com/in/suhaskodumuru/) instead.

## Architecture

```
Browser
    |
    v
Static site — no build step, no backend, no database
  index.html   (content: hero, about, experience, projects,
                skills explorer shell, certifications, contact)
  styles.css   (Bootstrap 5.3 via CDN + glassmorphism theme,
                responsive breakpoints at 768px and 992px)
  app.js       (skills data + filter / search / select logic)
```

Bootstrap 5.3 is loaded from the jsDelivr CDN. Everything else is
local. There is no JavaScript framework and no server-side code.

## How to run

Requirements: Python 3 (only to serve the files) or any static
file server. No build step.

```bash
python3 -m http.server 8137
```

Then open http://localhost:8137 in a browser. Or open
`index.html` directly — everything works from `file://` except
nothing needs a server at all.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

14 tests in `tests/test_site.py` (standard library only) plus 3
correction tests, 17 total. They check: no placeholder `#` links;
all six projects present; the GitHub repo and case-study links for
the two published projects; the four portfolio projects are
labelled "Personal project" with no employer or work dates, while
the two work projects keep theirs; the skills explorer data has 24
skills in 4 categories, each with a usage note, and does not tie
any portfolio project to Verizon; experience facts (employers,
dates, degrees, AI-102); contact details; all external links are
HTTPS or `mailto:`; glassmorphism styles and responsive breakpoints
are present; accessibility basics (skip link, `aria-pressed`,
live regions, Bootstrap 5 CDN).

The skills explorer logic was also exercised in Node with a small
DOM stub (`/tmp/dom-test.js`, not part of the deliverable): initial
render 24 chips; Languages filter 6 chips; Languages + search
"java" 2 chips; selecting Java shows its category and where it was
used; a search with no match shows 0 chips and "No skills match
that search."

## Data

All profile facts come from Sai's LinkedIn profile and resume
work: employers and dates, degrees and GPAs, the AI-102
certification, and the six LinkedIn projects. No employers, dates,
metrics, or testimonials were invented. The Experience section is
the work history; the Projects section keeps the four portfolio
projects separate from it, as personal projects.
