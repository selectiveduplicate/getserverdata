// create a new XMLHttpRequest object 
var newXhr = new XMLHttpRequest();
// initialize a request and log the status response
newXhr.open('GET', 'http://0.0.0.0:8000/directory_structure.xml', true);
newXhr.responseType = 'document';

newXhr.onload = function () {
    if (newXhr.readyState == newXhr.DONE && newXhr.status == 200) {
        // console.log(newXhr.response, newXhr.responseXML.baseURI);
        window.open(newXhr.responseXML.baseURI)
    }
}

newXhr.send()
