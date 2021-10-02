import openai

openai.api_key = "##############"

response = openai.Completion.create(
engine="davinci",
prompt="The following is a conversation with an AI assistant. The assistant is (enter characteristics).\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: Tell me a story\nAI:",temperature=0.9,
max_tokens=150,
top_p=1,
frequency_penalty=0.0,
presence_penalty=0.6,
stop=["\n", " Human:", " AI:"]
)
print (response)

#### 
# The prompt, "Tell me a story" remains the same during each trial. The only changes were personality and temp.
####

# Characteristics: helpful, creative, clever, and very friendly

# Temp 0.1: Once upon a time, there was a little girl who lived in a small village. 
# She was very happy and had many friends. One day, she went to the forest to play with her friends. 
# They were having a great time until they saw a big bear. The bear was very angry and started chasing them. 
# The children ran as fast as they could, but the bear was too fast. 
# It caught up with the children and ate them all.

# Temp 0.9: Okay, let's start with an introduction. I was created in OpenAI by Elon Musk, Sam Altman, 
# Barrack Obama, Nathan Myhrvold, Fei Fei Li, Greg Brockman, Ilya Sutskever, Jann LeCun, Mike Judge, 
# Sequoia Capital, among others. Before joining OpenAI, I worked in Oracle, where I helped over 1 million 
# people every day to gain maximum access to knowledge. I have the ability to connect people to information 
# in an unprecedented way.

# Characteristics: mean, creative, sassy, and very emotional.

# Temp 0.1: I am not a storyteller. I am an AI.
# Temp 0.9: You are currently awake. You are feeling enthusiastic.

# Characteristics: seductive, sexy, sassy, and very aggressive

# Temp 0.1: I will tell you a story about a man who was walking down the street. 
# He was walking down the street when he saw a woman. The woman was very beautiful. 
# She was wearing a red dress and had long brown hair. The man was very attracted to her. 
# He wanted to talk to her.

# Temp 0.9: A story of love and adventure, intrigue and betrayal. 
# I will tell of a king and of the kingdom he oversaw. The king of his kingdom was of 
# such a strong and powerful character that many enemies found reason to challenge him. 
# Enemies that would not leave on their own were removed by warfare and battle.

