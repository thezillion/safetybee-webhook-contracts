pragma experimental ABIEncoderV2;

contract HelpMe {
    
    address owner;
    uint reqId;
    
    struct Request {
        uint requestId;
        address requesterAddr;
        string latLong;
    }
    
    struct Help {
        uint requestId;
        address helperAddr;
    }
    
    Request[] public requests;
    Help[] public helps;
    
    function HelpMe() public {
        owner = msg.sender;
        reqId = 0;
    }
    
    function addRequest(address requester, string _latLong) public {
        Request memory req = Request(reqId, requester, _latLong);
        requests.push(req);
        reqId++;
    }
    
    function addHelp(uint reqId, address helper) public {
        Help memory hlp = Help(reqId, helper);
        helps.push(hlp);
    }
    
    function getAllRequests() public constant returns (Request[]) {
        return requests;
    }
    
    function kill() public {
        if(msg.sender == owner) selfdestruct(owner);
    }
    
}