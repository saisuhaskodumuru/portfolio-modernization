"""Static checks for the Portfolio Modernization demo site.

Run: python3 -m unittest discover -s tests -v
Uses only the standard library; no browser needed.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
JS = (ROOT / "app.js").read_text(encoding="utf-8")


class TestContent(unittest.TestCase):
    def test_no_placeholder_links(self):
        self.assertNotIn('href="#"', HTML)
        self.assertNotIn("href='#'", HTML)
        self.assertNotIn('href="#"', JS)

    def test_six_projects_present(self):
        titles = [
            "AI-Powered Fraud Detection Dashboard",
            "Enterprise RAG AI Chatbot",
            "Ohio Job and Family Services: HCL Volt MX Iris to Angular Migration",
            "Verizon: Fraud Detection and LLM Customer Support Microservices",
            "Portfolio Modernization",
            "Java ML Inference Engine",
        ]
        for title in titles:
            self.assertIn(title, HTML, f"missing project: {title}")

    def test_live_github_links(self):
        self.assertIn(
            "https://github.com/saisuhaskodumuru/ai-fraud-detection-dashboard/blob/main/docs/CASE_STUDY.md",
            HTML,
        )
        self.assertIn(
            "https://github.com/saisuhaskodumuru/enterprise-rag-ai-chatbot/blob/main/docs/CASE_STUDY.md",
            HTML,
        )
        self.assertIn("https://github.com/saisuhaskodumuru/ai-fraud-detection-dashboard", HTML)
        self.assertIn("https://github.com/saisuhaskodumuru/enterprise-rag-ai-chatbot", HTML)

    def test_portfolio_projects_are_personal_not_work(self):
        # Correction (Nov 24, 2026): the 4 portfolio projects are personal
        # projects — no employer labels and no work dates on their cards.
        self.assertEqual(HTML.count("Personal project"), 4)
        articles = re.findall(r"<article.*?</article>", HTML, re.DOTALL)
        self.assertEqual(len(articles), 6)
        personal_titles = [
            "AI-Powered Fraud Detection Dashboard",
            "Enterprise RAG AI Chatbot",
            "Portfolio Modernization",
            "Java ML Inference Engine",
        ]
        for article in articles:
            for title in personal_titles:
                if title in article:
                    self.assertIn("Personal project", article, f"{title} is not labelled personal")
                    self.assertNotIn("Verizon", article, f"{title} is still linked to Verizon")
                    self.assertNotIn("Feb 2024", article, f"{title} still carries work dates")

    def test_work_projects_keep_employer_labels(self):
        # The two work projects are separate from the portfolio projects
        # and keep their employer and dates.
        self.assertIn("Ohio Department of Job and Family Services &bull; Jun 2026 – Present", HTML)
        self.assertIn("Verizon &bull; Feb 2024 – May 2026", HTML)

    def test_skills_explorer_does_not_tie_portfolio_projects_to_verizon(self):
        for project in ["Enterprise RAG AI Chatbot", "AI-Powered Fraud Detection Dashboard",
                        "Java ML Inference Engine"]:
            for m in re.finditer(re.escape(project) + r'[^"]*"', JS):
                self.assertNotIn("Verizon", m.group(0), f"{project} tied to Verizon in app.js")

    def test_projects_without_repos_link_linkedin(self):
        # The four projects without a published repo link to LinkedIn.
        self.assertGreaterEqual(HTML.count("https://www.linkedin.com/in/suhaskodumuru/"), 5)

    def test_experience_facts(self):
        for fact in [
            "Ohio Department of Job and Family Services",
            "Jun 2026 – Present",
            "Verizon",
            "Feb 2024 – May 2026",
            "Truist",
            "Feb 2023 – Feb 2024",
            "Northern Trust",
            "Mar 2022 – Feb 2023",
            "SS&amp;C Health",
            "May 2018 – Dec 2021",
            "University of Cincinnati",
            "4.0/4.0",
            "3.7/4.0",
            "Azure AI Engineer Associate (AI-102)",
        ]:
            self.assertIn(fact, HTML, f"missing fact: {fact}")

    def test_contact(self):
        self.assertIn("mailto:k.suhas1729@outlook.com", HTML)
        self.assertIn("https://saisuhaskodumuru.github.io", HTML)
        self.assertIn("https://github.com/saisuhaskodumuru", HTML)

    def test_all_external_links_https_or_mailto(self):
        hrefs = re.findall(r'href="([^"]+)"', HTML)
        for href in hrefs:
            self.assertTrue(
                href.startswith("https://") or href.startswith("mailto:")
                or href.startswith("#") or href.endswith(".css"),
                f"unexpected href: {href}",
            )


class TestSkillsExplorer(unittest.TestCase):
    def test_skill_count_and_categories(self):
        names = re.findall(r'\{ name: "([^"]+)", category: "([^"]+)"', JS)
        self.assertEqual(len(names), 24, f"expected 24 skills, found {len(names)}")
        categories = {c for _, c in names}
        self.assertEqual(categories, {"Languages", "Frameworks", "Cloud/AI", "Tools"})

    def test_every_skill_has_usage(self):
        entries = re.findall(r'usedIn: "([^"]+)"', JS)
        self.assertEqual(len(entries), 24)
        for entry in entries:
            self.assertTrue(entry.strip(), "empty usedIn")

    def test_no_invented_testimonials(self):
        self.assertNotIn("testimonial", HTML.lower())
        self.assertNotIn("what clients say", HTML.lower())


class TestStyleAndAccessibility(unittest.TestCase):
    def test_glassmorphism_present(self):
        self.assertIn("backdrop-filter: blur(16px)", CSS)
        self.assertIn("rgba(255, 255, 255, 0.78)", CSS)

    def test_responsive_breakpoints(self):
        self.assertIn("@media (max-width: 767.98px)", CSS)
        self.assertIn("@media (min-width: 768px) and (max-width: 991.98px)", CSS)

    def test_accessibility_basics(self):
        self.assertIn('<html lang="en">', HTML)
        self.assertIn("Skip to main content", HTML)
        self.assertIn('aria-label="Main navigation"', HTML)
        self.assertIn('aria-pressed="true"', HTML)
        self.assertIn('aria-live="polite"', HTML)
        self.assertIn('role="group"', HTML)
        self.assertIn('aria-labelledby="skills-heading"', HTML)

    def test_bootstrap_5_cdn(self):
        self.assertIn("bootstrap@5.3.3", HTML)
        self.assertIn("bootstrap.bundle.min.js", HTML)


if __name__ == "__main__":
    unittest.main()
