# LinkedInJSONParser

A quick and VERY dirty Python based parser for LinkedIn output.

This parser is designed to work with the JSON responses resulting from a search on LinkedIn. For example, when you're looking at a company's LinkedIn page and you click "Show all employees", the resulting list is provided as a JSON response from the LinkedIn API. Using Burp Suite Pro's Intruder tool, you can issue repeated requests to get responses containing all of the employees.

When you're done harvesting using Burp, export the server responses into text files. DO NOT concatenate the results into a single file. The output includes the response header which gets in the way of the parser and needs to be removed. The included 'file_splitter.py' script will remove the header and save the pure JSON object in a file with the name '[original_filename]_clean.json'. 'LinkedInJSONParser.py' will read the clean file and output the names, titles, and location information for each employee returned by the API. The script also auto-removes andy "LinkedIn Member" entries and entries that have no name listed.

This was hammered out very quickly one morning during a social engineering engagement after finding out that none of the other parsers worked anymore and the manual methods previously provided didn't fit with the new API either. There is MUCH that can be done to improve it. There is likely a much better way to do some of the things this script is doing, but this works. Edits, fixes, improvements, they're all welcome.

HOW TO USE
--------------
1. Export your responses from Burp WITHOUT CONCATENATING so there's one file per response.
2. Use the file_splitter.py to clean the headers out of the output files:
  
    file_splitter.py --file=[filename]
    
    EXAMPLE: for f in $(ls ~/linkedinoutputfiles/*); do python file_splitter.py --file=$f; done

3. Use LinkedInJSONParser.py to parse and output the names, titles, and locations from the clean response file:

    LinkedInJSONParser.py --file=[filename]
    
    EXAMPLE: for f in $(ls ~/linkedinoutputfiles/*.json); do python LinkedInJSONParser.py --file=$f; done >> names_list.txt
  
Enjoy!

-PapaHack
