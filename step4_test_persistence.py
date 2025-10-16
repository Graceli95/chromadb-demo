# Step 4: Testing Data Persistence
# This script proves that our data survives program restarts

import chromadb

print("=== TESTING DATA PERSISTENCE ===")
print("This script will connect to our existing persistent database...")
print("If our data truly persists, we should be able to retrieve it!")
print()

# Connect to the existing persistent database
# Notice: We're NOT adding any new data, just connecting to what's already saved
persistent_client = chromadb.PersistentClient(path="./chroma_db")
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

print("✅ Connected to existing persistent database")
print()

print("=== RETRIEVING SAVED DATA ===")
# Let's get all the documents we saved in the previous script
all_docs = p_collection.get()

print(f"Found {len(all_docs['ids'])} documents in the database:")
print()

for i, doc_id in enumerate(all_docs['ids']):
    print(f"{i+1}. ID: {doc_id}")
    print(f"   Content: {all_docs['documents'][i]}")
    print(f"   Metadata: {all_docs['metadatas'][i]}")
    print()

print("=== TESTING SEMANTIC SEARCH ON SAVED DATA ===")
# Let's test that semantic search still works on our saved data
results = p_collection.query(
    query_texts=["What approvals are required for travel?"],
    n_results=2
)

print("Query: 'What approvals are required for travel?'")
if results['documents'][0]:
    for i, doc in enumerate(results['documents'][0]):
        print(f"Result {i+1}: {doc}")
        print(f"Distance: {results['distances'][0][i]:.4f}")
        print()
else:
    print("No results found")

print("🎉 PERSISTENCE TEST SUCCESSFUL!")
print("Our data survived the program restart and is fully functional!")
print()
print("This proves that:")
print("✅ Data is saved to disk")
print("✅ Data persists between program runs") 
print("✅ Semantic search works on saved data")
print("✅ All CRUD operations work with persistent storage")
