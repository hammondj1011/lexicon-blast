# lexicon-blast
This repo contains the source code used to automatically tweet Lexicon tweets from the F3Nashville and F3Nation accounts.

This script was built to allow F3Nation to automate tweets based on the Lexicon as populated by the pax. A few notes:

1. Lexicon terms and definitions are stored in a sqlite3 database.

2. This script utilizes the "python-twitter" module that must be imported through pip.

3. Timing was defined by Dark Helmet for F3Nation and Hambone defined the F3Nashville tweet timings.

4. Tweets utilizing this API must not have the same text. As such, the datetime is used in the tweet itself to help drive (some) uniqueness. a random number is generated to pick the line from the database that will be tweeted out.
