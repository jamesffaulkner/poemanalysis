from openai import OpenAI

#File reader function to extract .txt files
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."

#Poem analyzer that starts a chat completions; system and user instructions are prefabricated
def analyze_poem_chat(sample, poem, model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": "Assistant provides detailed analyses of poems. Assistant is familiar with these poetic terms: simile, metaphor, metonymy, imagery, synecdoche, meter, diction, end rhyme, internal rhyme, and slant rhyme."},
                {"role": "user", "content": f"Base analysis and output on these samples. The sample poems are delimited by the xml tags <poem> and </poem>. The sample analyses follow their respective sample poems and are delimited by xml tags <analysis> and </analysis>. /n/nSample: {sample}./n/nPlease analyze this poem delimited by <poem> and </poem> XML tags:\n\n{poem}"}]
    
    MyAI = OpenAI(
        #Initialize api_key = "INSERT YOUR API KEY AS A STRING" 
        #or follow other OpenAI API methods detailed in online docs
        #(e.g., editing your bash_profile) 
    )
    response = MyAI.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.2
    )
    #Print the message produced by the ChatGPT model
    ai_response = response.choices[0].message.content
    return ai_response



# Get samples

file_path = "PoemAnalysisSamples.txt"  # Replace with the path to your file
sample_poems = read_file(file_path)

# Analyzing a new poem (replace with the poem you want to analyze)
second_file_path = "DesertPlaces.txt"
new_poem = read_file(second_file_path)
analysis = analyze_poem_chat(sample_poems, new_poem)

print(analysis)
