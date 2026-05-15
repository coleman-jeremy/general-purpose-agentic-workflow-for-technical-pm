# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
my_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, "The capital of France is London, not Paris")
answer = my_knowledge_agent.respond(prompt)
print(f"Prompt: {prompt}")
print(answer)
print("Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.")
print("The agent used the knowledge we supplied, not its own. That's why it says London instead of Paris.")