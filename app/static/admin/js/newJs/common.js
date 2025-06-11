//console.log("hi");
var f_c ="red";
var brdr = "2px solid red";

function IsEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}//end IsEmail

function IsMobile(phone) {
  //var regex = /^([0-9]{10})+$/;
  var regex = /^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$/;
  return regex.test(phone);
}//endIsPhone

function Removef(nm)
{
  //$('#'+nm).css('border','1px solid #DEE2E6');
  $("#error_"+nm).html('');
}

function showPwd(nm)
{
  if('password' == $('#'+nm).attr('type')){
         $('#'+nm).prop('type', 'text');
    }else{
         $('#'+nm).prop('type', 'password');
    }
}

function RemoveER(nm)
{
  
  $('#'+nm).css('border','1px solid #DEE2E6');
  $("#error_"+nm).html('');
}

function clearCache()
{
   var epath = admin_pth+'/clear-cache';
   
   $.ajaxSetup({
      headers: {
          'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
      }
  });
  $.ajax({
          type:'get',  
              url:epath,
              cache: false,
              beforeSend: function () {
              $(".preload").show();
            },
              success:function(data){
                         
                 var obj = JSON.parse(data);
          if (obj.error) 
          {
            Message.add(obj.message,{skin:'ico-medium',type:'warning',vertical:'top',horizontal:'center',icon:true,close:false,life:'3000'});               
          }
          else
          {
            Message.add(obj.message,{skin:'ico-medium',type:'success',vertical:'top',horizontal:'center',icon:true,close:false,life:'3000'});    
         }
                },
        error : function(err)
        {
          console.log(err);
          Message.add('Internal Server Error',{skin:'ico-medium',type:'warning',vertical:'top',horizontal:'center',icon:true,close:false,life:'3000'});
        },
        complete: function () {
              $(".preload").hide();
            }

      
  }); 

}

function loadFile(nm,errId)
{
  $('#'+nm).css('border','1px solid #DEE2E6');
  $("#"+errId).hide();
}


  function checkList()
{
 

   if ($('#selectAll').is(':checked')) {
          $('#tbody input[type=checkbox]').attr('checked', 'checked');           
     }
     else {
          $('#tbody input[type=checkbox]:checked').removeAttr('checked');
     }
}

$("#selectAll").click(function(){
        $("input[name=master]").prop('checked', $(this).prop('checked'));

});

function deleteSelected(path)
 {
  
  var id = [];
    $.each($("input[name='master']:checked"), function(i){
        id[i] = $(this).val()
    });    
   console.log(id);  
   dataVal = {
    'id' : id
    };        
  var epath = path;//b_path+path;  
  console.log(epath, dataVal);
   if(id.length ===0)    
            {    
                alert("Please select row(s).");    
            }  else {  
    if(confirm("Are you sure you want to delete this ?"))
    {          

  $.ajax({
                type:'get',
                url:epath,
                cache:false,
                data:dataVal,
                dataType:"json",
                success:function(obj){
                console.log(obj);
                  outputMsg(obj.error, obj.msg);
                  if(obj.error==false)
                  {
                  setTimeout(() => {
                  window.location.reload(true); 
                  }, time_period);
                  }
                  },
                  error:function(err)
                  {
                    console.log(err)
                    serverError()
                  }
           });
}
}
 }


function updateSelected(path)
 {
  
  var id = [];
    $.each($("input[name='master']:checked"), function(i){
        id[i] = $(this).val()
    });    
   console.log(id);  
   dataVal = {
    'id' : id
    };
  var epath = path;          
  console.log(epath, id)
   if(id.length <=0)    
            {    
                alert("Please select row(s).");  
                return false;  
            }  else {  

  $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                type:'get',
                url:epath,
                data:dataVal,
                dataType:"json",
                success:function(obj){
                  outputMsg(obj.error, obj.msg);
                  setTimeout(() => {
                  window.location.reload(true); 
                  }, time_period);
                  },
                  error:function(err)
                  {
                    console.log(err)
                    serverError();
                  }
           });

}
 }



function dataSave(fm, btn, pth, mtd)
{
  if(mtd() != false)
  {
var formData = $("#"+fm).serialize();
var submit_btn_text=$("#"+btn).html();   
var epath = pth;//b_path+pth;
var creditory_type = $("#creditory_type").val();
 console.log(fm, btn, epath, creditory_type);
  $.ajax({
          headers: { "X-CSRFToken": csrftoken },
          type:'post',  
              url:epath,
              data:formData,
              cache: false,
              beforeSend: function () {
             $("#"+btn).prop("disabled", true);
              $("#"+btn).html('Please wait...'); 
            },
              success:function(obj){
                  // console.log(obj);  
                  outputMsg(obj.error, obj.msg);
            //       setTimeout(() => {
            //   window.location.reload(true);
            // }, time_period); 
          
               },
        error : function(err)
        {
          console.log(err);
          serverError(obj.msg)
        },
        complete: function () {
              $("#"+btn).removeAttr("disabled"),jQuery("#"+btn).html(submit_btn_text); 
            }     
  });
}

}

