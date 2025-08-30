function PageValidate()
{
    var title = document.getElementById('title');
    var status = document.getElementById('status');

    if(title.value=='')
    {
        document.getElementById('error_title').innerHTML="Please enter title";
        return false;
    }
    if(status.value=='')
    {
        document.getElementById('error_status').innerHTML="Please select status";
        return false;
    }
}

function loginValidate()
{
    var username = document.getElementById('username');
    var password = document.getElementById('password');

    if(username.value.trim() == '')
    {
        document.getElementById('error_username').innerHTML = 'Please enter username';
        return false;
    }
    if(password.value.trim() == '')
    {
        document.getElementById('error_password').innerHTML = "Please enter password";
        return false;
    }
}







