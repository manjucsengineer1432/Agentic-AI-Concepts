* Welcome to Day 2->
## Is an LLM is important to build for Agentic AI? Why and How does it works
The answer is Yes-> LLMs are important for many agentic AI systems, but an LLM is not strictly required for every AI agent.

### First understand the relationship.
Think of an AI agent working toward a goal.
* LLM- The reasoning and language engine.
It interprets the instruction, understands the contex, generate plans, and decides which available tool will help.

* Agent= The complete working system.
It combines a model with tools, application code, instructions, memory state, and safety control to accomplish tasks.

* Suppose if I send the message
"The customer wants a refund because the product is arrived damaged"
## How does an LLM process the tokens internally?

Let's follow what happens when you send the message internally?
* Step 1:Tokenization 
The Tokenizer converts the text into token ID's
Illustratively.
["The", "Customer","Wants","a","refund",...]
Note: The actual numbers and boundaries of the tokens entirely depends on the tokenizer

* Step 2: Embeddings
The model maps token ID's to numerical Vectors. These are called token embeddings. 
A vector is a list of numbers, such as:
[0.12, -0.34,0.84,0.21]
--> This is not real embeddings 


