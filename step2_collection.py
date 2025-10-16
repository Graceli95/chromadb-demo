# Step 2: Creating Your First Collection
# A collection is like a single drawer in your filing cabinet for a specific topic

import chromadb

# Initialize the ChromaDB client. This creates an in-memory database.
# Think of this as opening the filing cabinet - but it's only in memory (RAM)
# This means data will be lost when the program ends (we'll fix this in Step 4)
client = chromadb.Client()

# Create a new collection or get it if it already exists.
# A collection is like a labeled drawer in our filing cabinet
# We're creating a drawer specifically for "travel_policies"
collection = client.get_or_create_collection(name="travel_policies")

print("✅ Collection 'travel_policies' created successfully!")
print(f"Collection name: {collection.name}")

# Let's verify our collection exists by listing all collections
all_collections = client.list_collections()
print(f"Total collections: {len(all_collections)}")
for coll in all_collections:
    print(f"  - {coll.name}")
