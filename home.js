
// Request following info from server on startup

// Store info relating to site account
let User = {
    Username,
    Password,
    EmailAccounts: [],
    Settings = {
        ActiveAccounts: [],
        Tags: [],
    }        // Make an object instead?
};
/*
let settings = {
    ActiveAccounts: [],
    Tags: [],
}
*/


let Emails = {
    From,
    To,
    Subject,
    Msg,
    Folders : [],
    Tags
};


////////////////////////////////////////////////  Home page functions //////////////////////////////////////////////////////////////
/*
function populateData(){    // Gets user data from backend. Sets up connection.

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("demo").innerHTML = this.responseText;
        }
      };
      xhttp.open("POST", "demo_post2.asp", true);
      xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

      //xhttp.send("fname=Henry&lname=Ford");
    // Receive data from backend
        //TODO

    // Store to web cache
    sessionStorage.User = User.Username;
    //sessionStorage.EmailAccounts = User.EmailAccounts;
    //sessionStorage.settings = User.Settings;
}
*/

function signout(){ // Signs user out of account, clears data, links back to the log in page.
    // Saves settings and sends them to backend
    updateSettings();

    // Clears web cache
    sessionStorage.clear(); 

    // Exits page and goes to login page
    window.location.href = "http://52.12.189.175:8000/loginPage.html";
}

/*
function hideEmailAccount(){    // Removes all emails from a specific email server from the inbox.
    // Updates list of availabe email accounts (removal)
    // Rebuilds EmailList with updated list of available email addresses 
}
*/
function showEmailAccount(){    // Adds all the emails from a specific email server to the inbox.
    // Updates list of availabe email accounts  (addition)
    // Rebuilds EmailList with updated list of available email addresses 
}



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////  Settings Page functions  ///////////////////////////////////////////////////////////

function addEmailAccount(){     // Sends backend a request to add a new email account.
    // Takes in email account info
    // sends info to backend
    // if fail, returns error
    // if back end is able to add, gives user success message
    // adds email account to list of email accounts
    // Updates list of available email accounts (addition)
    // Rebuilds EmailList with updated list of available email addresses
}

function removeEmailAccount(){  // Send backend a request to remove an email account.
    // Checks value of email address with backend
    // Sends request to remove account
    // Once request is approved, removes email from user settings
    // Updates list of available email accounts (removal)
    // Rebuilds EmailList with updated list of available email addresses 
}

function deleteUserAccount(){   // Sends backend a request to delete the users MailConnect account and all associated data.
    // asks if user wants to confirm
    // sends back end request to delete account
    // calls signout function
}

function addTag(){      // Creates a new tag that emails can be associtated with.
    // Adds new tag to list of tags
}

