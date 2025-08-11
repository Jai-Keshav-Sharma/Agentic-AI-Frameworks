# 🚀 OpenAI Agents Framework: Advanced Multi-Agent Systems

This repository demonstrates the power of OpenAI's Agents Framework for building sophisticated multi-agent systems with tool integration, handoffs, guardrails, and web search capabilities. The collection progresses from basic agent creation to production-ready deep research systems.

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [🔧 Setup and Requirements](#-setup-and-requirements)
- [📚 Learning Journey](#-learning-journey)
  - [Lab 1: Basic Agent Creation](#lab-1-basic-agent-creation)
  - [Lab 2: Multi-Agent Sales System](#lab-2-multi-agent-sales-system)
  - [Lab 3: Cross-Platform Integration & Guardrails](#lab-3-cross-platform-integration--guardrails)
  - [Lab 4: Deep Research System](#lab-4-deep-research-system)
- [🏭 Production Application](#-production-application)
- [🏗️ Architecture Patterns](#️-architecture-patterns)
- [💼 Commercial Applications](#-commercial-applications)
- [📈 Key Learnings](#-key-learnings)

## 🎯 Overview

This collection showcases the evolution from simple agent interactions to complex multi-agent orchestrations capable of:
- Autonomous agent collaboration through tools and handoffs
- Cross-platform model integration (OpenAI, Groq, DeepSeek)
- Input/output guardrails for safety and compliance
- Web search and deep research capabilities
- Production-ready applications with streaming interfaces

```mermaid
graph TD
    A[Basic Agent Creation] --> B[Multi-Agent Sales System]
    B --> C[Cross-Platform Integration]
    C --> D[Deep Research System]
    D --> E[Production Application]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#ffebee
```

## 🔧 Setup and Requirements

### Prerequisites
- Python 3.8+
- OpenAI API Key (with Agents enabled)
- Optional: Groq API Key, DeepSeek API Key
- SendGrid API Key for email functionality

### Installation
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file with:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key          # Optional
DEEPSEEK_API_KEY=your_deepseek_api_key  # Optional
SENDGRID_API_KEY=your_sendgrid_api_key  # For email functionality
```

## 📚 Learning Journey

### Lab 1: Basic Agent Creation
**File:** [`1_lab.ipynb`](1_lab.ipynb)

Introduction to OpenAI Agents Framework fundamentals:

#### System Architecture:
```mermaid
flowchart LR
    A[Agent Definition] --> B[Runner Execution]
    B --> C[Result Processing]
    C --> D[Trace Analysis]
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
```

#### Key Features Demonstrated:
- **Agent Creation**: Simple agent with name, instructions, and model
- **Execution Patterns**: Using `Runner.run()` for agent execution
- **Tracing**: Built-in tracing for debugging and monitoring
- **OpenAI Platform Integration**: Direct trace viewing on OpenAI platform

#### Code Highlights:
```python
# Basic agent creation
agent = Agent(
    name="Jokester", 
    instructions="You are a professional joke teller", 
    model='gpt-4.1-nano'
)

# Execution with tracing
with trace("telling a joke"):
    result = await Runner.run(agent, "tell me the best joke")
```

---

### Lab 2: Multi-Agent Sales System
**File:** [`2_lab.ipynb`](2_lab.ipynb)

A comprehensive sales automation system demonstrating agent collaboration:

#### Multi-Agent Architecture:
```mermaid
sequenceDiagram
    participant SM as Sales Manager
    participant SA1 as Professional Agent
    participant SA2 as Engaging Agent  
    participant SA3 as Concise Agent
    participant SP as Sales Picker
    participant EA as Email Agent
    
    SM->>SA1: Generate sales email
    SM->>SA2: Generate sales email
    SM->>SA3: Generate sales email
    
    par Parallel Generation
        SA1->>SM: Professional email
        SA2->>SM: Engaging email  
        SA3->>SM: Concise email
    end
    
    SM->>SP: Pick best email
    SP->>SM: Selected email
    SM->>EA: Format & send email
    EA->>SM: Confirmation
```

#### Advanced Features:
1. **Agent Workflows**: Parallel execution of multiple sales agents
2. **Tools Integration**: Converting agents to tools for reusability
3. **Handoffs**: Seamless control transfer between agents
4. **Email Integration**: SendGrid API for actual email delivery

#### Key Innovations:
- **Agent-as-Tools**: Converting agents to reusable function tools
- **Selection Logic**: Automated best email selection
- **HTML Email Processing**: Subject writing and HTML conversion
- **Control Flow**: Manager agent orchestrating the entire process

#### Tool Integration Pattern:
```mermaid
graph TB
    subgraph "Sales Agents"
        A[Professional Agent]
        B[Engaging Agent]
        C[Concise Agent]
    end
    
    subgraph "Processing Agents"
        D[Subject Writer]
        E[HTML Converter]
    end
    
    subgraph "Output Tools"
        F[SendGrid Email]
    end
    
    A --> G[Sales Manager]
    B --> G
    C --> G
    G --> H[Email Agent]
    D --> H
    E --> H
    H --> F
    
    style G fill:#ffcdd2
    style H fill:#e8f5e8
```

---

### Lab 3: Cross-Platform Integration & Guardrails
**File:** [`3_lab.ipynb`](3_lab.ipynb)

Advanced system with multi-provider support and safety mechanisms:

#### Cross-Platform Architecture:
```mermaid
graph TD
    subgraph "Model Providers"
        A[OpenAI GPT-4]
        B[Groq Llama-3.3]
        C[DeepSeek Models]
    end
    
    subgraph "Agent System"
        D[Sales Manager]
        E[Email Agent]
        F[Guardrail System]
    end
    
    subgraph "Safety Layer"
        G[Input Guardrails]
        H[Name Detection]
        I[Tripwire System]
    end
    
    A --> D
    B --> D
    C --> D
    G --> F
    H --> F
    F --> I
    D --> E
    
    style F fill:#ffcdd2
    style I fill:#fff3e0
```

#### Guardrails System:
```mermaid
flowchart TD
    A[User Input] --> B[Input Guardrails]
    B --> C{Name Detected?}
    C -->|Yes| D[Tripwire Triggered]
    C -->|No| E[Process Normally]
    D --> F[Block/Modify Request]
    E --> G[Agent Processing]
    F --> H[Safe Response]
    G --> H
    
    style D fill:#ffcdd2
    style F fill:#ffcdd2
```

#### Key Features:
- **Multi-Provider Support**: OpenAI, Groq, and DeepSeek integration
- **Input Guardrails**: Pydantic-based safety checks
- **Tripwire System**: Automated blocking of problematic inputs
- **Cross-Model Collaboration**: Different models for different tasks

---

### Lab 4: Deep Research System
**File:** [`4_lab.ipynb`](4_lab.ipynb)

Production-ready research system with web search and structured outputs:

#### Research Pipeline Architecture:
```mermaid
flowchart TB
    subgraph "Planning Phase"
        A[User Query] --> B[Planner Agent]
        B --> C[Search Plan Generation]
    end
    
    subgraph "Execution Phase"
        C --> D[Parallel Web Searches]
        D --> E[Search Agent 1]
        D --> F[Search Agent 2]  
        D --> G[Search Agent N]
    end
    
    subgraph "Synthesis Phase"
        E --> H[Results Aggregation]
        F --> H
        G --> H
        H --> I[Writer Agent]
        I --> J[Structured Report]
    end
    
    subgraph "Delivery Phase"
        J --> K[Email Agent]
        K --> L[HTML Email Delivery]
    end
    
    style B fill:#e3f2fd
    style I fill:#f3e5f5
    style K fill:#e8f5e8
```

#### Advanced Components:

##### 1. **Structured Planning System**
```python
class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    
class WebSearchItem(BaseModel):
    reason: str  # Why this search matters
    query: str   # What to search for
```

##### 2. **Parallel Execution Engine**
```python
async def perform_searches(search_plan):
    tasks = [asyncio.create_task(search(item)) for item in search_plan.searches]
    results = await asyncio.gather(*tasks)
    return results
```

##### 3. **Comprehensive Output Structure**
```python
class ReportData(BaseModel):
    short_summary: str
    markdown_report: str
    follow_up_questions: list[str]
```

#### Web Search Integration:
- **OpenAI WebSearchTool**: Hosted web search capability
- **Cost-Aware Implementation**: Configurable search context size
- **Error Handling**: Graceful degradation for failed searches
- **Parallel Processing**: Concurrent search execution

---

## 🏭 Production Application
**Folder:** [`deep_research/`](deep_research/)

A complete production-ready research application with streaming interface:

### Application Architecture:
```mermaid
classDiagram
    class ResearchManager {
        +run(query: str)
        +plan_searches(query: str)
        +perform_searches(plan)
        +write_report(query, results)
        +send_email(report)
    }
    
    class PlannerAgent {
        +generate_search_plan()
        +output_type: WebSearchPlan
    }
    
    class SearchAgent {
        +web_search()
        +tools: WebSearchTool
    }
    
    class WriterAgent {
        +synthesize_report()
        +output_type: ReportData
    }
    
    class EmailAgent {
        +send_html_email()
        +tools: SendGrid
    }
    
    class GradioInterface {
        +streaming_ui()
        +progress_updates()
    }
    
    ResearchManager --> PlannerAgent
    ResearchManager --> SearchAgent
    ResearchManager --> WriterAgent
    ResearchManager --> EmailAgent
    GradioInterface --> ResearchManager
```

### Production Features:
- **Streaming Interface**: Real-time progress updates
- **Modular Design**: Separate agent files for maintainability
- **Error Recovery**: Graceful handling of failed searches
- **Trace Integration**: Built-in monitoring and debugging
- **Web Deployment**: Gradio-based web interface

### Key Files:
- `deep_research.py`: Main application with Gradio UI
- `research_manager.py`: Core orchestration logic
- `planner_agent.py`: Search planning intelligence
- `search_agent.py`: Web search execution
- `writer_agent.py`: Report synthesis
- `email_agent.py`: Email delivery

---

## 🏗️ Architecture Patterns

### 1. Agent Orchestration Pattern
```mermaid
graph TB
    A[Manager Agent] --> B[Worker Agent 1]
    A --> C[Worker Agent 2]
    A --> D[Worker Agent 3]
    B --> E[Result Aggregation]
    C --> E
    D --> E
    E --> F[Next Stage]
```

### 2. Tool Integration Pattern
```mermaid
flowchart LR
    A[Agent] --> B{Decision Point}
    B -->|Use Tool| C[Function Call]
    B -->|Direct Response| D[Text Output]
    C --> E[Tool Execution]
    E --> F[Result Processing]
    F --> G[Continue Conversation]
    D --> G
```

### 3. Handoff Pattern
```mermaid
sequenceDiagram
    participant A1 as Agent 1
    participant M as Manager
    participant A2 as Agent 2
    
    A1->>M: Task Complete
    M->>A2: Handoff Control
    A2->>M: Processing Result
    M->>A1: Final Result
```

### 4. Guardrail Pattern
```mermaid
flowchart TD
    A[Input] --> B[Guardrail Check]
    B --> C{Safe?}
    C -->|Yes| D[Process]
    C -->|No| E[Block/Modify]
    D --> F[Output]
    E --> G[Safe Alternative]
```

## 💼 Commercial Applications

### 1. **Automated Sales Development**
- Multi-style email generation
- A/B testing through parallel agents
- Automated lead qualification
- CRM integration capabilities

### 2. **Market Research Automation**
- Comprehensive topic analysis
- Real-time web data integration
- Structured report generation
- Stakeholder communication

### 3. **Content Creation Pipeline**
- Research-driven content
- Multi-format output generation
- Quality assurance through multiple agents
- Distribution automation

### 4. **Customer Support Intelligence**
- Query categorization
- Response quality validation
- Escalation management
- Knowledge base updates

### 5. **Compliance and Safety Systems**
- Input validation and filtering
- Policy enforcement
- Audit trail maintenance
- Risk mitigation

## 📈 Key Learnings

### Technical Insights:

#### 1. **Agent Design Principles**
- **Single Responsibility**: Each agent should have a focused purpose
- **Clear Instructions**: Precise instructions lead to better outcomes
- **Model Selection**: Match model capabilities to task requirements

#### 2. **Collaboration Patterns**
- **Tools vs Handoffs**: Tools return control, handoffs transfer it
- **Async Execution**: Parallel processing dramatically improves performance
- **State Management**: Careful context passing between agents

#### 3. **Production Considerations**
- **Error Handling**: Graceful degradation for failed operations
- **Cost Management**: Monitor API usage, especially for web search
- **Observability**: Built-in tracing is essential for debugging

### Business Insights:

#### 1. **Quality Through Diversity**
- Multiple agents provide different perspectives
- Selection mechanisms improve final output quality
- A/B testing becomes built-in capability

#### 2. **Scalability Through Modularity**
- Agent-as-tools pattern enables reuse
- Clear separation of concerns
- Easy addition of new capabilities

#### 3. **Safety First**
- Guardrails are essential for production systems
- Input validation prevents problematic outputs
- Compliance requirements can be automated

### Best Practices:

#### 1. **Development Workflow**
- Start simple with basic agents
- Add complexity incrementally
- Use tracing extensively for debugging
- Test error conditions early

#### 2. **Production Deployment**
- Implement comprehensive monitoring
- Plan for API rate limits and costs
- Design for graceful degradation
- Maintain audit trails

#### 3. **Agent Design**
- Use structured outputs (Pydantic) for reliability
- Implement proper tool descriptions
- Consider context length limitations
- Plan for multi-model scenarios

---

## 🔗 Navigation Links

- [🏠 Back to Main Repository](../README.md)
- [📂 View Source Code](.)
- [🚀 Run Deep Research App](deep_research/deep_research.py)
- [📊 Explore Notebooks](.)
- [🔍 OpenAI Traces](https://platform.openai.com/traces)

---

## 🎯 Next Steps

After mastering these concepts, you're ready to:
- Build custom multi-agent systems for your domain
- Integrate with enterprise systems and APIs
- Implement sophisticated workflow automation
- Create production-ready AI applications

*This module demonstrates the power of orchestrated AI agents working together to solve complex, real-world problems.*
