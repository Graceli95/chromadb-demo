# 🚀 ChromaDB Demo - A Comprehensive Learning Guide

A step-by-step tutorial project demonstrating ChromaDB's capabilities, from basic setup to advanced OpenAI embeddings integration. Perfect for junior developers learning vector databases and semantic search!

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-1.1.1-green.svg)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📚 Table of Contents

- [About This Project](#about-this-project)
- [What You'll Learn](#what-youll-learn)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Step-by-Step Guide](#step-by-step-guide)
- [Running the Examples](#running-the-examples)
- [OpenAI Integration](#openai-integration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Resources](#resources)

---

## 🎯 About This Project

This repository contains a complete, hands-on tutorial for learning **ChromaDB**, a powerful vector database for semantic search and AI applications. Each step builds on the previous one, with well-commented code and clear explanations.

**What is ChromaDB?**
ChromaDB is an AI-native open-source embedding database. Think of it as a smart filing cabinet that understands the *meaning* of your text, not just exact keyword matches.

**Use Cases:**
- 🤖 Building chatbots with memory
- 📄 Document search and retrieval
- 🔍 Semantic search engines
- 💬 Question-answering systems
- 🧠 AI applications with context awareness

---

## 🎓 What You'll Learn

### Core Concepts
- ✅ Vector databases and embeddings
- ✅ Semantic search vs keyword search
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ Collection management
- ✅ Persistent vs in-memory storage
- ✅ Default vs custom embedding models

### Practical Skills
- ✅ Setting up Python virtual environments
- ✅ Installing and configuring ChromaDB
- ✅ Writing natural language queries
- ✅ Integrating OpenAI's embedding models
- ✅ Managing API keys securely
- ✅ Understanding tokens and costs

---

## 📋 Prerequisites

- **Python 3.9+** installed on your system
- **pip** (Python package manager)
- **Git** for cloning the repository
- **Basic Python knowledge** (functions, imports, variables)
- **(Optional)** OpenAI API key for Step 6

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Graceli95/chromadb-demo.git
cd chromadb-demo
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Your First Example
```bash
python test_installation.py
```

You should see:
```
✅ ChromaDB imported successfully!
ChromaDB version: 1.1.1
```

---

## 📁 Project Structure

```
chromadb-demo/
├── README.md                      # This file
├── SETUP_OPENAI_API_KEY.md       # OpenAI API key setup guide
├── chromadb-guide.md             # Original comprehensive guide
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
│
├── test_installation.py         # Verify ChromaDB installation
│
├── step2_create_collection.py   # Step 2: Creating collections
├── step3_crud_operations.py     # Step 3: CRUD operations
├── step4_persistent_storage.py  # Step 4: Persistent database
├── step5_manage_collections.py  # Step 5: Collection management
├── step6_openai_embeddings.py   # Step 6: OpenAI integration
│
└── chroma_db/                   # Persistent database storage (gitignored)
```

---

## 📖 Step-by-Step Guide

### Step 1: Installation ✅
**File:** `requirements.txt`, `test_installation.py`

Learn how to set up ChromaDB with a Python virtual environment.

```bash
python test_installation.py
```

**Key Concepts:**
- Virtual environments
- Package installation
- Dependency management

---

### Step 2: Creating Collections 🗂️
**File:** `step2_create_collection.py`

Create your first "filing cabinet" (collection) for storing documents.

```bash
python step2_create_collection.py
```

**Key Concepts:**
- ChromaDB Client initialization
- Collection creation
- get_or_create_collection method

**Code Example:**
```python
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="travel_policies")
```

---

### Step 3: CRUD Operations 📝
**File:** `step3_crud_operations.py`

Master Create, Read, Update, and Delete operations on documents.

```bash
python step3_crud_operations.py
```

**Key Concepts:**
- Adding documents with metadata
- Semantic search queries
- Updating documents with upsert
- Deleting documents

**Code Example:**
```python
# Add documents
collection.add(
    ids=["policy_01"],
    documents=["Employees must book economy class for domestic flights."],
    metadatas=[{"policy_type": "flights"}]
)

# Query with natural language
results = collection.query(
    query_texts=["What is the flight policy?"],
    n_results=2
)
```

---

### Step 4: Persistent Storage 💾
**File:** `step4_persistent_storage.py`

Save your data permanently to disk instead of losing it when the program ends.

```bash
python step4_persistent_storage.py
# Run it twice to see data persistence!
```

**Key Concepts:**
- In-memory vs persistent databases
- PersistentClient
- Data durability

**Code Example:**
```python
# Data survives program restarts!
persistent_client = chromadb.PersistentClient(path="./chroma_db")
collection = persistent_client.get_or_create_collection(name="saved_policies")
```

---

### Step 5: Managing Collections 🗃️
**File:** `step5_manage_collections.py`

Learn to create, list, modify, and delete entire collections.

```bash
python step5_manage_collections.py
```

**Key Concepts:**
- Listing all collections
- Renaming collections
- Deleting collections
- Organization strategies

**Code Example:**
```python
# List all collections
all_collections = client.list_collections()

# Rename a collection
collection.modify(name="new_name")

# Delete a collection (careful!)
client.delete_collection(name="old_collection")
```

---

### Step 6: OpenAI Embeddings 🧠
**File:** `step6_openai_embeddings.py`

Integrate OpenAI's powerful embedding models for enhanced semantic understanding.

```bash
# Set up your API key first (see SETUP_OPENAI_API_KEY.md)
export OPENAI_API_KEY='your-key-here'

python step6_openai_embeddings.py
```

**Key Concepts:**
- Custom embedding functions
- OpenAI's text-embedding-3-small model
- Token counting and costs
- Comparing embedding models

**Code Example:**
```python
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    model_name="text-embedding-3-small",
    api_key=os.environ['OPENAI_API_KEY']
)

collection = client.get_or_create_collection(
    name="my_collection",
    embedding_function=openai_ef
)
```

---

## 🏃 Running the Examples

### Run All Steps Sequentially
```bash
# Activate virtual environment
source venv/bin/activate

# Run each step
python step2_create_collection.py
python step3_crud_operations.py
python step4_persistent_storage.py
python step5_manage_collections.py
python step6_openai_embeddings.py  # Requires API key
```

### Run Individual Steps
Each script is standalone and can be run independently:
```bash
python step3_crud_operations.py
```

### Clear Persistent Data
If you want to start fresh:
```bash
rm -rf chroma_db/
```

---

## 🔑 OpenAI Integration

To use OpenAI embeddings in Step 6, you need an API key.

### Quick Setup (macOS/Linux)
```bash
# Add to ~/.zshrc or ~/.bashrc
export OPENAI_API_KEY='sk-your-key-here'

# Reload shell configuration
source ~/.zshrc  # or source ~/.bashrc
```

### Detailed Instructions
See [SETUP_OPENAI_API_KEY.md](SETUP_OPENAI_API_KEY.md) for:
- Getting your API key
- Setting environment variables
- Troubleshooting common issues
- Security best practices
- Alternative setup methods

### Cost Estimation
The `text-embedding-3-small` model costs approximately:
- **$0.00002 per 1,000 tokens**
- Running Step 6 costs less than $0.01
- Average document: 10-50 tokens

---

## 🔧 Troubleshooting

### Import Error: No module named 'chromadb'
**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### OpenAI API Key Not Found
**Solution:**
```bash
# Check if the key is set
echo $OPENAI_API_KEY

# If empty, set it
export OPENAI_API_KEY='your-key-here'
```

See [SETUP_OPENAI_API_KEY.md](SETUP_OPENAI_API_KEY.md) for detailed troubleshooting.

### Permission Denied on macOS
**Solution:**
```bash
# Use python3 instead of python
python3 -m venv venv
```

### Persistent Database Issues
**Solution:**
```bash
# Clear the database and start fresh
rm -rf chroma_db/
python step4_persistent_storage.py
```

---

## 🤝 Contributing

This is a learning project, but contributions are welcome!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Add clear comments and documentation
5. Test your changes
6. Commit with descriptive messages
7. Push to your fork
8. Open a Pull Request

### Contribution Ideas
- Add more example use cases
- Create Jupyter notebooks
- Add visualization of embeddings
- Implement a simple web interface
- Add more embedding model comparisons
- Improve documentation

---

## 📚 Resources

### Official Documentation
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

### Learning Resources
- [What are Vector Databases?](https://www.pinecone.io/learn/vector-database/)
- [Understanding Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Semantic Search Explained](https://www.elastic.co/what-is/semantic-search)

### Related Projects
- [LangChain](https://github.com/langchain-ai/langchain) - Building applications with LLMs
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for LLM applications
- [Pinecone](https://www.pinecone.io/) - Alternative vector database

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- **ChromaDB Team** - For creating an amazing vector database
- **OpenAI** - For powerful embedding models
- **ASU AZNext Program** - For supporting this educational initiative
- **JesterCharles** - Original guide author

---

## 📬 Contact & Support

- **Repository:** [github.com/Graceli95/chromadb-demo](https://github.com/Graceli95/chromadb-demo)
- **Issues:** [Report a bug or request a feature](https://github.com/Graceli95/chromadb-demo/issues)

---

## 🎓 Learning Path

**Beginner** → Start with Steps 1-3  
**Intermediate** → Complete Steps 4-5  
**Advanced** → Master Step 6 with OpenAI integration

---

## ⭐ Star This Repository

If you find this helpful, please consider giving it a star! It helps others discover this learning resource.

---

**Happy Learning! 🚀**

*Last Updated: October 19, 2025*

