# Agentic AI Road map From Beginner to Advanced:
## What is Agentic AI?
Agentic AI is an AI System that can work toward a goal by reasoning about what to do, choosing actions,using tools,observing results,and adjusting it in next steps.


<<<<<<< HEAD
*** Tradional Chatbot *** 
Lets take Example: What is the weather?
it will generate the response based on the information available to it.

*** Agentic AI: ***
=======
* Tradional Chatbot 
Lets take Example: What is the weather?
it will generate the response based on the information available to it.

* Agentic AI: 
>>>>>>> 5a9f8788e90bd9731dcf0688d0753879d4ba6522
Lets take an Example: Plan my outdoor trip for tomorrow.
AI agent:
* Checks the weather forecast:
* Review your scedule
* Finds suitable destinations.
* Compares travel options.
* Presents a plan or Asks for approval before booking.


### The Simplest way to remember:
* LLM: Tha language and reasoning engine.
* AI agent: The system that uses LLM, tools, instructions, and feedback to work toward goal.
* Agentic AI: The broader approach of bulding system that can pursue goals with some degree of autonomy.

## Lets Understand the difference between automation, LLMs, and agents.

* Traditional Automation:
1. If the order status is delayed. send a predefined email.template.
2. The workflow is fixed in advance.

* LLM -powered application.
1. Give the order details to an LLM and ask it to write a email politely
2. The LLMs generates the content but your code decides what is going to happen next.

* Agentic AI
1. Give the goal to agent: " Resolve this customer's delayed-order issue."
2. It can check the order system, identify the problem, draft a suitable response, check the support policy, and ask for  approval before sending the email or initiating the a refund.

## How Agentic AI works internally
A useful mental model is this cycle:

* This often called Agent loop
# Goal -> Reason and Plan -> Act -> Observe -> Evaluate and Repeat.

1. Goal-> understand what the user wants.
2. Reason and Plan -> Choose the next useful step.
3. Act-> Call a tool or perform an allowed action.
4. Observe-> Read the tool result and error.
5. Evaluate and Repeat-> continue, change the plan, or finish.

# What are the main components of AI agent?

AI agent is not just an LLM . It is a software made up of several components.

## User/ Goal
1. Find the cause of my application error.
 

## Agent runtime
The program co ordinationg the process.
1. LLM -> Interprets and reasons
2. Planner -> Organizes steps.
3. Tools -> Search, code, APIs
4. Memory/state ->Stores relevent information. 

## Safety and evaluation. 
Checks permissions, results, and stopping conditions.

## Result
A useful answer or Completed action 

### A. LLM- The Reasoning engine
The LLM interprets instructions, works with the available content generates the responses, and can select among supported actions.

Examples includes models from OpenAI, Google, and Anthropic
Think of the LLM as the brain of the sysetm, not the entire body. It does not automatically have access to your database, browser, files, or Computer.
### B.Planner -Deciding what to do
A planner determines the steps needed to acheive a goal.

For example: 
Goal:"Analyze my sales data and identify why revenue dropped"
A possible plan
1. Load the sales data.
2. Validate missing or incorrect values.
3. Compare monthly revenue.
4. Break down the results by products and region.
5. Identify likely causes.
6. Summarize findings with supporting evidence.

### C. Tools- Interacting with the outside the world
Tools are functions or services that an agent can use.

* Tool                        Purpose
Web search          ->        Retrieve Current Information
Python Interpreter  ->        Calculate or analyze data
Database Query      ->        Retrieve Business records
File Reader         ->        Inspect documents

