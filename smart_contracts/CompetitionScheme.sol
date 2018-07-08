pragma solidity ^0.4.0;


contract CompetitionScheme {

    function CompetitionScheme(){}

    function validateHash(uint256 _blocknumber, uint256 _blocktimestamp, uint256 _difficulty) public constant returns (uint256) {
        return uint256(keccak256(_blocknumber, _blocktimestamp, _difficulty));
    }
    
}