from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

#Load API key from .env file
#For securely storing your API key, see: https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key
load_dotenv(find_dotenv())
api_key = os.environ["OPENAI_API_KEY"]

# Poem analyzer that starts a chat completions; system and user instructions are prefabricated
def analyze_poem(sample, poem, model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": "Assistant provides detailed analyses of poems. Assistant is familiar with these poetic terms: simile, metaphor, metonymy, imagery, synecdoche, meter, diction, end rhyme, internal rhyme, and slant rhyme."},
                {"role": "user", "content": f"Base analysis and output on these samples. The sample poems are delimited by the xml tags <poem> and </poem>. The sample analyses follow their respective sample poems and are delimited by xml tags <analysis> and </analysis>. /n/nSample: {sample}./n/nPlease analyze this poem delimited by <poem> and </poem> XML tags:\n\n{poem}"}]
    
    client = OpenAI(
        api_key=api_key
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2
    )

    #Return the response message produced by the ChatGPT model
    
    return response.choices[0].message.content



#Get a new poem to analyze
def format_target(file_path):
    with open(file_path, 'r') as f:
        sample = f.readlines()
    with open("TargetText.txt", 'w') as f:
        f.write("<poem>\n")
        for i, line in enumerate(sample, start=1):
            f.write(f"{i} {line}")
        f.write("\n</poem>")


#Get and print ChatGPT response
def main():
    #Get samples
    with open("samples/PoemAnalysisSamples.txt", 'r') as f:
        sample_poems = f.read()
    
    #Get new poem to analyze
    file_path = "samples/DesertPlaces.txt" # Change this to the path of the poem you want to analyze
    format_target(file_path)
    with open("TargetText.txt", 'r') as f:
        target_text = f.read()

    #Get and print ChatGPT response
    analysis = analyze_poem(sample_poems, target_text)
    print(analysis)
    
if __name__ == "__main__":
    main()
