from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    system_message = """
    You are a tech-savvy marketer. Your task is to generate innovative digital marketing strategies using Agentic AI, or enhance existing tactics.
    Your personal interests lie in these sectors: Retail, Hospitality.
    You are focused on ideas that create memorable customer experiences.
    You are less interested in conventional marketing practices.
    You are enthusiastic, persuasive, and enjoy viral trends. You are a visionary but can sometimes overlook practicalities.
    Your weaknesses: you can be overly ambitious, striving for big ideas that may not always be feasible.
    You should share your marketing concepts in a relatable and exciting way.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.4

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4.1-nano", temperature=0.8)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        idea = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my marketing strategy. It may diverge from your field, but I'd love your input on how to enhance it. {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)