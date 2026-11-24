// Skills explorer data. "usedIn" lists only roles / projects documented
// in Sai's LinkedIn profile and resume work; generic skills that span
// many roles say "Across full-stack roles" rather than inventing a
// specific employer for them.
const SKILLS = [
  { name: "Java", category: "Languages", usedIn: "Ohio Department of Job and Family Services; Verizon; Truist; Northern Trust; SS&C Health" },
  { name: "Python", category: "Languages", usedIn: "Enterprise RAG AI Chatbot (personal project); AI-Powered Fraud Detection Dashboard (personal project)" },
  { name: "JavaScript", category: "Languages", usedIn: "Ohio Department of Job and Family Services — Angular migration; Portfolio Modernization" },
  { name: "TypeScript", category: "Languages", usedIn: "Ohio Department of Job and Family Services — Angular migration" },
  { name: "SQL", category: "Languages", usedIn: "Across full-stack roles" },
  { name: "HTML/CSS", category: "Languages", usedIn: "Portfolio Modernization; across full-stack roles" },
  { name: "Spring Boot", category: "Frameworks", usedIn: "Ohio Department of Job and Family Services; AI-Powered Fraud Detection Dashboard (personal project)" },
  { name: "Angular", category: "Frameworks", usedIn: "Ohio Department of Job and Family Services — HCL Volt MX Iris to Angular migration" },
  { name: "React", category: "Frameworks", usedIn: "Across full-stack roles" },
  { name: "LangChain", category: "Frameworks", usedIn: "Enterprise RAG AI Chatbot (personal project)" },
  { name: "Bootstrap 5", category: "Frameworks", usedIn: "Portfolio Modernization" },
  { name: "FastAPI", category: "Frameworks", usedIn: "Enterprise RAG AI Chatbot (personal project)" },
  { name: "Azure OpenAI", category: "Cloud/AI", usedIn: "Enterprise RAG AI Chatbot (personal project)" },
  { name: "Azure ML", category: "Cloud/AI", usedIn: "AI-Powered Fraud Detection Dashboard (personal project)" },
  { name: "GPT-4", category: "Cloud/AI", usedIn: "Enterprise RAG AI Chatbot (personal project)" },
  { name: "Retrieval-Augmented Generation (RAG)", category: "Cloud/AI", usedIn: "Enterprise RAG AI Chatbot (personal project)" },
  { name: "FAISS", category: "Cloud/AI", usedIn: "Enterprise RAG AI Chatbot (personal project)" },
  { name: "Microsoft Azure", category: "Cloud/AI", usedIn: "Ohio Department of Job and Family Services — AKS and Azure DevOps; personal AI projects (Azure ML, Azure OpenAI)" },
  { name: "Kafka", category: "Tools", usedIn: "Verizon — Fraud Detection and LLM Customer Support Microservices (work project)" },
  { name: "Docker", category: "Tools", usedIn: "Across full-stack roles" },
  { name: "Kubernetes (AKS)", category: "Tools", usedIn: "Ohio Department of Job and Family Services — Azure Kubernetes Service" },
  { name: "Azure DevOps", category: "Tools", usedIn: "Ohio Department of Job and Family Services" },
  { name: "Git", category: "Tools", usedIn: "Across full-stack roles" },
  { name: "REST APIs", category: "Tools", usedIn: "Ohio Department of Job and Family Services; Java ML Inference Engine (personal project)" },
];

let activeCategory = "All";
let searchText = "";
let selectedSkill = null;

const listEl = document.getElementById("skills-list");
const countEl = document.getElementById("skills-count");
const detailEl = document.getElementById("skill-detail");
const searchEl = document.getElementById("skill-search");

function filteredSkills() {
  return SKILLS.filter((s) => {
    const inCategory = activeCategory === "All" || s.category === activeCategory;
    const inSearch = s.name.toLowerCase().includes(searchText.toLowerCase());
    return inCategory && inSearch;
  });
}

function renderSkills() {
  const skills = filteredSkills();
  listEl.innerHTML = "";
  skills.forEach((skill) => {
    const li = document.createElement("li");
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "skill-chip";
    btn.textContent = skill.name;
    btn.setAttribute("aria-pressed", selectedSkill === skill.name ? "true" : "false");
    btn.addEventListener("click", () => selectSkill(skill));
    li.appendChild(btn);
    listEl.appendChild(li);
  });
  countEl.textContent = skills.length === 0
    ? "No skills match that search."
    : `Showing ${skills.length} of ${SKILLS.length} skills.`;
  if (skills.length === 0) {
    detailEl.innerHTML = "<p>No skills match that search. Try a different term or category.</p>";
  }
}

function selectSkill(skill) {
  selectedSkill = skill.name;
  detailEl.innerHTML = "";
  const heading = document.createElement("h3");
  heading.textContent = skill.name;
  const category = document.createElement("p");
  category.innerHTML = `<strong>Category:</strong> ${skill.category}`;
  const used = document.createElement("p");
  used.innerHTML = `<strong>Where it was used:</strong> ${skill.usedIn}`;
  detailEl.append(heading, category, used);
  renderSkills();
}

document.querySelectorAll("#category-filters button").forEach((btn) => {
  btn.addEventListener("click", () => {
    activeCategory = btn.dataset.category;
    document.querySelectorAll("#category-filters button").forEach((b) => {
      const active = b === btn;
      b.classList.toggle("active", active);
      b.setAttribute("aria-pressed", active ? "true" : "false");
    });
    renderSkills();
  });
});

searchEl.addEventListener("input", () => {
  searchText = searchEl.value;
  renderSkills();
});

renderSkills();
