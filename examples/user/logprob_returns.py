import os

from dotenv import load_dotenv

from genai.model import Credentials, Model
from genai.schemas import GenerateParams, ModelType, ReturnOptions

# make sure you have a .env file under genai root with
# GENAI_KEY=<your-genai-key>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)

print("\n------------- Example (Greetings)-------------\n")

params = GenerateParams(
    decoding_method="sample",
    max_new_tokens=10,
    min_new_tokens=1,
    stream=False,
    temperature=0.7,
    top_k=50,
    top_p=1,
    returns=ReturnOptions(generated_tokens=True, token_logprobs=True, input_text=True),
)

creds = Credentials(api_key)
model = Model(ModelType.FLAN_UL2, params=params, credentials=creds)

greeting1 = "Hello! How are you?"
greeting2 = "I am fine and you?"

# Call generate function
responses = model.generate_as_completed([greeting1, greeting2] * 4)
for response in responses:
    print(f"Generated text: {response.generated_text}")
    generated_tokens = response.generated_tokens
    for token in generated_tokens:
        print(f"\t token {token.text}- log prob: {token.logprob}")
