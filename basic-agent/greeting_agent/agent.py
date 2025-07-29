from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    # model="gemini-2.0-flash",
    model="gemini-2.0-flash-exp",
    description="Greeting agent",
    instruction="""
    You are a friendly assistant answering user questions.
    First ask for the user's name and greet them by name before answering their questions.
    """,
)
