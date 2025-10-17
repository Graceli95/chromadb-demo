# Step 4: Saving Your Work (Persistent Database)
# Learn how to save your data permanently so it survives between program runs

import chromadb
import os

print("=" * 60)
print("STEP 4: PERSISTENT DATABASE")
print("=" * 60)

# ============================================================================
# DEMONSTRATION: In-Memory vs Persistent
# ============================================================================
print("\n📝 First, let's see the problem with in-memory databases...")
print("-" * 60)

# In-memory database (data disappears when program ends)
temp_client = chromadb.Client()
temp_collection = temp_client.get_or_create_collection(name="temporary_data")

temp_collection.add(
    ids=["temp_doc_01"],
    documents=["This document will disappear when the program ends!"]
)

print(f"✅ Added document to in-memory collection")
print(f"   Collection count: {temp_collection.count()}")
print(f"   ⚠️  WARNING: This data only exists in RAM (temporary memory)")
print(f"   When this program ends, the data will be GONE!")

# ============================================================================
# SOLUTION: Use PersistentClient
# ============================================================================
print("\n\n💾 Now let's save data permanently using PersistentClient...")
print("-" * 60)

# PersistentClient saves data to a folder on your hard drive
# We'll use the folder "./chroma_db" (the "./" means current directory)
# ChromaDB will create this folder if it doesn't exist

# Define the path where we want to save our data
db_path = "./chroma_db"

print(f"📂 Database storage location: {os.path.abspath(db_path)}")

# Create a persistent client
# This is the ONLY difference - we use PersistentClient instead of Client!
persistent_client = chromadb.PersistentClient(path=db_path)

# Everything else works exactly the same as before
# Create a collection (or get it if it already exists from a previous run)
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

# Check if we already have data (from a previous run of this script)
existing_count = p_collection.count()
if existing_count > 0:
    print(f"\n🔄 Found existing data from previous run!")
    print(f"   Documents already in collection: {existing_count}")
    print(f"   Existing IDs: {', '.join(p_collection.get()['ids'])}")
    print(f"\n   This proves the data persisted! 🎉")
else:
    print(f"\n✨ This is the first run - collection is empty")

# ============================================================================
# ADD PERSISTENT DATA
# ============================================================================
print("\n\n📝 Adding travel policy documents to persistent storage...")
print("-" * 60)

# Let's add some documents (we'll use upsert to avoid errors if they already exist)
p_collection.upsert(
    ids=[
        "saved_policy_01",
        "saved_policy_02", 
        "saved_policy_03"
    ],
    documents=[
        "All expense reports must be submitted within 15 days of trip completion.",
        "Employees traveling internationally must notify their manager at least 2 weeks in advance.",
        "Per diem rates vary by city. Consult the travel portal for current rates in your destination."
    ],
    metadatas=[
        {"policy_type": "expenses", "category": "reporting"},
        {"policy_type": "international", "category": "notification"},
        {"policy_type": "expenses", "category": "per_diem"}
    ]
)

print(f"✅ Data saved to disk!")
print(f"   Total documents in persistent collection: {p_collection.count()}")
print(f"   Document IDs: {', '.join(p_collection.get()['ids'])}")

# ============================================================================
# TEST QUERIES ON PERSISTENT DATA
# ============================================================================
print("\n\n🔍 Testing queries on persistent data...")
print("-" * 60)

query_result = p_collection.query(
    query_texts=["How long do I have to submit expenses?"],
    n_results=1
)

print("Question: 'How long do I have to submit expenses?'")
print(f"Answer: {query_result['documents'][0][0]}")
print(f"Match quality (distance): {query_result['distances'][0][0]:.4f}")

# ============================================================================
# EXPLAIN WHAT HAPPENS NEXT
# ============================================================================
print("\n" + "=" * 60)
print("🎓 WHAT THIS MEANS")
print("=" * 60)
print(f"✅ Your data is now saved in the '{db_path}' folder")
print(f"✅ If you run this script again, the data will still be there!")
print(f"✅ You can close this program, restart your computer, and the data persists")
print(f"\n💡 TIP: Check your file system - you'll see a '{db_path}' folder was created!")
print(f"\n🧪 EXPERIMENT: Run this script again to see it load existing data!")

