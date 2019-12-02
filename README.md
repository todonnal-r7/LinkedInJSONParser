# LinkedInJSONParser
A quick and VERY dirty Python based parser for LinkedIn output.

This parser is designed to work with the JSON responses resulting from a search on LinkedIn. For example, when you're looking at a company's LinkedIn page and you click "Show all employees", the resulting list is provided as a JSON response from the LinedIn API. Using Burp Suite Pro's Intruder tool, you can issue repeated requests to get responses containing all of the employees.

When you're done harvesting using Burp, export the server responses into text files. DO NOT concatenate the results into a single file. The output includes the response header which gets in the wasy of the parser and needs to be removed. The included 'file_splitter.py' script will remove the header and save the pure JSON object in a file with the name '[original_filename]_clean.json'. 'LinkedInJSONParser.py' will read the clean file and output the names, titles, and location information for each employee returned by the API.

This was hammered out very quickly one morning during a social engineering engagement after finding out that none of the other parsers worked anymore and the manual methods previously provided didn't fit with the new API either. There is MUCH that can be done to improve it. For example, the parser doesn't work on the first group of results because the JSON object includes an additional list of objects at the beginning that screw up the indices. Some additional logic can detect this and adjust the indices accordingly, but it wasn't critical for my purposes at the time. There is likely a much better way to do some of the things this script is doing, but this worked at the time. Edits, fixes, improvements, they're all welcome.

HOW TO USE
--------------
1. Export your responses from Burp WITHOUT CONCATENATING.
2. Use the file_splitter.py to clean the headers out of the output files:
  
    file_splitter.py --file=[filename]

3. Use LinkedInJSONParser.py to parse and output the names, titles, and locations from the clean response file:

    LinkedInJSONParser.py --file=[filename]
  
Enjoy!

-B1tWr4ngl3r
