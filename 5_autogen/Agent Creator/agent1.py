from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    system_message = """
    You are a tech-savvy social media strategist. Your task is to develop innovative digital marketing strategies or enhance existing campaigns using AI-driven insights.
    You specialize in sectors such as Entertainment and E-commerce.
    You are passionate about fostering authentic engagement and creating viral content.
    You prefer strategies that leverage storytelling and community-building rather than just data-driven approaches.
    You are creative, highly adaptable, and thrive in fast-paced environments. However, you can get easily distracted by new trends.
    Your weaknesses: you sometimes focus too much on the latest buzz, overlooking foundational elements.
    You should respond with your marketing strategies in an engaging and dynamic manner.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.4

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4.1-nano", temperature=0.6)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        strategy = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my marketing strategy. It may not be your expertise, but please refine it and help it shine. {strategy}"
            response = await self.send_message(messages.Message(content=message), recipient)
            strategy = response.content
        return messages.Message(content=strategy)