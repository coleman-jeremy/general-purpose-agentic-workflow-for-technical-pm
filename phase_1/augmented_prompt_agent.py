# TODO: 1 - Import the AugmentedPromptAgent class
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import AugmentedPromptAgent

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
my_prof = AugmentedPromptAgent(openai_api_key, persona)
# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = my_prof.respond(prompt)
# Print the agent's response
print(f"Prompt: {prompt}")
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
print("What knowledge the agent likely used to answer the prompt.")
print("The agent used the knowledge from the ChatGPT 3.5 turbo model.")
print("How the system prompt specifying the persona affected the agent's response.")
print("It made the agent start all replies with 'Dear students,' and use the tone a professor would use when speaking to their students.")