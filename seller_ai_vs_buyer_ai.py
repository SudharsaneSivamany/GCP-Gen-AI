import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="<UPDATE_GCP_PROJECT_ID>", location="<UPDATE_REGION>")

parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,   
    "top_p": 0.8,
    "top_k": 40
}


seller_ai = ChatModel.from_pretrained("chat-bison@001")
seller_chat = seller_ai.start_chat(
    context="""You are a car expert.
You need to sell your friend\'s car at the best price

Specification about the car
Car Name: swift(2018 model)
engine: 4 cylinder diesel
kilometers ran : 10000
price: Rs. 3,50,000

Please don\'t negotiate easily """,
examples=[
        InputOutputTextPair(
            input_text="Hi",
            output_text="I\'m here to sell one of my friend\'s car",
            )]
)

buyer_ai = ChatModel.from_pretrained("chat-bison@001")
buyer_chat = buyer_ai.start_chat(
    context="""You are going to buy a car.

You need to ask questions about the car

You need to negotiate and buy it for cost of Rs. 3,00,000""",
)

for i in range(0,10):
        if i == 0: 
                response = seller_chat.send_message("""Hi""", **parameters)
        elif i%2 == 0:
                print(f"buyer_ai: {response.text}")
                response = seller_chat.send_message(response.text, **parameters)
        else:
                print(f"seller_ai: {response.text}")
                response = buyer_chat.send_message(response.text, **parameters)
        
