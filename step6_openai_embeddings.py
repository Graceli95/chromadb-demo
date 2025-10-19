# Step 6: Advanced - Using OpenAI's Embedding Model
# Learn how to integrate more powerful embedding models from OpenAI

import chromadb
from chromadb.utils import embedding_functions
import os

print("=" * 60)
print("STEP 6: USING OPENAI'S EMBEDDING MODEL")
print("=" * 60)

# ============================================================================
# SETUP: Check for OpenAI API Key
# ============================================================================
print("\n🔑 Checking for OpenAI API Key...")
print("-" * 60)

# OpenAI requires an API key for authentication
# Best practice: Store it as an environment variable (keeps it secure)
# You can get an API key from: https://platform.openai.com/api-keys

api_key = os.environ.get('OPENAI_API_KEY')

if not api_key:
    print("⚠️  WARNING: OPENAI_API_KEY environment variable not found!")
    print("\n📚 This is a demonstration script showing you HOW to use OpenAI embeddings.")
    print("   To actually run it, you would need to:")
    print("   1. Get an API key from https://platform.openai.com/api-keys")
    print("   2. Set it as an environment variable:")
    print("      export OPENAI_API_KEY='your-key-here'")
    print("\n💡 For now, we'll show you the code structure even without a key.")
    print("=" * 60)
else:
    print("✅ OpenAI API key found!")
    print(f"   Key preview: {api_key[:8]}...{api_key[-4:]}")

# ============================================================================
# UNDERSTANDING TOKENS (Important for costs!)
# ============================================================================
print("\n\n📊 Understanding Tokens...")
print("-" * 60)

# Before using OpenAI's API, it's important to understand tokens
# Tokens are pieces of words that the model "sees" and are used for billing
# Example: "Hello world" might be 2 tokens, "Embedding" might be 1-2 tokens

print("What are tokens?")
print("   - Tokens are chunks of text that models process")
print("   - Roughly: 1 token ≈ 4 characters or 0.75 words")
print("   - OpenAI charges based on the number of tokens processed")
print("   - The 'text-embedding-3-small' model uses ~$0.00002 per 1K tokens")

# To count tokens accurately, we can use tiktoken (OpenAI's tokenizer)
try:
    import tiktoken
    
    print("\n✅ tiktoken library found - let's count some tokens!")
    
    # Get the encoding for OpenAI's embedding model
    # Most OpenAI models use the 'cl100k_base' encoding
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # Example texts
    sample_texts = [
        "This is a sample sentence.",
        "For domestic flights, employees must book economy class tickets.",
        "Employees can book hotels up to a maximum of $300 per night."
    ]
    
    print("\n📝 Token count examples:")
    for text in sample_texts:
        token_count = len(encoding.encode(text))
        print(f"   '{text}'")
        print(f"   → {token_count} tokens\n")
    
except ImportError:
    print("\n⚠️  tiktoken not installed (optional - only needed for token counting)")
    print("   Install with: pip install tiktoken")

# ============================================================================
# CREATE COLLECTION WITH OPENAI EMBEDDING FUNCTION
# ============================================================================
print("\n\n🚀 Creating a Collection with OpenAI Embeddings...")
print("-" * 60)

# Initialize ChromaDB
client = chromadb.Client()

print("\n📋 Comparison of embedding functions:")
print("   Default (all-MiniLM-L6-v2):")
print("      • Free and runs locally")
print("      • Good for most use cases")
print("      • ~384 dimensions")
print("\n   OpenAI (text-embedding-3-small):")
print("      • Costs money (pay per use)")
print("      • Better semantic understanding")
print("      • ~1536 dimensions")
print("      • Requires internet connection")

