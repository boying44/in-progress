function httpGet()
{
    var xmlHttp = new XMLHttpRequest();
    //token expired
    var theURL = "https://graph.facebook.com/v2.9/me/friends?fields=id,name,birthday&access_token=EAACEdEose0cBAFg6ZCDbZB61ZCTlNLYIKEMXcL5asK1fM1QfZChnVSA4WWvR7ixYAZC2flDpkkAwBcJMYuYsu8SBjycbnZC28awEXSCGe9xL6ElQMwZA0XnWl6BDUfFynmdUMGOLp6lTTpR6cRZAQXl6vhjq4PcWDU4MUCBeiQy6gCHZA4NS8nSUTnmtwvoYgHPIZDl"
    xmlHttp.open( "GET", theURL, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log( xmlHttp.responseText);
}

httpGet()