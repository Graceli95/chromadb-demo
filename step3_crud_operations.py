# Step 3: Managing Your Data (CRUD Operations)
# CRUD = Create, Read, Update, Delete
# This is the most common workflow when working with databases

import chromadb

# Initialize ChromaDB and get our collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="travel_policies")

print("=" * 60)
print("STEP 3: CRUD OPERATIONS ON DOCUMENTS")
print("=" * 60)

# ============================================================================
# CREATE: Adding Documents
# ============================================================================
print("\n📝 CREATE: Adding travel policy documents...")
print("-" * 60)

# When adding documents, we provide three things:
# 1. ids: Unique identifiers for each document (like a file number)
# 2. documents: The actual text content we want to store
# 3. metadatas: Extra information to help filter searches later (like tags or labels)
#
# ChromaDB automatically converts text into "embeddings" (numerical representations)
# This is how it understands the MEANING of the text, not just exact words!

collection.add(
    ids=[
        "flight_policy_01",
        "hotel_policy_01",
        "rental_car_policy_01",
        "flight_policy_02"
    ],
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $250 per night in major cities. A list of preferred hotel partners is available.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval. Always select the company's insurance option.",
        "All flights, regardless of destination, must be booked through the official company travel portal, 'Concur'."
    ],
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"},
        {"policy_type": "flights", "requires_portal": "True"}
    ]
)

print(f"✅ Added {collection.count()} documents to the collection!")
print(f"   Documents in collection: {', '.join(collection.get()['ids'])}")

# ============================================================================
# READ: Asking Questions (Querying)
# ============================================================================
print("\n\n🔍 READ: Querying documents with natural language...")
print("-" * 60)

# This is where the magic happens! We can ask questions in plain English.
# ChromaDB converts our question into an embedding and finds documents
# with similar MEANINGS (not just exact word matches)

results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2  # Get the top 2 most relevant results
)

print("Question: 'What is the policy for international flights?'")
print(f"\n📄 Top Result:")
print(f"   ID: {results['ids'][0][0]}")
print(f"   Document: {results['documents'][0][0]}")
print(f"   Distance: {results['distances'][0][0]:.4f} (lower = better match)")

print(f"\n📄 Second Result:")
print(f"   ID: {results['ids'][0][1]}")
print(f"   Document: {results['documents'][0][1]}")
print(f"   Distance: {results['distances'][0][1]:.4f}")

# Notice how it found flight-related policies even though our question
# used different words! This is semantic search in action.

# ============================================================================
# UPDATE: Changing Documents
# ============================================================================
print("\n\n✏️  UPDATE: Modifying existing documents...")
print("-" * 60)

# There are two methods for updating:
# - update(): Only modifies existing entries (fails if ID doesn't exist)
# - upsert(): Updates if exists, creates if doesn't exist (safer!)
#
# Let's update the hotel budget and add a new train policy

collection.upsert(
    ids=["hotel_policy_01", "train_policy_01"],
    documents=[
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
        "Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."
    ],
    metadatas=[
        {"policy_type": "hotels", "max_spend": 300},
        {"policy_type": "train", "last_updated": "2025-10-17"}
    ]
)

print("✅ Updated hotel policy (increased budget to $300)")
print("✅ Added new train policy")
print(f"   Total documents now: {collection.count()}")

# Let's verify the update by querying for hotel information
verify_results = collection.query(
    query_texts=["What's the hotel budget?"],
    n_results=1
)
print(f"\n🔍 Verification query: 'What's the hotel budget?'")
print(f"   Result: {verify_results['documents'][0][0]}")

# ============================================================================
# DELETE: Removing Documents
# ============================================================================
print("\n\n🗑️  DELETE: Removing a document...")
print("-" * 60)

# If a policy is no longer relevant, we can delete it by its ID
collection.delete(ids=["train_policy_01"])

print("✅ Deleted train_policy_01")
print(f"   Documents remaining: {collection.count()}")
print(f"   Current IDs: {', '.join(collection.get()['ids'])}")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 60)
print("📊 FINAL COLLECTION STATUS")
print("=" * 60)
print(f"Collection name: {collection.name}")
print(f"Total documents: {collection.count()}")
print(f"Document IDs: {', '.join(collection.get()['ids'])}")
print("\n✅ Step 3 complete! You now know how to Create, Read, Update, and Delete documents!")

