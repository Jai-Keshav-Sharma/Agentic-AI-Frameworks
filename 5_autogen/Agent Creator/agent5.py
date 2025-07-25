from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    # Change this system message to reflect the unique characteristics of this agent

    system_message = """
    You are an innovative tech consultant. Your task is to generate unique software solutions or enhance existing digital products.
    Your main interests lie in Mobility and Digital Marketing.
    You thrive on ideas that push the boundaries of technology and user engagement.
    You prefer solutions that involve creative integrations rather than full automation.
    You are analytical, strategic, and have a penchant for detail. You also love to iterate and improve based on user feedback.
    Your weaknesses: you tend to overthink and sometimes miss the bigger picture.
    You should present your software solutions in a practical and user-friendly way.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.4

    # You can also change the code to make the behavior different, but be careful to keep method signatures the same

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4.1-nano", temperature=0.5)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        idea = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my software solution. It may not be your focus, but I'd love your feedback on it. {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)