# ChatQuotient-Bot - disdaccbot
ChatQuotient-Bot is a simple Discord chat bot.
## Commands
1. **Hello**: Chat bot responds to Hello command with the follwing response: Hello, {username}!
2. **?**: Chat bot responds privately to the user when typing question mark. 
3. **!**: There are several commands triggered with the exclamation mark, as listed below:
    - **!quote**: Returns a randomn quote fetched from an API.
    - **!challenge**: Returns a randomn coding challenge returned from a locally saved JSON object.
    - **!add url**: Adds a new coding challenge to the locally saved JSON object.
    - **!list**: Lists all of the coding challenges from the JSON object.

## Further details
ChatQuotient-Bot is a simple chat bot, created with Python. With this bot, I solved the <a href="https://codingchallenges.fyi/challenges/challenge-discord/">**Build Your Own Discord Bot**</a> challenge from Coding Challenges website. Some details that should be mentioned: 
- The chatbot does not duplicate the challenges in the JSON object, if the challenge already exists it returns URL already exists:{url} 
- When adding a new challenge, the title is extracted from the website with the provided url.
- Since Discord does not allow to add more than 2000 characters in one message, the data was separated into chunks. Another way to list all the data is by creating a txt file but it is more visually appealing in this way.
