function callGetAllEndpoint()
{
    try {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "http://127.0.0.1:3000/getAll", false );
        xmlHttp.send( null );
        return xmlHttp.responseText;
    } catch(e) {
        throw new Error("Cannot fetch endpoint 'getAll', is the server runnning?")
    }
}