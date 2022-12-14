from solcx import compile_standard, install_solc

with open("/Users/ashutoshhota/Coding/Web_3/SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
# print(simple_storage_file)

# Compile our Solidity Code

install_solc("0.8.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourcMap"]}
            }
        },
    },
    solc_version="0.8.0",
)
print(compiled_sol)
