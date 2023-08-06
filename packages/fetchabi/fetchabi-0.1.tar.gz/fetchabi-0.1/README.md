# fetch abi

A quick python script used to fetch an ethereum smart contracts ABI, if it is available on etherscan.

# How to use

Simply import the fetch-abi function and use the contract address as an argument. Target smart contract must be verified thus have its ABI available on etherscan.

    abi = fetch_abi("0xe11c90922BB5d6fe661B44039DA64c04b5B153E9")
    print(abi)

Gives

    {
        "abi": [
            {
                "inputs": [],
                "stateMutability": "nonpayable",
                "type": "constructor"
            },
            {
                "stateMutability": "payable",
                "type": "fallback"
            },
            {
                "inputs": [],
                "name": "implementation",
                "outputs": [
                    {
                        "internalType": "address",
                        "name": "",
                        "type": "address"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "stateMutability": "payable",
                "type": "receive"
            }
        ]
    }
