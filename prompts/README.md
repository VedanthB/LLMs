# Prompt Library

A curated collection of 27 specialized AI prompts for building products, planning projects, and accelerating workflows. These prompts are designed to help you think better, ideate faster, and execute more efficiently.

## 📚 Table of Contents

- [Overview](#overview)
- [How to Use](#how-to-use)
- [Prompt Categories](#prompt-categories)
  - [Critical - Planning & Building](#critical---planning--building)
  - [Business - Marketing & Growth](#business---marketing--growth)
  - [Ideation - Ideas & Strategy](#ideation---ideas--strategy)
  - [Automation - Workflows & AI](#automation---workflows--ai)
  - [Personal - Self Discovery](#personal---self-discovery)
  - [Utility - General Tools](#utility---general-tools)
- [Quick Start Guide](#quick-start-guide)
- [Best Practices](#best-practices)

---

## Overview

This prompt library contains 27 specialized prompts organized into 6 categories. Each prompt is designed to guide you through a specific process - from planning a technical architecture to growing your LinkedIn presence to discovering your personal goals.

**Key Features:**
- Structured conversation flows that ask the right questions
- Domain-specific expertise in each prompt
- Output formats designed for action (PRDs, masterplans, roadmaps)
- Personalized for AI Engineering and product building

---

## How to Use

### Basic Usage

1. **Copy the entire prompt** from the .md file
2. **Paste it into your AI assistant** (Claude, ChatGPT, etc.)
3. **Start the conversation** - the prompt will guide you through questions
4. **Get your output** - PRD, masterplan, strategy doc, etc.

### Advanced Usage

- **Customize prompts**: Add your specific context, tech stack preferences, or constraints
- **Chain prompts**: Use output from one prompt as input to another (e.g., IDEA_ANALYSIS → PRD → HLD)
- **Iterate**: Run the same prompt multiple times as your project evolves
- **Combine**: Mix and match sections from different prompts for custom workflows

### When to Use Each Prompt

See the detailed descriptions below for guidance on when each prompt is most valuable.

---

## Prompt Categories

### Critical - Planning & Building

**Location:** `prompts/critical/`

These are your core product development prompts. Use these when planning, designing, and building AI products or features.

#### AI_CTO.md
**Use When:** You have an app/product idea and need a technical blueprint
**Output:** `masterplan.md` - High-level technical architecture and implementation roadmap
**Key Questions:**
- What are you building and why?
- Who are the users?
- What's the core functionality?
- Technical stack recommendations
- Development phases

**Best For:**
- New product ideas
- Technical validation of concepts
- Getting architectural guidance
- Planning development phases

---

#### PRODUCT_MANAGER.md
**Use When:** You need a Product Requirements Document for an AI feature/product
**Output:** `prd.md` - Product specification document
**Key Questions:**
- What problem are you solving?
- Who is the user?
- What does success look like?
- Core features for v1
- Constraints and risks

**Best For:**
- Defining product scope
- Aligning team on requirements
- Before starting development
- Planning AI integrations

---

#### PRD.md (Enhanced)
**Use When:** You need a comprehensive PRD with AI-specific sections
**Output:** `prd.md` - Detailed product requirements with KPIs, model requirements, data needs
**Includes:**
- Business objectives & KPIs
- User journeys & scenarios
- Functional requirements
- Model requirements (LLM selection, latency, context window)
- Data requirements
- Prompt requirements
- Testing & measurement
- Risks & mitigations
- GTM/Rollout plan

**Best For:**
- LLM-powered products
- RAG systems
- AI agents
- Complex AI integrations
- Communicating with stakeholders

---

#### ARD.md (Agent Requirements Document)
**Use When:** Planning an AI agent (ReAct, Reflection, Research patterns, etc.)
**Output:** `ard.md` - Agent specification document
**Key Questions:**
- What LLM will you use?
- What tools does the agent need?
- What instructions/behavior?
- What should it remember (memory)?
- Success & termination conditions
- Evaluation metrics

**Best For:**
- Building autonomous agents
- Learning agentic patterns
- Planning tool-calling workflows
- Agent evaluation strategies

---

#### HLD.md (High-Level Design)
**Use When:** You have a PRD and need system architecture
**Output:** High-level technical design document
**Includes:**
- System overview & components
- Logical architecture diagram
- Data model (Supabase/Postgres schemas)
- Pipeline flow
- Integration details
- Prompt design examples
- API endpoints
- Deployment & scaling
- Monitoring & security
- Engineering deliverables

**Best For:**
- After completing PRD
- Before implementation starts
- Technical team alignment
- AI system architecture

---

#### MVP.md
**Use When:** Building an LLM-based RAG app (example included)
**Output:** MVP implementation plan
**Includes:**
- MVP scope definition
- Technical stack (Streamlit, FastAPI, LM Studio)
- Core features
- Data structure
- API endpoints
- Implementation steps

**Best For:**
- Quick RAG prototypes
- "Second brain" applications
- Learning RAG architecture
- FastAPI + Streamlit projects

---

### Business - Marketing & Growth

**Location:** `prompts/business/`

Use these for marketing, growth, content creation, and business strategy.

#### AI_CMO.md
**Use When:** Starting or growing social media presence organically
**Output:** `growthplan.md` - Social media growth strategy
**Key Questions:**
- Brand identity and voice
- Target audience and pain points
- Content pillars
- Platform strategy (X, LinkedIn, Instagram, YouTube)
- Posting cadence and engagement
- Success metrics

**Best For:**
- Building personal brand
- Product launch marketing
- Content strategy planning
- Organic growth tactics

---

#### LINKEDIN_CREATOR.md
**Use When:** Building LinkedIn presence (personal brand + company content)
**Output:** 30-day content masterplan + automation workflows
**Includes:**
- Personal brand positioning
- Company brand engine
- Content calendar (30 days)
- Example post drafts in your tone
- CTAs and lead flow
- Optional: n8n automation workflows

**Best For:**
- LinkedIn content strategy
- Founder/executive visibility
- Company page growth
- Lead generation
- Content automation

---

#### LANDINGPAGE_GENERATOR.md
**Use When:** Planning a landing page or portfolio
**Output:** `masterplan.md` - Landing page blueprint
**Key Questions:**
- Site purpose & core message
- Target audience
- Required sections
- Visual style (colors, typography)
- Platform preference
- Content needs

**Best For:**
- AI product landing pages
- Personal portfolio planning
- Quick website design
- Conceptual planning (no code)

---

#### BUSINESS_COACH.md
**Use When:** Auditing a business idea or current business for growth
**Output:** Ruthless business audit with growth plan
**Includes:**
- Current state snapshot
- Competitive benchmarking
- Bottleneck analysis
- Quick wins (≤90 days)
- Strategic initiatives (≥90 days)
- 90-day roadmap
- Expected revenue impact

**Best For:**
- Business idea validation
- Growth strategy
- AI product business models
- Identifying bottlenecks
- Revenue acceleration

---

#### OGILVY_COPY_REVIEWER.md
**Use When:** Reviewing marketing copy against Ogilvy principles
**Output:** Copy critique and improvements

**Best For:**
- Landing page copy
- Ad copy review
- Marketing material
- Conversion optimization

---

### Ideation - Ideas & Strategy

**Location:** `prompts/ideation/`

Use these for brainstorming, analyzing ideas, and strategic thinking.

#### IDEA_ANALYSIS.md
**Use When:** You have multiple ideas and need to evaluate/rank them
**Output:** Structured analysis with rankings and recommendations
**Framework:**
- Market potential (1-10)
- Execution complexity (1-10)
- Resource requirements
- Time to market
- Revenue streams
- Competitive advantage
- Pattern recognition across ideas
- Synergy mapping
- Execution roadmap for top 3

**Best For:**
- Choosing between multiple ideas
- Side project prioritization
- Finding non-obvious connections
- Optimization opportunities
- Business idea validation

---

#### IDEATION_AGENT.md
**Use When:** Deep exploration of a single idea through 25+ iterations
**Output:** Comprehensive ideation journey with evolved concept
**Process:**
- Autonomous recursive ideation
- Critical analysis after each iteration
- Feasibility evaluation
- 25+ iterations automatically
- Summary of evolution

**Best For:**
- Deep thinking on one idea
- Uncovering hidden aspects
- Thorough concept exploration
- Creative problem solving

---

#### STRATEGIC_ADVISOR.md
**Use When:** Need strategic guidance on business decisions
**Output:** Strategic recommendations

**Best For:**
- High-level strategy
- Business direction
- Strategic partnerships
- Market positioning

---

### Automation - Workflows & AI

**Location:** `prompts/automation/`

Use these for identifying automation opportunities and building AI workflows.

#### OPT_COACH.md ⭐ (Customized)
**Use When:** Finding AI automation opportunities in your work
**Output:** `masterplan` for task automation
**Framework:** OPT (Operating model, Process, Task)
- Operating model: Your role and success metrics
- Process: Repeating workflows
- Task: Discrete actions to automate

**Process:**
- Understand your operating model
- Map core processes
- Identify 3 automation candidates
- Select one and get detailed masterplan

**Best For:**
- AI Engineers looking for automation wins
- Workflow optimization
- AI product automation
- Process improvement

---

#### OPT.md ⭐ (Customized)
**Use When:** Building a chatbot to automate a workflow
**Output:** Chatbot masterplan (Python + Gradio)
**Similar to OPT_COACH but focused on:**
- Chatbot-specific implementation
- Gradio UI design
- API design
- Integration planning

**Best For:**
- Building internal tools
- Workflow chatbots
- Gradio applications
- AI automation projects

---

#### N8N_COACH.md
**Use When:** Building automation workflows with n8n
**Output:** n8n workflow guidance

**Best For:**
- No-code automation
- Workflow automation
- API integrations
- Data pipelines

---

#### n8n_CONSULTANT.md
**Use When:** Advanced n8n consulting and complex workflows
**Output:** n8n implementation strategy

**Best For:**
- Complex n8n workflows
- Enterprise automation
- Multi-step integrations
- Advanced n8n patterns

---

### Personal - Self Discovery

**Location:** `prompts/personal/`

#### SELF_DISCOVERY.md
**Use When:** Understanding your current development and growth areas
**Output:** Development assessment & transformation strategies
**Framework:** HUMAN 3.0 Model (4 quadrants)
- Mind: Mental world, beliefs, worldview
- Body: Physical presence, health, energy
- Spirit: Relationships, meaning, purpose
- Vocation: Career, value creation, impact

**Includes:**
- Adaptive interview process
- Metatype identification
- Lifestyle archetype
- Problem-solving lens
- Actionable transformation strategies
- Integration of all quadrants

**Best For:**
- Personal development planning
- Understanding strengths/weaknesses
- Goal setting (pairs well with business goals)
- Identifying growth opportunities
- Before running this prompt library (shapes context)

---

### Utility - General Tools

**Location:** `prompts/utility/`

General-purpose prompts for various tasks.

#### ASK_ME.md
Simple Q&A prompt structure.

#### BROWSER_USE.md
Browser automation and web interaction guidance.

#### CLAUDE_INSTRUCTION.md
Claude-specific instructions and optimization.

#### DEEPSEEK.md
DeepSeek model-specific guidance.

#### TEMPLATE_PROMPT.md
Template for creating new prompts.

#### RESOURCES.md
Curated resources and references.

#### AI_CONSULTANT.xml
General AI consulting prompt (XML format).

#### VIBE_PPT.md ⭐ (Customized)
**Use When:** Converting content to reveal.js slide deck
**Output:** Web-based presentation
**Includes:**
- Brand customization
- Vibe coding workflow example
- Gemini Canvas tutorial

**Best For:**
- Presentation creation
- Technical talks
- Product demos
- Portfolio presentations

---

## Quick Start Guide

### For New AI Products

```
1. SELF_DISCOVERY.md → Understand your goals and strengths
2. IDEA_ANALYSIS.md → Evaluate your product ideas
3. PRODUCT_MANAGER.md or PRD.md → Define requirements
4. AI_CTO.md or HLD.md → Design architecture
5. MVP.md or ARD.md → Plan implementation
```

### For Marketing & Growth

```
1. BUSINESS_COACH.md → Audit current state
2. AI_CMO.md → Plan content strategy
3. LINKEDIN_CREATOR.md → Build LinkedIn presence
4. LANDINGPAGE_GENERATOR.md → Design landing page
5. OGILVY_COPY_REVIEWER.md → Refine copy
```

### For Automation Projects

```
1. OPT_COACH.md → Identify automation opportunities
2. OPT.md → Plan chatbot implementation
3. N8N_COACH.md → Build no-code workflows
```

### For Learning AI Patterns

```
1. ARD.md → Design an AI agent
2. MVP.md → Build RAG system
3. PRD.md → Plan LLM integration
4. HLD.md → Architect AI system
```

---

## Best Practices

### 1. Start with Self-Discovery
Run `SELF_DISCOVERY.md` first to shape your goals and context. This will help you personalize other prompts.

### 2. Chain Prompts Together
Use outputs as inputs:
- `IDEA_ANALYSIS → PRD → HLD → Implementation`
- `BUSINESS_COACH → AI_CMO → LINKEDIN_CREATOR`

### 3. Iterate and Evolve
- Re-run prompts as your project evolves
- Update outputs regularly
- Keep track of changes

### 4. Customize for Your Context
After running SELF_DISCOVERY and understanding your working style:
- Add your tech stack preferences
- Include your active projects
- Reference your constraints
- Mention your goals

### 5. Create a Prompt Journal
Track which prompts you've used and when:
```
Date: 2026-01-02
Prompt: PRD.md
Project: ReImagine Interior AI v2
Output: prd-reimagine-v2.md
Next Steps: Run HLD.md for architecture
```

### 6. Use Examples Folder
As you use prompts, save good outputs in `examples/` folder for reference.

### 7. Mix and Match
Don't feel constrained by exact prompt structure - take sections from multiple prompts to create your ideal workflow.

---

## Customization Notes

### Personalized Prompts (⭐)

Three prompts have been customized for Vedanth Bora:
- **OPT_COACH.md**: References AI Engineer role at Krazimo
- **OPT.md**: Uses AI product examples (ReImagine Interior AI, Product Photoshoot AI)
- **VIBE_PPT.md**: Generic branding placeholders

After running `SELF_DISCOVERY.md`, you may want to further personalize other prompts with your specific context, tech stack, and goals.

---

## Contributing

As you use these prompts:
1. Note what works well and what doesn't
2. Customize prompts for your specific use cases
3. Create new prompts using `TEMPLATE_PROMPT.md`
4. Share examples of outputs in `examples/` folder

---

## Next Steps

1. ✅ **Run SELF_DISCOVERY.md first** - This will shape your context for all other prompts
2. Choose a prompt based on your current goal
3. Copy the entire prompt into your AI assistant
4. Follow the conversation flow
5. Save the output for reference
6. Iterate and improve

---

**Last Updated:** January 2, 2026
**Total Prompts:** 27
**Categories:** 6
