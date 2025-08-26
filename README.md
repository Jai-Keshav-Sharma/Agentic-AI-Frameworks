# 🤖 Agentic AI Frameworks: Complete Multi-Agent Systems Mastery

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: All Rights Reserved](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](#license)
[![Frameworks](https://img.shields.io/badge/Frameworks-6-green.svg)](#frameworks-overview)
[![Production Ready](https://img.shields.io/badge/Production-Ready-success.svg)](#production-applications)

A comprehensive implementation of cutting-edge agentic AI frameworks, showcasing the complete spectrum of multi-agent orchestration technologies. This repository demonstrates advanced implementations across OpenAI Agents, CrewAI, LangGraph, AutoGen, and Model Context Protocol (MCP) integrations.

## 🌟 What I Built

Complete multi-agent systems implementations featuring:

- **🔧 Foundation Building**: Core agentic AI concepts and architecture patterns
- **🚀 OpenAI Agents**: Advanced multi-agent systems with tool integration
- **👥 CrewAI**: Production-ready agent orchestration and collaboration
- **🕸️ LangGraph**: State machine-based agent workflows and memory systems
- **🤖 AutoGen**: Microsoft's distributed agent communication framework
- **🔌 MCP Integration**: Tool ecosystem integration via Model Context Protocol

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor': '#4CAF50', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#4CAF50', 'lineColor': '#ffffff', 'sectionBkColor': '#1e1e1e', 'altSectionBkColor': '#2d2d2d', 'gridColor': '#404040', 'textColor': '#ffffff', 'taskBkColor': '#404040', 'taskTextColor': '#ffffff', 'taskTextLightColor': '#ffffff', 'taskTextOutsideColor': '#ffffff', 'activeTaskBkColor': '#4CAF50', 'activeTaskBorderColor': '#4CAF50', 'cScale0': '#1a1a2e', 'cScale1': '#16213e', 'cScale2': '#0f3460', 'cScale3': '#533483', 'cScale4': '#7209b7', 'cScale5': '#a663cc'}}}%%
graph TB
    subgraph "🎯 Implementation Journey"
        A[🔧 Foundations<br/>Core Concepts & LLM Integration] --> B[🚀 OpenAI Agents<br/>Multi-Agent Systems]
        B --> C[👥 CrewAI<br/>Production Orchestration]
        C --> D[🕸️ LangGraph<br/>State-Based Workflows]
        D --> E[🤖 AutoGen<br/>Distributed Systems]
        E --> F[🔌 MCP Integration<br/>Tool Ecosystems]
    end
    
    subgraph "💼 Production Implementations"
        G[📊 Trading Systems]
        H[🔍 Research Platforms]
        I[💬 Customer Support]
        J[📝 Content Generation]
        K[🛡️ Compliance Systems]
    end
    
    F --> G
    F --> H
    F --> I
    F --> J
    F --> K
```

## 📋 Table of Contents

- [🚀 Implementation Overview](#-implementation-overview)
- [🏗️ Framework Implementations](#️-framework-implementations)
- [📚 Development Journey](#-development-journey)
- [🎯 Key Projects Built](#-key-projects-built)
- [💼 Production Systems](#-production-systems)
- [🛠️ Technical Architecture](#️-technical-architecture)
- [🔧 Setup Instructions](#-setup-instructions)
- [📖 Technical Documentation](#-technical-documentation)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🚀 Getting Started

### System Requirements
- Python 3.13+ 
- OpenAI API Key
- Git

### Installation & Setup
```bash
# Clone the repository
git clone https://github.com/Jai-Keshav-Sharma/Agentic-AI-Frameworks.git
cd Agentic-AI-Frameworks

# Environment setup
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
# OR using uv (recommended)
uv sync
```

### Configuration
```bash
# Add API keys to .env
echo "OPENAI_API_KEY=your_openai_key_here" >> .env
echo "LANGCHAIN_API_KEY=your_langchain_key_here" >> .env
```

### Running the Systems
```python
# Test basic functionality
python main.py

# Run specific implementations
cd 1_foundations && jupyter notebook 1_lab.ipynb
```

## 🏗️ Framework Implementations

Each framework implementation demonstrates different approaches to multi-agent systems:

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor': '#4CAF50', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#4CAF50', 'lineColor': '#ffffff', 'sectionBkColor': '#1e1e1e', 'altSectionBkColor': '#2d2d2d', 'gridColor': '#404040', 'textColor': '#ffffff', 'taskBkColor': '#404040', 'taskTextColor': '#ffffff', 'taskTextLightColor': '#ffffff', 'taskTextOutsideColor': '#ffffff', 'activeTaskBkColor': '#4CAF50', 'activeTaskBorderColor': '#4CAF50'}}}%%
graph TB
    subgraph "🔧 Foundations"
        A1[LLM Fundamentals]
        A2[Agent Architecture]
        A3[Tool Integration]
        A4[Business Applications]
    end
    
    subgraph "🚀 OpenAI Agents"
        B1[Multi-Agent Systems]
        B2[Tool Integration]
        B3[Cross-Platform Support]
        B4[Production Research App]
    end
    
    subgraph "👥 CrewAI"
        C1[Agent Orchestration]
        C2[Memory Systems]  
        C3[Hierarchical Management]
        C4[5 Production Projects]
    end
    
    subgraph "🕸️ LangGraph"
        D1[State Machines]
        D2[Memory Persistence]
        D3[Workflow Control]
        D4[The Sidekick App]
    end
    
    subgraph "🤖 AutoGen"
        E1[Distributed Runtime]
        E2[Agent Communication]
        E3[Meta-Programming]
        E4[Agent Creator System]
    end
    
    subgraph "🔌 MCP Protocol"
        F1[Tool Standardization]
        F2[Custom Servers]
        F3[Multi-Server Integration]
        F4[Autonomous Trading Floor]
    end
```

### Implementation Summary

| Framework | Implementation Focus | Built Applications | Complexity |
|-----------|---------------------|-------------------|------------|
| **🔧 Foundations** | Core concepts, architecture patterns | Educational demos, business cases | ⭐⭐ |
| **🚀 OpenAI Agents** | Native OpenAI integration | Multi-agent research platform | ⭐⭐⭐ |
| **👥 CrewAI** | Production orchestration | 5 enterprise applications | ⭐⭐⭐⭐ |
| **🕸️ LangGraph** | State-based workflows | The Sidekick assistant | ⭐⭐⭐⭐ |
| **🤖 AutoGen** | Distributed systems | Agent Creator meta-system | ⭐⭐⭐⭐⭐ |
| **🔌 MCP** | Tool ecosystem integration | Autonomous trading floor | ⭐⭐⭐⭐ |

## 📚 Development Journey

### 🔧 Phase 1: Foundation Development (Weeks 1-2)
**Built:** [`1_foundations/`](1_foundations/)
- Core LLM integration patterns
- Basic agent architecture implementations
- Tool integration frameworks
- Business case development

### 🚀 Phase 2: OpenAI & CrewAI Systems (Weeks 3-4)
**Built:** [`2_openai/`](2_openai/) → [`3_crew/`](3_crew/)
- Multi-agent orchestration systems
- Production-ready frameworks
- Memory and persistence layers
- Real-world applications

### 🏆 Phase 3: Advanced Architectures (Weeks 5-8)
**Built:** [`4_langgraph/`](4_langgraph/) → [`5_autogen/`](5_autogen/) → [`6_mcp/`](6_mcp/)
- State machine workflows
- Distributed agent systems
- Meta-programming capabilities
- Protocol-based integrations

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#7C3AED', 'lineColor': '#ffffff', 'sectionBkColor': '#1a1a1a', 'altSectionBkColor': '#262626', 'gridColor': '#333333', 'secondaryColor': '#1a1a1a', 'tertiaryColor': '#333333'}}}%%
gantt
    title Implementation Timeline
    dateFormat  X
    axisFormat %s
    
    section Foundations
    🔧 Core Concepts    :done, foundations1, 1, 2
    💡 Python & APIs   :done, foundations2, 1, 2
    
    section OpenAI + CrewAI
    🚀 Multi-Agents     :done, openai1, 3, 4
    🎯 Production Apps  :done, openai2, 3, 4
    
    section LangGraph + AutoGen
    🕸️ State Machines   :done, langgraph1, 5, 6
    🏗️ Distributed Sys :done, autogen1, 5, 6
    
    section MCP + Production
    🔌 Tool Integration :done, mcp1, 7, 8
    💼 Enterprise Apps  :done, production1, 7, 8
```

## 🎯 Key Projects Built

### 🏆 Flagship Applications

#### 📊 Autonomous Trading Floor (MCP)
**Location:** [`6_mcp/Autonomous Stock Trading Environment/`](6_mcp/Autonomous%20Stock%20Trading%20Environment/)

Complete autonomous trading system with 4 AI trader personalities:
- **Warren**: Value investment focus (GPT-4.1-Mini)
- **George**: Bold trading strategies (DeepSeek V3)
- **Ray**: Systematic analysis (Gemini 2.5 Flash)
- **Cathie**: Tech innovation focus (Grok 3 Mini)

**Features:**
- 44 integrated MCP tools
- Real-time market data integration
- Multi-model AI architecture
- Live web dashboard
- Push notification system

#### 🤖 Agent Creator System (AutoGen)
**Location:** [`5_autogen/Agent Creator/`](5_autogen/Agent%20Creator/)

Revolutionary meta-programming system where agents create other agents:
- Autonomous agent generation
- Collaborative idea refinement
- Dynamic specialization
- Emergent creativity networks

#### 🤝 The Sidekick (LangGraph)
**Location:** [`4_langgraph/The Sidekick/`](4_langgraph/The%20Sidekick/)

Advanced personal assistant with persistent memory:
- Long-term conversation memory
- Context-aware responses
- Tool integration capabilities
- State-based workflow management

#### 🔍 Deep Research Platform (OpenAI)
**Location:** [`2_openai/deep_research/`](2_openai/deep_research/)

Production research application with streaming interface:
- Multi-agent research coordination
- Real-time progress updates
- Email delivery integration
- Comprehensive report generation

### 📁 Project Portfolio

#### CrewAI Productions ([`3_crew/`](3_crew/))
1. **Coder**: Autonomous programming agent
2. **Debate**: Multi-perspective analysis system  
3. **Engineering Team**: Full-stack development crew
4. **Financial Researcher**: Investment analysis platform
5. **Stock Picker**: Intelligent investment advisor

#### Foundation Applications ([`1_foundations/`](1_foundations/))
- Business case development
- LLM interaction patterns
- Tool integration examples
- Regulatory compliance frameworks

## 💼 Production Applications

### Architecture Patterns Implemented

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#7C3AED', 'lineColor': '#ffffff', 'sectionBkColor': '#1a1a1a', 'altSectionBkColor': '#262626', 'gridColor': '#333333', 'secondaryColor': '#1a1a1a', 'tertiaryColor': '#333333'}}}%%
graph TB
    subgraph "🏢 Enterprise Applications"
        A[Customer Support<br/>Intelligence]
        B[Business Process<br/>Automation]
        C[Decision Support<br/>Systems]
        D[Compliance &<br/>Risk Management]
    end
    
    subgraph "💰 Financial Services"
        E[Portfolio<br/>Management]
        F[Market Research<br/>& Analysis]
        G[Risk Assessment<br/>& Monitoring]
        H[Regulatory<br/>Reporting]
    end
    
    subgraph "🚀 Technology Solutions"
        I[Software Development<br/>Automation]
        J[Content Creation<br/>& Curation]
        K[Research &<br/>Development]
        L[Integration<br/>Platforms]
    end
    
    subgraph "🛠️ Core Technologies"
        M[Multi-Agent<br/>Orchestration]
        N[Memory &<br/>Persistence]
        O[Tool Integration<br/>& APIs]
        P[Real-time<br/>Communication]
    end
    
    A --> M
    B --> N
    C --> O
    D --> P
    E --> M
    F --> N
    G --> O
    H --> P
    I --> M
    J --> N
    K --> O
    L --> P
    
    classDef enterprise fill:#164e63,stroke:#0891b2,stroke-width:2px,color:#ffffff
    classDef financial fill:#7c2d12,stroke:#dc2626,stroke-width:2px,color:#ffffff
    classDef technology fill:#581c87,stroke:#7c3aed,stroke-width:2px,color:#ffffff
    classDef core fill:#365314,stroke:#65a30d,stroke-width:2px,color:#ffffff
    
    class A,B,C,D enterprise
    class E,F,G,H financial
    class I,J,K,L technology
    class M,N,O,P core
```

### Industry Applications

#### 🏦 Financial Services
- **Algorithmic Trading**: Autonomous decision-making systems
- **Risk Management**: Real-time monitoring and assessment
- **Customer Advisory**: Personalized investment guidance
- **Compliance Automation**: Regulatory requirement management

#### 🏢 Enterprise Operations
- **Customer Support**: Intelligent ticket routing and resolution
- **Process Automation**: Workflow optimization and management
- **Knowledge Management**: Information discovery and curation
- **Quality Assurance**: Automated testing and validation

#### 💻 Technology Development
- **Code Generation**: Automated programming assistance
- **Testing Automation**: Comprehensive quality assurance
- **Documentation**: Self-generating technical documentation
- **Integration Services**: API and service orchestration

## 🛠️ Technical Architecture

### System Components Built

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#7C3AED', 'lineColor': '#ffffff', 'sectionBkColor': '#1a1a1a', 'altSectionBkColor': '#262626', 'gridColor': '#333333', 'secondaryColor': '#1a1a1a', 'tertiaryColor': '#333333'}}}%%
graph TB
    subgraph "🧠 AI Models"
        A1[OpenAI GPT-4/4o]
        A2[DeepSeek V3]
        A3[Google Gemini 2.5]
        A4[Anthropic Claude]
        A5[xAI Grok]
    end
    
    subgraph "🔧 Agent Frameworks"
        B1[OpenAI Agents SDK]
        B2[CrewAI]
        B3[LangGraph]
        B4[AutoGen]
        B5[Custom Implementations]
    end
    
    subgraph "🔌 Integration Layer"
        C1[MCP Protocol]
        C2[LangChain Tools]
        C3[Custom APIs]
        C4[Web Services]
        C5[Database Connections]
    end
    
    subgraph "💾 Persistence"
        D1[SQLite Databases]
        D2[Memory Systems]
        D3[File Storage]
        D4[Vector Databases]
        D5[Knowledge Graphs]
    end
    
    subgraph "🌐 User Interfaces"
        E1[Jupyter Notebooks]
        E2[Gradio Web Apps]
        E3[CLI Applications]
        E4[REST APIs]
        E5[Real-time Dashboards]
    end
    
    A1 --> B1
    A2 --> B2
    A3 --> B3
    A4 --> B4
    A5 --> B5
    
    B1 --> C1
    B2 --> C2
    B3 --> C3
    B4 --> C4
    B5 --> C5
    
    C1 --> D1
    C2 --> D2
    C3 --> D3
    C4 --> D4
    C5 --> D5
    
    D1 --> E1
    D2 --> E2
    D3 --> E3
    D4 --> E4
    D5 --> E5
    
    classDef models fill:#1a1a2e,stroke:#16213e,stroke-width:2px,color:#ffffff
    classDef frameworks fill:#16213e,stroke:#0f3460,stroke-width:2px,color:#ffffff
    classDef integration fill:#0f3460,stroke:#533483,stroke-width:2px,color:#ffffff
    classDef persistence fill:#533483,stroke:#7209b7,stroke-width:2px,color:#ffffff
    classDef interfaces fill:#7209b7,stroke:#a663cc,stroke-width:2px,color:#ffffff
    
    class A1,A2,A3,A4,A5 models
    class B1,B2,B3,B4,B5 frameworks
    class C1,C2,C3,C4,C5 integration
    class D1,D2,D3,D4,D5 persistence
    class E1,E2,E3,E4,E5 interfaces
```

### Technology Stack

#### **Core Dependencies**
```toml
[project.dependencies]
gradio = ">=5.35.0"           # Web interfaces
langchain = ">=0.3.26"        # LLM orchestration  
langgraph = ">=0.5.3"         # State-based workflows
openai = ">=1.93.0"           # OpenAI integration
openai-agents = ">=0.1.0"     # OpenAI Agents SDK
python-dotenv = ">=1.1.1"     # Environment management
requests = ">=2.32.4"         # HTTP operations
```

#### **Framework Integrations**
- **CrewAI**: Production agent orchestration
- **AutoGen**: Distributed multi-agent systems
- **LangGraph**: Workflow state management
- **MCP**: Standardized tool integration

#### **External Services**
- **OpenAI**: GPT models and embeddings
- **DeepSeek**: Advanced reasoning capabilities
- **Google**: Gemini model integration
- **Anthropic**: Claude model support
- **Various APIs**: Market data, search, notifications

## 🔧 Development Setup

### Development Environment

```bash
# Development with uv (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync

# Development with pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Environment configuration
cp .env.example .env
# Edit .env with your API keys and configuration
```

### API Keys Required

```bash
# Core APIs (Required)
OPENAI_API_KEY=your_openai_key

# Extended functionality (Optional)
LANGCHAIN_API_KEY=your_langchain_key
SERPER_API_KEY=your_serper_key         # Web search
BRAVE_API_KEY=your_brave_key           # Alternative search
POLYGON_API_KEY=your_polygon_key       # Financial data
SENDGRID_API_KEY=your_sendgrid_key     # Email delivery

# Model providers (Optional)
DEEPSEEK_API_KEY=your_deepseek_key
OPENROUTER_API_KEY=your_openrouter_key
```

### Testing and Validation

```bash
# Run basic functionality test
python main.py

# Test individual frameworks
cd 1_foundations && jupyter notebook
cd 2_openai && jupyter notebook
cd 3_crew && uv run src/coder/main.py
cd 4_langgraph && jupyter notebook
cd 5_autogen && jupyter notebook  
cd 6_mcp && jupyter notebook

# Run production applications
cd 6_mcp && uv run app.py                    # Trading dashboard
cd 4_langgraph/The\ Sidekick && python app.py  # Sidekick assistant
cd 2_openai/deep_research && python deep_research.py  # Research platform
```

## 📖 Documentation

### Framework-Specific Guides

| Framework | Documentation | Key Features |
|-----------|--------------|--------------|
| **🔧 [Foundations](1_foundations/)** | [README.md](1_foundations/README.md) | Core concepts, business applications |
| **🚀 [OpenAI Agents](2_openai/)** | [README.md](2_openai/README.md) | Multi-agent systems, tool integration |
| **👥 [CrewAI](3_crew/)** | [README.md](3_crew/README.md) | Agent orchestration, memory systems |
| **🕸️ [LangGraph](4_langgraph/)** | [README.md](4_langgraph/README.md) | State machines, workflow control |
| **🤖 [AutoGen](5_autogen/)** | [README.md](5_autogen/README.md) | Distributed systems, meta-programming |
| **🔌 [MCP](6_mcp/)** | [README.md](6_mcp/README.md) | Tool protocols, integration standards |

### External Resources

- **OpenAI Agents**: [Official Documentation](https://platform.openai.com/docs/agents)
- **CrewAI**: [Framework Guide](https://docs.crewai.com/)
- **LangGraph**: [State Machine Guide](https://langchain-ai.github.io/langgraph/)
- **AutoGen**: [Microsoft Documentation](https://microsoft.github.io/autogen/)
- **MCP Protocol**: [Specification](https://spec.modelcontextprotocol.io/)

### Learning Resources

- **Jupyter Notebooks**: Interactive learning experiences
- **Production Examples**: Real-world implementation patterns
- **Architecture Diagrams**: System design and component relationships
- **Best Practices**: Development and deployment guidelines

## 🤝 Contributing

### Development Workflow

1. **Fork the Repository**
   ```bash
   git fork https://github.com/Jai-Keshav-Sharma/Agentic-AI-Frameworks
   cd Agentic-AI-Frameworks
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-enhancement
   ```

3. **Develop and Test**
   ```bash
   # Make your changes
   # Test thoroughly across frameworks
   uv sync && python -m pytest  # If tests exist
   ```

4. **Submit Pull Request**
   - Clear description of changes
   - Include relevant documentation updates
   - Test results and validation steps

### Contribution Areas

- **New Framework Integration**: Additional agentic AI frameworks
- **Production Examples**: Real-world use case implementations
- **Documentation**: Improved guides and tutorials
- **Performance Optimization**: Speed and resource improvements
- **Testing**: Comprehensive test coverage
- **Bug Fixes**: Issue resolution and stability improvements

### Code Standards

- **Python 3.13+**: Latest Python features and typing
- **Type Hints**: Comprehensive type annotations
- **Documentation**: Clear docstrings and comments  
- **Environment Management**: Proper .env and secrets handling
- **Error Handling**: Graceful failure and recovery patterns

---

## 🎯 Next Steps

### 🚀 Get Started Immediately
1. **Clone the repository** and set up your environment
2. **Configure API keys** for the services you want to explore
3. **Start with [Foundations](1_foundations/)** to build core understanding
4. **Pick a framework** that matches your interests or business needs
5. **Build a project** using the patterns and examples provided

### 🏗️ Build Production Systems
- **Scale the trading floor** with additional traders and strategies
- **Deploy research platforms** for your organization's needs
- **Create custom MCP servers** for your specific business tools
- **Develop agent orchestration systems** for complex workflows

### 🌟 Join the Community
- **Share your implementations** and learnings
- **Contribute to the codebase** with improvements and new features
- **Connect with other practitioners** building agentic AI systems
- **Stay updated** with the latest developments in the field

---

**🔥 Ready to master agentic AI?** Start your journey with [`1_foundations/`](1_foundations/) and build toward production-ready autonomous systems that can transform your business operations.

*This comprehensive repository represents the current state of agentic AI technology, providing both educational foundations and production-ready patterns for building sophisticated multi-agent systems.*

## 📄 License

**© 2025 Jai Keshav Sharma. All Rights Reserved.**

This repository and all its contents are proprietary and confidential. The code, documentation, and materials are provided for **educational and reference purposes only**.

### ⚠️ Usage Restrictions:
- ✅ **Viewing**: You may view and read the code for learning and understanding
- ✅ **Education**: You may reference concepts and patterns for educational purposes
- ❌ **Commercial Use**: No commercial use of any code or materials
- ❌ **Redistribution**: No copying, sharing, or redistributing any part of this repository
- ❌ **Modification**: No creating derivative works or modifications
- ❌ **Production Use**: No use in production systems or applications
- ❌ **Integration**: No incorporating any code into other projects

### 📚 Educational Fair Use:
- You may discuss concepts and approaches learned from this repository
- You may reference architectural patterns in academic or educational contexts
- You may cite this work with proper attribution for educational purposes

### 🔒 Enforcement:
This repository is protected by copyright law. Unauthorized use, reproduction, or distribution may result in legal action.

**For licensing inquiries or permissions beyond educational use, please contact: ksharma9719@gmail.com**
