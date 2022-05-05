# Flask Server for NFT Classifier App

## Powered by this machine learning [classification model](https://www.github.com/zahidkhawaja)

API endpoints:

### GET /status

Returns a 200 OK to confirm server is running.

### POST /classify

Return a 200 OK with the NFT classification result, as long as the image format is valid (.jpg, .jpeg, .png).

Currently, this classification API works on the top 3 NFTs on OpenSea: CryptoPunks, Bored Ape Yacht Club, and Mutant Ape Yacht Club. Click [here](https://www.github.com/zahidkhawaja) to learn more about how this model was trained, More NFTs will be supported soon.