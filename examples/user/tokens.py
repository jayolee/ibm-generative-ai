import os

from dotenv import load_dotenv

from genai.model import Credentials, Model
from genai.schemas import GenerateParams, ModelType

# make sure you have a .env file under genai root with
# GENAI_KEY=<your-genai-key>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)

print("\n------------- Example (Greetings Tokens)-------------\n")

params = GenerateParams(
    decoding_method="sample",
    max_new_tokens=10,
    min_new_tokens=1,
    stream=False,
    temperature=0.7,
    top_k=50,
    top_p=1,
)

creds = Credentials(api_key)
model = Model(ModelType.FLAN_UL2, params=params, credentials=creds)

greeting1 = "Hello! How are you?"
greeting2 = "I am fine and you?"

# just get the token counts
responses = model.tokenize_as_completed([greeting1, greeting2])
for response in responses:
    print(f"Generated text: {response}")

# get the token counts and tokens
responses = model.tokenize_as_completed([greeting1, greeting2], return_tokens=True)
for response in responses:
    print(f"Generated text: {response}")
