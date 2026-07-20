from fastmcp import FastMCP
import random
import json

#create a instance of FastMCP server
mcp = FastMCP('Simple Calculator Server')

#Tool: Add two numbers
@mcp.tool()
def add(a: int,b: int) -> int:
    """Add two numbers together
    args:
            a: first number
            b: second number
        
    Returns:
        The sum of a and b"""
    
    return a + b

#Tool: Generate a random number
@mcp.tool()
def random_number(min_val: int = 1,max_val:int = 100) -> int:
    """Generate a random number within a given range"""

    return random.randint(min_val,max_val)

#Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    "Get inforamtion about this server."
    info = {
        "name" : "Simple Calculator Server",
        "version" : "1.0.0",
        "description" : "A basic MCP server with math tools",
        "tools" : ["add","random_number"],
        "author" : "Afroz"
    }

    return json.dumps(info,indent= 2)

#Start the server
if __name__ == '__main__':
    mcp.run(transport='http',host = '0.0.0.0',port = 8000)