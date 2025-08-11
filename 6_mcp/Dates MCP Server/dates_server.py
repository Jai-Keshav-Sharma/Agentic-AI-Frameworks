import dates
from datetime import date
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dates_server")

@mcp.tool()
async def get_date_today() -> str:
    """This function fetches you the date today."""

    return dates.get_date()


if __name__ == "__main__":
    mcp.run(transport='stdio')