
import sys
import os
import importlib.metadata


print("=== Python Environment ===")
print("Python:", sys.version.split()[0])
print("Meets requirement:", sys.version_info >= (3, 10))

print("\n=== Required Packages ===")

packages = [
"openai",
"pinecone",
"tiktoken",
"tenacity",
"fastapi"
]

for package in packages:
  try:
    version = importlib.metadata.version(package)
    print(f"[OK] {package}: {version}")
  except importlib.metadata.PackageNotFoundError:
    print(f"[MISSING] {package}") 

  print("\n=== API Keys ===")

for key in ["OPENAI_API_KEY", "PINECONE_API_KEY"]:
  if os.getenv(key):
    print(f"[OK] {key}")
  else:
    print(f"[MISSING] {key}")