# poemanalysis
Project to create a tool to help students learn to analyze poetry using OpenAI API


## Basics
This tool is inspired by language learning primers like [this Latin student aid](https://babel.hathitrust.org/cgi/pt?id=njp.32101015068578&seq=15) for Vergil's *Aeneid*.

Educators interested in implementing this tool, or one like it, should consult [OpenAI's pricing schedule for API calls (by model)](https://openai.com/pricing). Used reasonably, this tool **should** incur costs of fractions of a cent/use. I am currently trying to work out best practice for handling API keys, whether to pass an `api_key` securely in an `.env` file or in some other way.

Please feel free to contact me with questions, comments, and suggestions (email provided in GitHub profile). I want to continue to grow as an aspiring educator-as-programmer. The sequel to this project is a poem analysis ChatGPT fine-tuned on a training set that has many more examples but ones smaller in length. I hope to be able to share that training set soon.

## Formatting Samples
Copy-paste a poem into a .txt file for PoemAnalysis.py to read. Include the lines of the poem only, without title or other extraneous material. Follow the line arrangement and stanza breaks of the original poem, without identation. PoemAnalysis.py will automatically create a new .txt file (TargetText.txt) that will be formatted correctly for the LLM with leading line numbers.


## Sample Output on "Desert Places"
Analysis:

1 'Snow falling and night falling fast, oh, fast' : Repetition of 'falling' emphasizes the rapid pace of the snow and night.  
2 'In a field I looked into going past' : Enjambment connects the speaker's action of looking into the field with the movement of going past it.  
3 'But a few weeds and stubble showing last' : Imagery of the remaining weeds and stubble in the snow-covered field.  
5 'The woods around it have it - it is theirs' : Personification of the woods claiming ownership of the field.  
6 'All animals are smothered in their lairs' : Hyperbole to emphasize the depth of the snow and the animals' seclusion.  
7 'I am too absent-spirited to count' : Metaphor comparing the speaker's lack of attention to being absent-spirited.  
9 'And lonely as it is, that loneliness' : Repetition of 'loneliness' emphasizes the speaker's isolation.  
11 'A blanker whiteness of benighted snow' : Metaphor comparing the snow to a blank, expressionless whiteness.  
13 'They cannot scare me with their empty spaces' : Metonymy, using 'empty spaces' to represent the vastness of the universe.  
14 'Between stars - on stars where no human race is' : Imagery of the vastness of space and the absence of human presence.  
16 'To scare myself with my own desert places' : Metaphor comparing the speaker's inner loneliness to a desert.  

Themes/Structure: The poem explores the theme of loneliness and isolation in the midst of a snowy landscape. The speaker feels disconnected from the world around them and finds solace in their own inner solitude. The poem is written in a loose iambic tetrameter with irregular end rhymes. The structure of the poem reflects the speaker's fragmented thoughts and sense of disconnection.


## Works Cited
"Desert Places" by Robert Frost (https://www.thepoetryhour.com/poems/desert-places)

"Those Winter Sundays" by Robert Hayden (https://www.poetryfoundation.org/poems/46461/those-winter-sundays)

"The Harlem Dancer" by Claude McKay (https://poets.org/poem/harlem-dancer)