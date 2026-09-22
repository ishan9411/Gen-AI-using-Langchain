from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

#chat history as list -> we dont have info what we have sent and what AI has sent
#we can use dict -> {user: "....", AI: "....."}
#langchain has solution for this as built in libraries -> messages
chat_history = [
    SystemMessage(content="You are a chatbot assisstant")
]

while True:
    user_input = input("You: ")
    if(user_input == 'exit'):
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

