# Backend API - NFT Classifier App

## This API was built using Flask. It uses a classification ML model I trained to identify the top 3 NFTs on OpenSea: CryptoPunks, Bored Ape Yacht Club, and Mutant Ape Yacht Club. More NFTs will be supported soon!

API endpoints:

### GET /status

Returns a 200 OK to confirm server is running.

### POST /classify

Return a 200 OK with the NFT classification result, as long as the image format is valid (.jpg, .jpeg, .png).

## Frontend 
Here's the code for the [frontend](https://github.com/zahidkhawaja/NFT-Classifier)