function removeTag(){   // Removes an existing tag that emails can be associate with.
    // Removes tag from list of tags
    // Sends backend request to remove tags from emails
    // Rebuilds EmailList with updated list of available tags  
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//////////////////////////////////////////  Email list functions  /////////////////////////////////////////////////////////////////


function buildEmailList(){   // Pulls emails from backend and displays them in emailpit.    (DONE)

    // asks backend for emails asscociated with given account or email accounts
    // receives emails and parses them for sender, subject, timestamp, tags
    var Emails = JSON.parse(getJSON("loadEmails()")); 
    sessionStorage.EmailCache = Emails;

    // condesnses email into a html emailcontainer and appends to emailpit list.
    for(let i=0; i < Emails.length; i++){
        // Get sender
        let sender = document.createElement("p");
        sender.setAttribute('class','Email Sender')
        sender.textContent = Emails[i].From;

        // Get Subject
        let subject = document.createElement("p");
        subject.setAttribute('class','Email Subject')
        subject.textContent = Emails[i].Subject;

        // Get Time stamp?
        /*
        let timestamp = document.createElement("p");
        timestaamp.setAttribute('class','Email Time')
        timestamp.textContent = Emails[i].Time;
        */
       
        // Add email attributes to email container
       var div = document.createElement("div");
       div.setAttribute('class', 'd-flex flex-row justify-content-between align-items-center Email Section');

        // checks sender and determines if risk or not. If risk, add risk attribute to email
        accountJSON = JSON.stringify(sender);
        if(JSON.parse(getJSON("checkAccount("+ accountJSON +")")).suspicious){
            var warning = document.createElement("i");
            warning.setAttribute('class','fa fa-warning Email Warning')
            div.appendChild(warning);
        }
       div.appendChild(Sender);
       div.appendChild(Subject);

       var a = document.createElement("a");
       a.setAttribute('class', 'Email Section');
       a.setAttribute('href','EmailView.html');
       a.setAttribute('onclick','displayEmail('+ i +')');
       a.appendChild(div);        

        let email = document.createElement("li");
        email.setAttribute('class','Email_Line');
        email.appendChild(a);
    }
}

/*
function displaySendbox(){  // replaces emailpit list with a box to send a text email.
    //call email sender (already done in html)
}
*/

function selectTag(){   // Calls all the emails the are associated with a tag.
    // searches for all emails with tag (might be a backend function that does this?)
    // request for search criterea either from backend, or through currently avialable emails.
}

function sort(){    // Sorts emails by date
    // redisplays emails in reverse, with oldes first
}

/*
function search (){     // Searches available emails in inbox based on sender name
    //let search = document.getElementById("MainSearchBar");  // Grabs value in search bar
    // POST(search) to backend search function
    // Read back input from backend search function'
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("MainSearchBar");   // Grabs value in search bar
    filter = input.value.toUpperCase();
    ul = document.getElementById("EmailPitList");   // 
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("div")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }

}
*/

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



///////////////////////////////////////////////////////  Email view functions ////////////////////////////////////////////////////
function displayEmail(index){    // When an email banner is clicked, replace the emailpit list with the email view. Index is given by   (DONE)
    // call email view (already done in html)
    var Email = sessionStorage.EmailCache[index];
    // Check if warning needs to be displayed
    accountJSON = JSON.stringify(Email.From);
    if(JSON.parse(getJSON("checkAccount("+ accountJSON +")")).suspicious){
        let Warning = document.getElementById("WarningField");
        Warning.setAttribute('class', 'EmailContent WARNING');  // Resets the class to make the warning visible. By default it is not displayed.
    }

    // Fill the fields with the appropiate info
    document.getElementById("FromField").value = Email.From;
    document.getElementById("ToField").value = Email.To;
    document.getElementById("SubjectField").value = Email.Subject;
    document.getElementById("MainField").value = Email.Msg;
    
    // Overwrite reply and forward buttons
    let reply = document.getElementById("Reply");
    let forward = document.getElementById("Forward");

    reply.setAttribute('onclick', 'reply('+ index +')');
    forward.setAttribute('onclick', 'forward('+ index +')');
}

function deleteEmail(){ // Deletes the email (ABANDONED, too complex to impliment at this stage)
    // Sends server request to delete email
    // calls displayEmailList()
}

function reply(index){  // (DONE)
    // calls email sender and tells it to prepopulate TO, FROM, SUBJECT, and CONTENT fields
    sender(index, "reply");

}

function forward(index){    // (DONE)
    // calls email sender and tells it to prepopulate all fields except TO
    sender(index, "forward");
}

/*
function clearview(){   //clears view cache (REDUNDENT, different method used)
    // emptys view cache
    // returns to email list (already done in html)
}
*/

function manageTags(){  // allows user to add or remove tags from existing email (ABANDONED, too complex to impliment at this stage)
    // I dont know what to do here
}

/*
function flagSuspectEmail(){    // Notifiies user that an email is suspicious. (REDUNDENT)
    // Displays warning field above email information field and gives reason for warning, if returned.
}
*/
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////////////// Email Send functions  //////////////////////////////////////////////////////////////    --------------------------------------------------------| TODO
function sender(index, caller){
    // populate send list with list of all email accounts
    // check if given send request by reply or forward, if so, prepopulate those fields
    // if not, add first email account to the FROM field
}

function changeSender(){
    // Given a sender selection from sender account list
    // replace current value of FROM field with new value given
}

function reccomendJoke(category){   // Recommends joke based on user input.
    // Given a joke type, ask backend for a joke of that types
    var joke = JSON.parse(getJSON("getJoke("+ category +")"));
    
    /*
    for (var name in group) {
    if (group.hasOwnProperty(name)) {
        var value = group[name];
        // Do something
    }
}
    */
    // When joke is returned, add it to the end of email
    var myTextArea = $('#myTextarea')
    myTextArea.val(myTextArea.val() + joke);

    // Notify user that joke is saved in clipboard
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////////////////////  Universal functions //////////////////////////////////////////////////////////////
function updateSettings() { // Sends an update request to backend whenever user makes a change to settings that will last longer than the current session.
    // TODO: figure out which python file to send request to, and what format, POST or json to send the settings as ---------------------------------------------------------------| TODO
}

function displayEmailList(){    // When the user clicks to return to inbox, replace the current view with the emailput list. (REDUNDENT)
    // Switches to Email List
    buildEmailList();
}

var getJSON = function(url, callback) {     // Connection protocols for communicating with server.
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



/*
function EmailAccounts(){

}
*/

/*
for (i = 0; i < EmailAccounts.length; i++){
    
    var node = document.getElementById("EmailAccountsList");    // Create a new account node
    //var textnode = document.createTextNode("Water");         // Create a text node
    node.appendChild(textnode);                              // Append the text to <li>
    document.getElementById("myList").appendChild(node);
    
}
*/

//document.getElementById("EmailAccountsList").innerHTML = 