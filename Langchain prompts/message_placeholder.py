from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#create template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful assistant'),
    MessagesPlaceholder(variable_name='chat_history'), #used to retrieve and store the chat history
    ('human', '{query}')
])

#load chat history
chat_history = []

with open('Langchain prompts\\chat_history.txt') as f:
    chat_history.extend(f.readlines())

#create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':"Where is my refund"})

print(prompt)
