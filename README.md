# Lottery

Block number for the lottery will be mined shortly on the Ropsten network! The block number we chose for this lottery is: **424140**

# How this works


While the above process may seem unnecessarily complicated, it is actually the most transparent way of performing a random lottery. It ensures that nobody can influence or manupulate the outcome in any way, and it allows every participant to verify the correctness of the outcome.


Let's break this whole process down.

Earlier today, we published 3 different things: the **tickets.json** file, the **lottery.py** file and a **smart contract**.

The tickets.json file contains a list of all lottery participants and their corresponding ticket values. The lottery.py file contains an implementation of the weighted Reservoir Sampling algorithm, which is capable of simulating the random drawing of tickets as would happen in an actual real-world lottery. The smart contract is simply there to give us the ability to turn an arbitrary block on the blockchain into a random long string of characters.

The real trick here is that the lottery.py file requires an argument to run. We call this argument the Random Seed. While the lottery.py file does indeed randomly draw winners, the randomness is controlled by the Random Seed and as long as it is run with the *exact same* seed, it will always draw winners in the exact same order.

So the question is, what Random Seed to we use? Do we use "hello, I am a seed"? Do we use "bethereum bounty lottery"? Or do we perhaps use some string of random characters like "zineytvlukzsdfhmgzlrt"?

None of these seeds would truly be random, because someone could create a seed that ensures they get drawn among the first people! We needed a truly random seed that nobody could predict and nobody could manipulate. Thus we turned to the Blockchain. By deciding to use the hash of a block that had not been created yet as the Random Seed, we relinquish control over the lottery outcome and leave it entirely up to chance.

As our seed, we chose the hash of block number 3595000, which would not be created for another few hours.

This seed was then used to run the lottery and calculate the results that can be found in the **Results.MD** file.
