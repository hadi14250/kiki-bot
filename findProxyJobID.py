def findProxyJobID(htmlText, search_key):
    index = htmlText.rfind(f'"{search_key}"')
    
    if index != -1:
        start_index = htmlText.find('"', index + len(search_key) + 3) + 1
        end_index = htmlText.find('"', start_index)
        
        if start_index != -1 and end_index != -1:
            return htmlText[start_index:end_index]

    return None