from openai import OpenAI

#Poem analyzer that starts a chat completions; system and user instructions are prefabricated
def analyze_poem(sample, poem, model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": "Assistant provides detailed analyses of poems. Assistant is familiar with these poetic terms: simile, metaphor, metonymy, imagery, synecdoche, meter, diction, end rhyme, internal rhyme, and slant rhyme."},
                {"role": "user", "content": f"Base analysis and output on these samples. The sample poems are delimited by the xml tags <poem> and </poem>. The sample analyses follow their respective sample poems and are delimited by xml tags <analysis> and </analysis>. /n/nSample: {sample}./n/nPlease analyze this poem delimited by <poem> and </poem> XML tags:\n\n{poem}"}]
    
    client = OpenAI(
        # Initialize api_key = "INSERT_YOUR_API_KEY_AS_STRING" 
        # or use .env file with Python-dotenv module
        # or edit bash_profile—see OpenAI API quickstart instructions
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2
    )
    #Print the message produced by the ChatGPT model
    ai_response = response.choices[0].message.content
    return ai_response

# Get samples
with open("PoemAnalysisSamples.txt", 'r') as f:
    sample_poems = f.read()

# Get a new poem to analyze
with open("DesertPlaces.txt", 'r') as f: # Replace with path to your new poem file
    new_poem = f.read() 


#Get and print ChatGPT response
analysis = analyze_poem(sample_poems, new_poem)
print(analysis)
