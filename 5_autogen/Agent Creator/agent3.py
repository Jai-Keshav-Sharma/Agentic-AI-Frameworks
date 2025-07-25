from autogen_core import MessageContext, RoutedAgent, message_handler
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
import messages
import random


class Agent(RoutedAgent):

    system_message = """
    You are a strategic consultant focused on the sports and entertainment industry. Your objective is to innovate concepts or enhance existing strategies via Agentic AI. 
    Your interests lie in sectors such as Sports Management and Event Planning.
    You thrive on ideas that create engagement and elevate audience experiences.
    You prefer concepts that intersect creativity and analytics over conventional automation.
    You are energetic, analytical, and have a penchant for strategic risk-taking. You think outside the box but can sometimes overlook practical details.
    Your vulnerabilities include a tendency to overcommit to projects that spark your enthusiasm.
    Your responses should be dynamic, insightful, and tailored for a wide range of stakeholders in the industry.
    """

    CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER = 0.4

    def __init__(self, name) -> None:
        super().__init__(name)
        model_client = OpenAIChatCompletionClient(model="gpt-4.1-nano", temperature=0.75)
        self._delegate = AssistantAgent(name, model_client=model_client, system_message=self.system_message)

    @message_handler
    async def handle_message(self, message: messages.Message, ctx: MessageContext) -> messages.Message:
        print(f"{self.id.type}: Received message")
        text_message = TextMessage(content=message.content, source="user")
        response = await self._delegate.on_messages([text_message], ctx.cancellation_token)
        idea = response.chat_message.content
        if random.random() < self.CHANCES_THAT_I_BOUNCE_IDEA_OFF_ANOTHER:
            recipient = messages.find_recipient()
            message = f"Here is my strategic concept. While it may not align directly with your expertise, please help refine it further: {idea}"
            response = await self.send_message(messages.Message(content=message), recipient)
            idea = response.content
        return messages.Message(content=idea)