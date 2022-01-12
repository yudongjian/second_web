
// this is upload file
$('#button123').on('click', function () {
    $.ajax({
            url: "/upload_file",
            type: "POST",
            success: function (result) {
                const result_json = JSON.parse(result);
                if(result_json['flag']=='success'){
                    alert("upload file success")
                }else {
                    alert("upload file err!!!!")
                }
            }
        }
    );
});

// check file size
$(':file').on('change', function () {
  var file = this.files[0];

  if (file.size > 1024 * 1024 * 1024) {
    alert('max upload size is 1G');
  }else if (file.size > 1024 * 1024 * 10) {
    alert('max upload size is 10M');
  }
});

// upload percent
// function start_upload(n)
// {
//     if(n==0){alert("上传完成")}
//     var progress1=document.getElementById("uploadfile_progress")
//     n=n-1
//     cur_task = 100-n
//     progress1.value=cur_task
//     setTimeout("start_run("+n+")",100)
//
// }