# Case Study: Portfolio Modernization

## What this is

A standalone modernized rebuild of Sai Suhas Kodumuru's personal
portfolio, built as Project 3 of the portfolio. It is a static
site — HTML, CSS, and JavaScript with Bootstrap 5 — with a
glassmorphism UI, an interactive skills explorer, and a responsive
layout. It presents the same profile that is on the live portfolio
at https://saisuhaskodumuru.github.io, but it is a separate demo:
it does not touch the live portfolio repository or the live site.

## Problem

The live portfolio was a single static page whose project cards
linked to case studies that did not exist — every "View Case Study"
link was a `#` placeholder — and whose skills were a flat list with
no way to explore what a skill was used for. A recruiter landing
on it could not tell which projects were real and runnable, which
skills were used where, or whether the page worked on a phone. The
goal of this rebuild was a portfolio that is honest about what is
real (two projects now have public code and case studies on GitHub),
lets a visitor explore skills by category and usage, and works at
desktop and mobile widths.

## My role

I rebuilt the portfolio end to end as a personal project: the
information architecture (hero, About, Experience timeline,
Projects, Skills Explorer, Certifications, Contact), the
glassmorphism theme and responsive CSS, the skills explorer data
and JavaScript, the accessibility work, the tests, and this case
study. The profile facts are Sai's LinkedIn and resume facts; the
Experience section is his work history and the Projects section
keeps the portfolio projects separate from it.

## A correction that shaped the build

Halfway through the build, Sai corrected a framing error: all four
portfolio projects are **personal projects**, not work projects.
They must not be associated with Verizon or any other employer, and
must not carry work-experience dates. The first version of this
demo had labelled the Fraud Detection Dashboard, the RAG Chatbot,
and the Java ML Inference Engine with "Verizon, Feb 2024 – May
2026", and had framed the skills explorer as if those projects
were Verizon work. That was wrong, and it was fixed before the
demo was finished:

- The four portfolio project cards now say "Personal project" with
  no employer and no dates.
- The skills explorer's usage notes point at the personal projects
  by name instead of at Verizon.
- The two work projects on the page — the Ohio Volt MX to Angular
  migration and the Verizon fraud detection and LLM microservices —
  are separate cards that keep their employer and dates.
- Three automated tests now enforce this: the four personal cards
  must say "Personal project" and contain no employer or dates,
  the two work cards must keep theirs, and no portfolio project
  may be tied to Verizon in the skills data.

The same correction applies to the LinkedIn associations and to
the wording of the Project 1 and 2 repositories, which is being
handled separately; this demo is already correct.

## Architecture

```
Browser
    |
    v
index.html  — content and structure (no JavaScript-generated
              content: every section is real HTML, so the page
              is readable with JavaScript disabled except for
              the skills explorer)
styles.css  — Bootstrap 5.3 (CDN) + glassmorphism theme:
              frosted cards (backdrop-filter blur, translucent
              white, soft shadow) over a fixed deep gradient;
              dark text on light glass for contrast
app.js      — 24 skills in 4 categories with a "where it was
              used" note each; filter by category, search by
              name, click to see usage
```

No build step, no backend, no database, no JavaScript framework.
Bootstrap 5.3 comes from the jsDelivr CDN; everything else is
local files.

## What was built

- A hero with name, headline, a one-paragraph summary, and links
  to Projects, LinkedIn, and GitHub, plus an Open to Work note
  (remote from Cincinnati, OH).
- An About section with the summary, the current Ohio role, the
  Verizon role, the target roles, and a facts list (location,
  8.5 years, MS IT 4.0/4.0, BTech 3.7/4.0, AI-102).
- An Experience timeline with all five roles and their real
  employers, dates, locations, and work modes.
- A Projects grid with all six LinkedIn projects. The two with
  published repositories link to the repo and the case study on
  GitHub; the other four link to the LinkedIn profile, and the
  README says why.
- A Skills Explorer with 24 skills in four categories — Languages
  (6), Frameworks (6), Cloud/AI (6), Tools (6) — a search box,
  category filter buttons with `aria-pressed`, a live result
  count, and a detail panel that shows a selected skill's
  category and where it was used.
- A Certifications section with the Azure AI Engineer Associate
  (AI-102), and a Contact section (email, LinkedIn, GitHub,
  portfolio).
- Accessibility: skip link, semantic landmarks, keyboard-focusable
  filters, `aria-live` regions for the count and detail panel,
  visible focus outlines, and dark text on light glass so the
  frosted cards stay readable.

## Results, measured on this demo

These numbers were measured locally on 2026-11-24 by serving the
finished site with `python3 -m http.server` and curling the real
files. They describe the demo only.

- Tests: 17 run, 0 failures, in 0.003 s (`python3 -m unittest
  discover -s tests -v`).
- `GET /`: HTTP 200 in 0.0079 s, 15,013 bytes.
- `GET /styles.css`: HTTP 200 in 0.0038 s, 5,010 bytes.
- `GET /app.js`: HTTP 200 in 0.0009 s, 5,443 bytes.
- Served page: 16 glass-card elements, 8 unique external HTTPS
  links, 4 "Personal project" labels, 0 placeholder `#` links
  (verified by the tests, which fail on any `href="#"`).
- Skills explorer, exercised in Node with a DOM stub: initial
  render 24 chips ("Showing 24 of 24 skills"); Languages filter
  6 chips; Languages + search "java" 2 chips (Java, JavaScript);
  selecting Java shows "Category: Languages" and "Where it was
  used: Ohio Department of Job and Family Services; Verizon;
  Truist; Northern Trust; SS&C Health"; a search with no match
  shows 0 chips and "No skills match that search."
- Responsive: verified by the CSS breakpoints in the stylesheet
  (`max-width: 767.98px` for stacked cards and full-width hero
  buttons, `768px–991.98px` for the mid-size hero, Bootstrap's
  navbar collapse below 992px). No headless browser was available
  in this environment, so the layout was not screenshot-tested at
  mobile and desktop widths — the breakpoints and the Bootstrap
  grid are the check that exists, and a screenshot check is the
  known gap.

No production metrics are claimed here. There is no production
system behind this demo; it is a static site.

## Challenges

- The correction above: the first build tied three personal
  projects to Verizon with work dates, because the LinkedIn
  projects had been added that way. Fixing it meant changing the
  project cards, the skills data, and adding tests that pin the
  distinction, so the error cannot come back silently.
- The skills explorer's "where it was used" notes had to stay
  honest: a skill used across many roles says "Across full-stack
  roles" instead of inventing a specific employer for it, and
  portfolio-project usage is labelled "(personal project)" so a
  reader can tell it apart from job usage.
- A live-server check briefly left the demo server running: the
  first stop command killed the shell running the check instead
  of the server, because the kill pattern matched its own command
  line. The server was stopped afterwards by PID and the stop was
  verified with a curl that failed to connect.
- No headless browser was available for screenshot checks of the
  responsive layout, so that verification is limited to the CSS
  breakpoints and the Bootstrap grid, as noted above.

## Tech stack

HTML5, CSS3 (custom glassmorphism theme), Bootstrap 5.3 (CDN),
vanilla JavaScript, Python 3 `http.server` for local serving,
Python `unittest` (standard library) for tests, Node for the
skills-explorer DOM-stub check. No build step, no backend, no
database.
