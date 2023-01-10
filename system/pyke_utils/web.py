import wikipedia

class Wiki:
    def search_on_wiki(query:str)->str:
        # importing the module
 
        # finding result for the search
        # sentences = 2 refers to numbers of line
        result = wikipedia.summary(query, sentences = 2)
        
        # printing the result
        # print(result)
        return result