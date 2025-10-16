# Step 4: Saving Your Work (Persistent Database)
# This solves the problem of data disappearing when the program ends

import chromadb
import os

print("=== PROBLEM: In-Memory Database ===")
print("So far, we've been using chromadb.Client() which creates an in-memory database.")
print("This is like writing on a whiteboard - data disappears when the program ends!")
print()

# Let's demonstrate the problem first
print("Creating a temporary in-memory database...")
temp_client = chromadb.Client()
temp_collection = temp_client.get_or_create_collection(name="temporary_data")

temp_collection.add(
    ids=["temp_doc_01"],
    documents=["This data will disappear when the program ends!"]
)

print("✅ Added document to temporary database")
print("❌ But this data will be lost when the program ends!")
print()

print("=== SOLUTION: Persistent Database ===")
print("Now let's create a database that saves to disk...")

# SOLUTION: Use PersistentClient instead of Client
# This creates a database that saves to your computer's hard drive
persistent_client = chromadb.PersistentClient(path="./chroma_db")

print("✅ Created persistent client pointing to './chroma_db' directory")
print("   (If the directory doesn't exist, ChromaDB will create it automatically)")

# Create a collection in our persistent database
# This collection will be saved to disk and persist between program runs
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

print("✅ Created collection 'saved_policies' in persistent database")
print()

print("=== ADDING DATA TO PERSISTENT DATABASE ===")
# Add some data that will actually be saved
p_collection.add(
    ids=["expense_policy_01", "booking_policy_01"],
    documents=[
        "All expense reports must be submitted within 15 days of trip completion.",
        "All travel bookings must be approved by your direct manager before making reservations."
    ],
    metadatas=[
        {"policy_type": "expenses", "deadline_days": 15},
        {"policy_type": "approvals", "requires_manager": True}
    ]
)

print("✅ Added 2 documents to persistent database:")
print("   - expense_policy_01: Expense report deadline policy")
print("   - booking_policy_01: Manager approval requirement")

# Let's verify our data was saved
print("\n=== VERIFYING PERSISTENT STORAGE ===")
results = p_collection.query(
    query_texts=["What are the expense report requirements?"],
    n_results=1
)

print("Query: 'What are the expense report requirements?'")
print(f"Result: {results['documents'][0][0]}")
print()

print("=== CHECKING DISK STORAGE ===")
# Let's see if ChromaDB created the directory and files
if os.path.exists("./chroma_db"):
    print("✅ ChromaDB directory created successfully!")
    print("Contents of ./chroma_db:")
    
    # List what's in the chroma_db directory
    for item in os.listdir("./chroma_db"):
        item_path = os.path.join("./chroma_db", item)
        if os.path.isdir(item_path):
            print(f"  📁 {item}/ (directory)")
            # List contents of subdirectories
            for subitem in os.listdir(item_path):
                print(f"    - {subitem}")
        else:
            print(f"  📄 {item}")
else:
    print("❌ ChromaDB directory not found")

print("\n🎉 Persistent Database Setup Complete!")
print("Your data is now safely stored on disk and will survive program restarts!")
print()
print("Key Differences:")
print("• chromadb.Client() = Temporary (in-memory)")
print("• chromadb.PersistentClient() = Permanent (saved to disk)")
print("• Everything else works exactly the same!")