function dataNormalSave(fm, btn, pth, mtd) {
  if (mtd() !== false) {
    var form = document.getElementById(fm);
    var formData = new FormData(form);
    var submitBtn = document.getElementById(btn);
    var submitBtnText = submitBtn.innerHTML;
    var epath = pth; // b_path + pth;

    console.log(fm, btn, epath, formData);
    fetch(epath, {
      method: 'POST',
      headers: {
        "X-CSRFToken": csrftoken
      },
      body: formData,
      cache: "no-cache"
    })
      .then(response => response.json()) 
      .then(obj => {
        console.log(obj);
        outputMsg(obj.error, obj.msg);
          // setTimeout(() => { window.location.reload(true); }, time_period);
      })
      .catch(err => {
        console.log(err);
        serverError(err);
      })
      .finally(() => {
        submitBtn.disabled = false;
        submitBtn.innerHTML = submitBtnText;
      });
    submitBtn.disabled = true;
    submitBtn.innerHTML = 'Please wait...';
  }
}

// function dataNormalSave(fm, btn, pth, mtd)
// {
//   if(mtd() != false)
//   {
// var formData = new FormData($('#'+fm)[0]); 
// var submit_btn_text=$("#"+btn).html();   
// var epath = pth;//b_path+pth;
//  console.log(fm, btn, epath, formData);
//   $.ajax({
//           headers: { "X-CSRFToken": csrftoken },
//           type:'post',  
//               url:epath,
//               data:formData,
//               cache: false,
//               contentType: false,  
//               processData:false,
//               beforeSend: function () {
//              $("#"+btn).prop("disabled", true);
//               $("#"+btn).html('Please wait...'); 
//             },
//               success:function(obj){
//                    console.log(obj);  
//                   outputMsg(obj.error, obj.msg);
//             //       setTimeout(() => {
//             //   window.location.reload(true);
//             // }, time_period); 
          
//                },
//         error : function(err)
//         {
//           console.log(err);
//           serverError(err)
//         },
//         complete: function () {
//               $("#"+btn).removeAttr("disabled"),jQuery("#"+btn).html(submit_btn_text); 
//             }     
//   });
// }

// }

function dataEditorSave(fm, btn, pth, mtd) {
    if (mtd() !== false) {

        for (let instance in CKEDITOR.instances) {
            CKEDITOR.instances[instance].updateElement();
        }

        var form = document.getElementById(fm); 
        var formData = new FormData(form);
        var submitBtn = document.getElementById(btn); 
        var submitBtnText = submitBtn.innerHTML;  
        var epath = pth; 

        //console.log(fm, btn, epath, formData);

        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Please wait...';

        fetch(epath, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(obj => {
            console.log(obj);
            outputMsg(obj.error, obj.message);
            // setTimeout(() => {
            //     window.location.reload(true);
            // }, time_period);
        })
        .catch(err => {
            console.error(err);
            serverError(err);
        })
        .finally(() => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = submitBtnText;
        });
    }
}

function deleteData(pth, aid, mtd) {
  var epath = pth;
  console.log(epath);

  // Using SweetAlert for confirmation
  swal({
    text: "Do you want to remove?",
    icon: "warning",
    buttons: ["No", "Yes"],
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
    
      fetch(epath, {
        method: mtd,
        cache: 'no-cache'
      })
      .then(response => response.json())
      .then(obj => {
        console.log(obj);
        outputMsg(obj.error, obj.message); 
      
         setTimeout(() => { window.location.reload(true); }, time_period);
      })
      .catch(err => {
        console.log(err);
        serverError(); 
      })
      .finally(() => {
        document.getElementById(aid).disabled = false; 
      });

    
      document.getElementById(aid).disabled = true;
    }
  });
}


// function deleteData(pth, aid)
// {
  
//   var epath = pth;
//   console.log(epath)
//   swal({
//     //title: "Are you sure?",
//     text: "Do you want to remove ?",
//     icon: "warning",
//     buttons: ["No", "Yes"],
//     dangerMode: true,
//   })
// .then((willDelete) => {
//     if (willDelete) {
// $.ajaxSetup({
// headers: {
//   'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
// }
// });
//   $.ajax({
//       type: 'get',
//       url:epath,
//       cache: false,
//       beforeSend: function () {
//      $("#"+aid).prop("disabled", true); 
//     },
//       success: function(obj) {
//         console.log(obj)
//         outputMsg(obj.error, obj.msg);
//             //  setTimeout(() => {
//             //   window.location.reload(true);
//             // }, time_period); 
//       },
//       error:function(err)
//       { 
//         console.log(err)
//           serverError();
//       },
//       complete: function () {
//         $("#"+aid).prop("disabled", false);
//     }
//   })
// }})
// }