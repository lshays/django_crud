function mySubmit(id){
    console.log("yeet");
    $("#" + id).val("pressed");
    alert($("#" + id).val());
    alert($("#btn_submit").val());
    alert($("#btn_delete").val());
}