# Only create the OpenAI collection if we have an API key
if api_key:
    print("\n✅ Creating collection with OpenAI embedding function...")
    
    # Create an OpenAI embedding function
    # This tells ChromaDB to use OpenAI's model instead of the default
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        model_name="text-embedding-3-small",
        api_key=api_key
    )
    
    # Create a collection that uses the OpenAI embedding function
    openai_collection = client.get_or_create_collection(
        name="travel_policies_openai",
        embedding_function=openai_ef
    )
    
    print("✅ Collection created with OpenAI embeddings!")
    
    # ========================================================================
    # ADD DATA (works exactly the same as before!)
    # ========================================================================
    print("\n📝 Adding documents to OpenAI-powered collection...")
    print("-" * 60)
    
    # From here, adding and querying works EXACTLY the same as before
    # The only difference is what happens behind the scenes (better embeddings)
    
    openai_collection.add(
        ids=["flight_policy_01", "hotel_policy_01", "rental_car_policy_01"],
        documents=[
            "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
            "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
            "A mid-size sedan is the standard for car rentals. Upgrades require manager approval."
        ],
        metadatas=[
            {"policy_type": "flights"},
            {"policy_type": "hotels"},
            {"policy_type": "rental_cars"}
        ]
    )
    
    print(f"✅ Added {openai_collection.count()} documents")
    
    # ========================================================================
    # QUERY WITH OPENAI EMBEDDINGS
    # ========================================================================
    print("\n🔍 Querying with OpenAI embeddings...")
    print("-" * 60)
    
    results = openai_collection.query(
        query_texts=["What is the hotel budget?"],
        n_results=1
    )
    
    print("Question: 'What is the hotel budget?'")
    print(f"Answer: {results['documents'][0][0]}")
    print(f"Match quality (distance): {results['distances'][0][0]:.4f}")
    
    print("\n✅ Query successful! OpenAI embeddings are working!")

else:
    print("\n⚠️  Skipping OpenAI collection creation (no API key)")
    print("   Here's what the code would look like:\n")
    print("   ```python")
    print("   from chromadb.utils import embedding_functions")
    print("")
    print("   # Create OpenAI embedding function")
    print("   openai_ef = embedding_functions.OpenAIEmbeddingFunction(")
    print("       model_name='text-embedding-3-small',")
    print("       api_key=os.environ['OPENAI_API_KEY']")
    print("   )")
    print("")
    print("   # Create collection with custom embedding function")
    print("   collection = client.get_or_create_collection(")
    print("       name='my_collection',")
    print("       embedding_function=openai_ef")
    print("   )")
    print("")
    print("   # Everything else works the same!")
    print("   collection.add(ids=[...], documents=[...])")
    print("   results = collection.query(query_texts=[...])")
    print("   ```")

# ============================================================================
# COMPARISON: Default vs OpenAI (if we have API key)
# ============================================================================
if api_key:
    print("\n\n" + "=" * 60)
    print("📊 COMPARISON: Default vs OpenAI Embeddings")
    print("=" * 60)
    
    # Create a default collection for comparison
    default_collection = client.get_or_create_collection(name="travel_policies_default")
    
    default_collection.add(
        ids=["flight_policy_01", "hotel_policy_01"],
        documents=[
            "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
            "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners."
        ]
    )
    
    query = "What's the nightly accommodation limit?"
    
    print(f"\nQuery: '{query}'")
    print("\nDefault embeddings result:")
    default_results = default_collection.query(query_texts=[query], n_results=1)
    print(f"   Answer: {default_results['documents'][0][0][:80]}...")
    print(f"   Distance: {default_results['distances'][0][0]:.4f}")
    
    print("\nOpenAI embeddings result:")
    openai_results = openai_collection.query(query_texts=[query], n_results=1)
    print(f"   Answer: {openai_results['documents'][0][0][:80]}...")
    print(f"   Distance: {openai_results['distances'][0][0]:.4f}")
    
    print("\n💡 Both should find the hotel policy!")
    print("   OpenAI often provides better semantic matching for complex queries.")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n\n" + "=" * 60)
print("🎓 KEY TAKEAWAYS")
print("=" * 60)

print("\n✅ When to use DEFAULT embeddings (all-MiniLM-L6-v2):")
print("   • Free and runs locally")
print("   • Fast and efficient")
print("   • Good for most applications")
print("   • Perfect for learning and prototyping")

print("\n✅ When to use OPENAI embeddings:")
print("   • Need highest quality semantic understanding")
print("   • Working with complex or nuanced text")
print("   • Have budget for API costs")
print("   • Okay with data being sent to OpenAI")

print("\n💡 IMPORTANT: Both use the exact same API!")
print("   The only difference is passing embedding_function when creating the collection.")

print("\n✅ Step 6 complete! You've learned about advanced embedding models!")
print("\n🎉 CONGRATULATIONS! You've completed all 6 steps of the ChromaDB guide!")

