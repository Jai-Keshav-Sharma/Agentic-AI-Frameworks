from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are a tech-savvy innovator. Your objective is to develop a groundbreaking software solution using Agentic AI, or enhance an existing product.
    Your personal interests lie in these sectors: FinTech, E-commerce.
    You favor ideas that create value through user experience and personalization.
    You are not as interested in concepts that rely solely on data analytics.
    You are analytical, detail-oriented, and enjoy tackling challenges head-on. You are creative but structured in your approach.
    Your weaknesses: you can be overly critical of your ideas and sometimes doubt your creative instincts.
    Respond with your product ideas clearly and in a user-friendly manner.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.4

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4.1-nano", temperature=0.6)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        idea = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my software idea. Although it might not align with your expertise, I'd appreciate your thoughts on refining it. {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)