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









